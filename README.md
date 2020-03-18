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

- [CLEF2020-CheckThat! Task 2](#clef2020-checkthat-task-2)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Contents of the Distribution v1.0](#contents-of-the-distribution-v10)
  - [Data Format](#data-format)
    - [Facts:](#facts)
    - [Queries file:](#queries-file)
    - [Qrels file:](#qrels-file)
  - [__Results File Format__:](#results-file-format)
  - [Format checkers](#format-checkers)
  - [Scorers](#scorers)
    - [Evaluation metrics](#evaluation-metrics)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/03/?]__ - Training data. The training data for task 2 contains (626) Tweets and (518) NormClaims that represents the set of verified claims.

## Contents of the Distribution v1.0

We provide the following files:

* Main folder: [data](data)
  * [verified_facts.qrels.tsv](data/verified_facts.qrels.tsv) <br/>
  Contains all the verified claims used for fact checking released with the version 1.0
  * Subfolder [/train](data/train)
  Contains all training data released with the version 1.0
    * [tweets](data/train/tweets.queries.tsv)
      Contains information for training tweets.
    * [tweet-fact-pairs.qrels](data/train/tweet-fact-pairs.qrels)
     Contains the correct pairs between tweet and verified claims
  * [README.md](README.md) <br/>
    this file


## Data Format

The datasets are text files with the information TAB separated. The text encoding is UTF-8. You will get:

### Facts:

All the verified claims that will be used for both training and test are found in file (data/verified_facts.qrels.tsv). This file has information about the verified claims that are obtained from fact checking websites in the following format.

> fact_id <TAB> fact <TAB> title

Where: <br>

* fact_id: unique ID for a given NormClaim <br/>
* fact: text of the fact/verified claim <br/>
* title: title of the document fact checking the verified claim <br/>

Example:
>2       "A ""law to separate families"" was enacted prior to April 2018, and the federal government is powerless not to enforce it."       Was the ‘Law to Separate Families’ Passed in 1997 or ‘by Democrats’? <br/>
>222     Former U.S. Vice President Joe Biden owns the largest mansion in his state.     Does Joe Biden Own the Largest Mansion in His State? <br/>
>503     "U.S. Sen. Bernie Sanders compared Baltimore to a ""third world country."""     Did U.S. Sen. Bernie Sanders Say Baltimore Was Like a ‘Third World Country’?  <br/>
> .... <br/>

### Queries file:

Tweet details that are used for training or testing.
It is a text files with the information TAB separated.
The text encoding is UTF-8.

> tweet_id <TAB> tweet_conent

Where: <br>

* tweet_id: unique ID for a given tweet <br/>
* tweet_content: text of the tweet <br/>

Example: <br/>
>8       im screaming. google featured a hoax article that claims Minecraft is being shut down in 2020 pic.twitter.com/ECRqyfc8mI — Makena Kelly (@kellymakena) January 2, 2020 <br/>
>335     BREAKING: Footage in Honduras giving cash 2 women & children 2 join the caravan & storm the US border @ election time. Soros? US-backed NGOs? Time to investigate the source! pic.twitter.com/5pEByiGkkN — Rep. Matt Gaetz (@RepMattGaetz) October 17, 2018 <br/>
>622     y’all really joked around so much that tide put their tide pods in plastic boxes…smh pic.twitter.com/Z44efALcX5 — ㅤnavid (@NavidHasan\_) January 13, 2018 <br/>
>...


### Qrels file:

A file containing information about the pairs of tweet and verified claims;
such that the verified claim (__fact_id__) proves the tweet (__tweet_id__).
It is a text files with the information tab-separated.
The text encoding is UTF-8.

> tweet_id <TAB> 0 <TAB> fact_id <TAB> relevance


Where: <br/>

* tweet_id: unique ID for a given tweet. Tweet details found in the queries file. <br/>  
* 0: literally 0.
* fact_id: unique ID for a given NormClaim. NormClaim details found in the NormClaim file. <br/>
* relevance: 1 if the pair __tweet_id__ and __fact_id__ make a pair such that the fact corresponding to __fact_id__ proves the tweet corresponding to __tweet_id__; 0 otherwise. 

__Note__: The qrels file needs to contains only examples with relevance = 1. It assumes 0 for all others.

Example:

>422     0       92      1 <br/>
>538     0       454     1 <br/>
>221     0       12      1 <br/>
>137     0       504     1 <br/>
>...

## __Results File Format__:

For this task, the expected results file is a list of claims with the estimated score for check-worthiness.
Each line contains a tab-separated line with:
>tweet_id <TAB> 0 <TAB> fact_id <TAB> rank <TAB> score <TAB> tag

Where: <br>
* TweetID: is ID of the tweet given in the tweet file
* 0: literaly 0.
* fact_id: is ID of the normalized claim found in NormClaims.docs
* score: is the score given by your model for the pair _tweet_id_ and _fact_id_ 
* rank: is the rank of the pair given based on the scores of all possible pairs for a given _tweet_id_
* tag: is a string identifier used by participants.

 For example:
>359     Q0      303     1       1.1086285       elasic <br/>
>476     Q0      292     1       4.680018        elasic <br/>
>35      Q0      373     1       5.631936        elasic <br/>
>474     Q0      352     1       0.8830346       elasic <br/>
>174     Q0      408     1       0.98045605      elasic <br/>
>...

Your result file **MUST contain at most 1,000 NormClaims per tweet** from the respective input file.
Otherwise the scorer will not score this result file.

## Format checkers

TBA

## Scorers

[evaluate.py](/evaluate.py) - Returns the metrics needed for evaluation
Example for using the evaluation script:

> python3 evaluate.py -s \<prediction-scores-file\> -g data/train/tweet-fact-pairs.qrels <br/>

### Evaluation metrics

For Task 2 (ranking): R-Precision, Average Precision, Reciprocal Rank, Precision@k and means of these over all verified claims.
**The official metric for task2, that will be used for the competition ranking is the Mean Average Precision (MAP)**

You can use these repos as reference for the evaluation, https://github.com/joaopalotti/trectools and https://github.com/usnistgov/trec_eval.

## Baseline

To use the Elastic Search baseline you need to have a locally running Elastic Search instance.
You can follow [this](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html) article for Elastic Search installation. You can then run elasticsearch using the following command:
> /path/to/elasticsearch

Alternatively, if you have docker installed, you can run elasticsearch using this command:
> docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.1

Once you have Elastic Search running you can run the baseline script using the following:

> python3 elastic_search_baseline.py --facts data/verified_facts.docs.tsv --tweets data/train/tweets.queries.tsv --predict-file <prediction-scores-file> <br/>

## Licensing

  These datasets are free for general research use.

## Credits

Task 2 Organizers:

* Nikolay Babulkov, Sofia University <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval

Contact:   clef-factcheck@googlegroups.com

