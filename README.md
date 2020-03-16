# CLEF2020-CheckThat! Task 2
This repository contains the _dataset_ for the [CLEF2020-CheckThat! task 2](https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval).

It also contains the _format checker, scorer and baselines_ for the task.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 1.0: March ?, 2020 (Data and Baseline Release)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 2
on evidence retrieval estimation dataset provided for the CLEF2020-CheckThat! Lab
on "Automatic Identification and Verification of Claims".
The current TRIAL version (1.0, March ?, 2020) corresponds to the release of a
part of the training data set.
The test set will be provided in future versions.
All changes and updates on these data sets and tools are reported in Section 1 of this document.

__Table of contents:__
* [Evaluation Results](#evaluation-results)
* [List of Versions](#list-of-versions)
* [Contents of the Distribution v1.0](#contents-of-the-distribution-v10)
* [Data Format](#data-format)
* [Results File Format](#results-file-format)
* [Format checkers](#format-checkers)
* [Scorers](#scorers)
   * [Evaluation metrics](#evaluation-metrics)
* [Baselines](#baselines)
* [Notes](#notes)
* [Licensing](#licensing)
* [Citation](#citation)
* [Credits](#credits)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/03/?]__ - Training data. The training data for task 2 contains (626) Tweets and (518) NormClaims obtained from snopes.com.

## Contents of the Distribution v1.0

We provide the following files:

- Main folder: [data](data)
  - [verified_facts.qrels.tsv](data/verified_facts.qrels.tsv) <br/>
	Contains all the verified claims used for fact checking released with the version 1.0
  - Subfolder [/train](data/train)
	Contains all training data released with the version 1.0
	- [tweets](data/train/tweets.queries.tsv)
		Contains information for training tweets.
	- [tweet-fact-pairs.qrels](data/train/tweet-fact-pairs.qrels)
		Contains the correct pairs between tweet and verified claims

  * [README.md](README.md) <br/>
    this file


## Data Format

The datasets are text files with the information TAB separated. The text encoding is UTF-8. You will get:

### NormClaims:

All the verified claims that will be used for both training and test are found in file (data/verified_facts.qrels.tsv). This file has information about the verified claims that are obtained from snopes.com in the following format.

> NormClaimID [TAB] NormClaim [TAB] Title

Where: <br>
* NormClaimID: unique ID for a given NormClaim <br/>
* NormClaim: text of the fact/verified claim <br/>
* Title: title of the document fact checking the verified claim <br/>

Example:

2       "A ""law to separate families"" was enacted prior to April 2018, and the federal government is powerless not to enforce it."       Was the ‘Law to Separate Families’ Passed in 1997 or ‘by Democrats’?r
222     Former U.S. Vice President Joe Biden owns the largest mansion in his state.     Does Joe Biden Own the Largest Mansion in His State?
503     "U.S. Sen. Bernie Sanders compared Baltimore to a ""third world country."""     Did U.S. Sen. Bernie Sanders Say Baltimore Was Like a ‘Third World Country’?

### Queries file:

Tweet details that are used for training or testing.
It is a text files with the information TAB separated.
The text encoding is UTF-8.

> tweetID [TAB] tweet

Where: <br>
* tweetID: unique ID for a given tweet <br/>
* tweet: text of the tweet <br/>

Example:

8       im screaming. google featured a hoax article that claims Minecraft is being shut down in 2020 pic.twitter.com/ECRqyfc8mI — Makena Kelly (@kellymakena) January 2, 2020
335     BREAKING: Footage in Honduras giving cash 2 women & children 2 join the caravan & storm the US border @ election time. Soros? US-backed NGOs? Time to investigate the source! pic.twitter.com/5pEByiGkkN — Rep. Matt Gaetz (@RepMattGaetz) October 17, 2018
622     y’all really joked around so much that tide put their tide pods in plastic boxes…smh pic.twitter.com/Z44efALcX5 — ㅤnavid (@NavidHasan\_) January 13, 2018

### Qrels file:

A file containing information about the pairs of tweet and verified claims;
such that the verified claim (__NormClaimID__) proves the tweet (__tweetID__).
It is a text files with the information TAB separated.
The text encoding is UTF-8.

> tweetID [space] 0 [space] NormClaimID [space] label

Where: <br>
* tweetID: unique ID for a given tweet. Tweet details found in the queries file. <br/>
* 0: literally 0.
* NormClaimID: unique ID for a given NormClaim. NormClaim details found in the NormClaim file. <br/>
* label: 1 if the pair __tweetID__ and __NormClaimID__ make a pair such that the NormClaim corresponding to __NormClaimID__ proves the tweet corresponding to __tweetID__; 0 otherwise.

Example:
437 0 2 1
437 0 3 1
342 0 333 1
190 0 626 1

## __Results File Format__:

For this task, the expected results file is a list of claims with the estimated score for check-worthiness.
Each line contains a tab-separated line with:
>TweetID [space] 0 [space] NormClaimID [space] rank [space] score [space] tag

Where _TweetID_ is ID of the tweet given in the TweetInfo.queries file, _NormCLaimID_ is ID of the normalized claim found in NormClaims.docs, _score_ is the score given by your model for the pair _TweetID_, _NormCLaimID_ and _rank_ is the rank of the pair given the scores of all possible pairs for a given _TweerID_, and _tag_ is a string identifier used by participants.
 For example:
>1 0 1 1 0.9056 modelX <br/>
>1 0 2 2 0.6862 modelX <br/>
>2 0 1 2 0.1023 modelX <br/>
>2 0 2 1 0.235 modelX <br/>
> ...

Your result file **MUST contain at most 1,000 NormClaims per tweet** from the respective input file.
Otherwise the scorer will not score this result file.

## Format checkers

TBA

## Scorers
    - [evaluate.py](/evaluate.py) - Returns the metrics needed for evaluation

### Evaluation metrics

For Task 3 (ranking): R-Precision, Average Precision, Reciprocal Rank, Precision@k and means of these over all verified claims.
**The official metric for task3, that will be used for the competition ranking is the Mean Average Precision (MAP)**

You can use these repos as reference for the evaluation, https://github.com/joaopalotti/trectools and https://github.com/usnistgov/trec_eval.

## Baselines

To use the Elastic Search baseline you need to have a locally running Elastic Search instance.
You can follow [this](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html) article for Elastic Search installation. Alternatively, if you have docker installed, you can run it using only this command:
> docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.1

When you have Elastic Search running you can run the baseline script use the following:

> python3 elastic_search_baseline.py --facts data/verified_facts.docs.tsv --tweets data/train/tweets.queries.tsv --predict-file es-score-prediction.txt <br/>

## Licensing

  These datasets are free for general research use.

## Citation


## Credits

Task 3 Organizers:

* Nikolay Babulkov, Sofia University <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/
**The official rules are published on the website, check them!**

Contact:   clef-factcheck@googlegroups.com

