import sys
import argparse
import pandas as pd
from trectools import TrecRun, TrecQrel, TrecEval
from os.path import join, dirname, abspath

sys.path.append(join(dirname(abspath(__file__)), 'lib'))
from logger import logger
from format_checker import run_checks

METRICS = ['map', 'precision', 'reciprocal_rank']
MAX_DEPTH = 10000
METRICS_DEPTH = [1, 3, 5, 10, 20, MAX_DEPTH]
SCORES_COLUMNS = ['metric', '@depth', 'score']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scores', '-s', required=True,
                        help='File with predicted scores from your model.\
                        Format: qid Q0 docid rank score tag')
    parser.add_argument('--gold-labels', '-g', required=True,
                        help='File with gold labels. Format: qid 0 docid relevance')
    parser.add_argument('--metrics', '-m', choices=METRICS, action='append',
                        help='Metrics for evaluation. \
                        This parameter can be added multiple times with different metrics.')
    parser.add_argument('--depths', '-d', choices=METRICS_DEPTH, action='append', type=int,
                        help='Depth of evaluation. Example: Recall@K, Precision@K.\
                        This parameter can be added multiple times.')
    parser.add_argument('--output', '-o',
                        help='Output file with metrics.\
                        If not specified, prints output in stdout.')
    return parser.parse_args()

def extract_metrics(results, metrics, depths):
    metrics, depths = metrics or METRICS, depths or METRICS_DEPTH
    scores = pd.DataFrame([], columns=SCORES_COLUMNS)
    for metric in metrics:
        for depth in depths:
            score = {}
            metric_fn = eval(f'results.get_{metric}')
            score['metric'] = metric
            score['@depth'] = depth
            score['score'] = '{:,.3f}'.format(metric_fn(depth=depth))
            scores = scores.append(score, ignore_index=True)
    return scores

def main(args):
    format_check_passed = run_checks(args.scores)
    if not format_check_passed:
        return
    gold_labels = TrecQrel(args.gold_labels)
    prediction = TrecRun(args.scores)

    results = TrecEval(prediction, gold_labels)
    metrics = extract_metrics(results, args.metrics, args.depths)

    metrics.loc[:, '@depth'] = metrics.loc[:, '@depth'].astype(str)
    metrics.loc[:, '@depth'] = metrics.loc[:, '@depth'].replace(str(MAX_DEPTH), 'all')
    if args.output:
        metrics.to_csv(args.output, sep='\t', index=False)
        logger.info(f'Saved results to file: {args.output}')
    else:
        print(metrics.to_string(index=False))

if __name__=='__main__':
    args = parse_args()
    main(args)
