import os
import json
import numpy as np
import pandas as pd
import argparse
from elasticsearch import Elasticsearch

from lib.logger import logger

PREDICT_FILE_COLUMNS = ['qid', 'Q0', 'docno', 'rank', 'score', 'tag']

def build_index(es, vclaims, fieldnames):
    try:
        es.indices.delete(index='vclaim')
    except:
        pass

    for i, vclaim in vclaims.iterrows():
        if not es.exists(index='vclaim', id=i):
            body = vclaim.loc[fieldnames].to_dict()
            es.create(index='vclaim', id=i, body=body)
    logger.info(f"Built index ({vclaims.shape[0]} vclaims) with fieldnames: {fieldnames}")

def get_score(es, tweet, search_keys, size=10000):
    query = {"query": {"multi_match": {"query": tweet, "fields": search_keys}}}
    try:
        response = es.search(index="vclaim", body=query, size=size)
    except:
        logger.error(f"No elasticsearch results for {tweet}")
        raise

    results = response['hits']['hits']
    for result in results:
        info = result.pop('_source')
        result.update(info)
    df = pd.DataFrame(results)
    df['id'] = df._id.astype('int32').values
    df = df.set_index('id')
    return df._score

def get_scores(es, tweets, vclaims, search_keys, size):
    size_tweets, size_vclaims = max(tweets.index), max(vclaims.index)
    scores = {}

    logger.info(f"Get RM5 scores for {size_tweets} tweets and {size_vclaims} vclaims")
    for i, tweet in tweets.iterrows():
        score = get_score(es, tweet.tweet_content, search_keys=search_keys, size=size)
        scores[i] = score
    return scores

def create_connection(conn_string='127.0.0.1:9200'):
    logger.debug("Start ElasticSearch listener")
    es = Elasticsearch([conn_string])
    logger.debug("Elasticsearch connected")
    return es

def format_scores(scores):
    formatted_scores = []
    for tweet_id, s in scores.items():
        for vclaim_id, score in s.items():
            row = (str(tweet_id), 'Q0', str(vclaim_id), '1', str(score), 'elasic')
            formatted_scores.append(row)
    formatted_scores_df = pd.DataFrame(formatted_scores, columns=PREDICT_FILE_COLUMNS)
    return formatted_scores_df

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vclaims", "-v", required=True,
                        help="TSV file with vclaims. Format: vclaim_id vclaim title")
    parser.add_argument("--tweets", "-t", required=True,
                        help="TSV file with tweets. Format: tweet_id tweet_content")
    parser.add_argument("--predict-file", "-p", required=True,
                        help="File in TREC Run format containing the model predictions")
    parser.add_argument("--keys", "-k", default=['vclaim', 'title'],
                        help="Keys to search in the document")
    parser.add_argument("--size", "-s", default=10000,
                        help="Maximum results extracted for a query")
    parser.add_argument("--conn", "-c", default="127.0.0.1:9200",
                        help="HTTP/S URI to a instance of ElasticSearch")
    return parser.parse_args()

def main(args):
    vclaims = pd.read_csv(args.vclaims, sep='\t', index_col=0)
    tweets = pd.read_csv(args.tweets, sep='\t', index_col=0)

    es = create_connection(args.conn)
    build_index(es, vclaims, fieldnames=args.keys)

    scores = get_scores(es, tweets, vclaims,
                        search_keys=args.keys, size=args.size)
    formatted_scores = format_scores(scores)
    formatted_scores.to_csv(args.predict_file, sep='\t', index=False, header=False)
    logger.info(f"Saved scores from the model in file: {args.predict_file}")

if __name__=='__main__':
    args = parse_args()
    main(args)
