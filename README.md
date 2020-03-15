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

* __v1.0 [2020/03/?]__ - Training data. The training data for task 2 contains (?) Tweets and (?) NormClaims obtained from snopes.com.

## Contents of the Distribution v1.0

We provide the following files:

- Main folder: [data](data)
  - [verified_facts.tsv](data/verified_facts.tsv) <br/>
	  Contains all the verified claims used for fact checking released with the version 1.0
  - Subfolder [/training](data/training)
	  Contains all training data released with the version 1.0
  	- [tweets.train.queries](data/training/tweets.train.queries)
  		Contains information for training tweets.
  	- [pairs.train.qrels](data/training/pairs.train.qrels)
  		Contains the correct pairs between tweet and verified claims

  * [README.md](README.md) <br/>
    this file
  

## Data Format

The datasets are text files with the information TAB separated. The text encoding is UTF-8. You will get 

### NormClaims:

All the verified claims that will be used for both training and test are found in file (data/verified_facts.tsv). This file has information about the verified claims that are obtained from snopes.com in the following format. 

> NormClaimID [TAB] title [TAB] NormClaim [TAB] body

Where: <br>
* NormClaimID: unique ID for a given NormClaim <br/>
* title: title of the document fact checking the verified claim <br/>
* body: body of the document fact checking the verified claim <br/>
* NormClaim: text of the verified claim <br/>

Example:

// TODO: Add example here

### Queries file:

Tweet details that are used for training or testing. 
It is a text files with the information TAB separated. 
The text encoding is UTF-8.

> tweetID [TAB] tweet

Where: <br>
* tweetID: unique ID for a given tweet <br/>
* tweet: text of the tweet <br/>

Example:

// TODO: Add example here

### Qrels file:

A file containing information about the pairs of tweet and verified claims;
such that the verified claim (__NormClaimID__) proves the tweet (__tweetID__).
It is a text files with the information TAB separated. 
The text encoding is UTF-8.

> tweetID [TAB] 0 [TAB] NormClaimID [TAB] label

Where: <br>
* tweetID: unique ID for a given tweet. Tweet details found in the queries file. <br/>
* 0: literally 0.
* NormClaimID: unique ID for a given NormClaim. NormClaim details found in the NormClaim file. <br/>
* label: 1 if the pair __tweetID__ and __NormClaimID__ make a pair such that the NormClaim corresponding to __NormClaimID__ proves the tweet corresponding to __tweetID__; 0 otherwise.

Example:

// TODO: Add example here

## __Results File Format__: 

For this task, the expected results file is a list of claims with the estimated score for check-worthiness. 
Each line contains a tab-separated line with:
>TweetID [TAB] 0 [TAB] NormClaimID [TAB] rank [TAB] score [TAB] tag

Where _TweetID_ is ID of the tweet given in the TweetInfo.queries file, _NormCLaimID_ is ID of the normalized claim found in NormClaims.docs, _score_ is the score given by your model for the pair _TweetID_, _NormCLaimID_ and _rank_ is the rank of the pair given the scores of all possible pairs for a given _TweerID_, and _tag_ is a string identifier used by participants.
 For example:
>1  0  1  1  0.9056  modelX <br/>
>1  0  2  2  0.6862  modelX <br/>
>2  0  1  2  0.1023  modelX <br/>
>2  0  2  1  0.235  modelX <br/>
> ...

Your result file **MUST contain at most 1,000 NormClaims per tweet** from the respective input file.
Otherwise the scorer will not score this result file.

## Format checkers

TBA

## Scorers 

TBA

### Evaluation metrics

For Task 3 (ranking): R-Precision, Average Precision, Reciprocal Rank, Precision@k and means of these over all verified claims.
**The official metric for task3, that will be used for the competition ranking is the Mean Average Precision (MAP)**

You can use these repos as reference for the evaluation, https://github.com/joaopalotti/trectools and https://github.com/usnistgov/trec_eval.

## Baselines

To launch the baseline script use the following:

> python3 baselines/baselines.py  <br/>

The [baselines](/baselines) module contains a random and a simple TfIDF baseline for the task.

If you execute baseline.py, both of the baselines will be trained on 80% of the pairs and will use the lrest 20% as dev dataset.
The performance of both baselines will be displayed.

## Licensing

  These datasets are free for general research use.

## Citation


## Credits

Task 3 Organizers:

* Nikolay <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/
**The official rules are published on the website, check them!**

Contact:   clef-factcheck@googlegroups.com

