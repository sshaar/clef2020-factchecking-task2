# CLEF2020-CheckThat! Task 2: Verified Claim Retrieval

This repository contains the _dataset_, _format checker, scorer and baselines_ for the [CLEF2020-CheckThat! task 2](https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval). <br>
The task, given an input claim and a set of already verified claims, consists in ranking the already verified claims such that the ones that verify the input claim, or a subclaim in it, are ranked on top. <br>
The goal of the task is to build a tool to support journalists fact-checkers when trying to determine whether a claim has been already fact-checked.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 1.0: March 20th, 2020 (Training set batch 1 and Baseline Released)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 2 dataset provided for the CLEF2020-CheckThat! Lab on "Automatic Identification and Verification of Claims".
The current version of the data (1.0, March 20th, 2020) corresponds to the release of a first batch of the training data set.
The test set will be released on May 1st, 2020.

All changes and updates on these data sets and tools are reported in Section 1 of this document.

__Table of contents:__

- [CLEF2020-CheckThat! Task 2](#clef2020-checkthat-task-2)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Contents of the Repository](#contents-of-the-repository)
  - [Data Format](#data-format)
    - [Already Verified Claims:](#already-verified-claims)
    - [Queries file](#queries-file)
    - [Qrels file](#qrels-file)
    - [Results File](#results-file)
  - [Format checkers](#format-checkers)
  - [Evaluation metrics and Scorers](#evaluation-metrics-and-scorers)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/03/20]__ - Batch 1 of the training data: 626 Tweets and 518 already verified claims.

## Contents of the Repository

We provide the following files:

* Main folder: [data](data)
  * [verified_claims.docs.tsv](data/verified_claims.docs.tsv) <br/>
  Contains all the verified claims used for fact checking released with the version 1.0
  * Subfolder [/train](data/train)
  Contains all training data released with the version 1.0
    * [tweets](data/train/tweets.queries.tsv)
      Contains information for training tweets (file format described in section [Queries file](#queries-file)).
    * [tweet-vclaim-pairs.qrels](data/train/tweet-vclaim-pairs.qrels)
     Contains the correct pairing between the input tweet and verified claims (file format described in section [Qrels file](#qrels-file))
  * [README.md](README.md) <br/>
    this file


## Data Format

The format used in the task is inspired from [Text REtrieval Conference (TREC)](https://trec.nist.gov/)'s campaigns for information retrieval (a description of the TREC format can be found [here](https://github.com/joaopalotti/trectools#file-formats)).

The datasets are TAB separated csv files.
The text encoding for all files is UTF-8.

### Already Verified Claims

All the verified claims that will be used for both training and test are found in file (data/verified_claims.qrels.tsv).
The file has the following format:

> vclaim_id <TAB> vclaim <TAB> title <TAB> body

where <br>

* vclaim_id: unique ID of the verified claim <br/>
* vclaim: text of the verified claim <br/>
* title: title of the document fact checking the verified claim <br/>
* body: content of the document fact checking the verified claim <br/>

Example:
>2       "A ""law to separate families"" was enacted prior to April 2018, and the federal government is powerless not to enforce it."       Was the ‘Law to Separate Families’ Passed in 1997 or ‘by Democrats’? "TEXT OF DOCUMENT..." <br/>
>222     Former U.S. Vice President Joe Biden owns the largest mansion in his state.     Does Joe Biden Own the Largest Mansion in His State? "TEXT OF DOCUMENT..." <br/>
>503     "U.S. Sen. Bernie Sanders compared Baltimore to a ""third world country."""     Did U.S. Sen. Bernie Sanders Say Baltimore Was Like a ‘Third World Country’? "TEXT OF DOCUMENT..." <br/>
> .... <br/>

### Queries file

TAB separated file with the input tweets. 
A row of the file has the following format

> tweet_id <TAB> tweet_content

where: <br>

* tweet_id: unique ID for a given tweet <br/>
* tweet_content: text of the tweet <br/>

Example: <br/>
>8       im screaming. google featured a hoax article that claims Minecraft is being shut down in 2020 pic.twitter.com/ECRqyfc8mI — Makena Kelly (@kellymakena) January 2, 2020 <br/>
>335     BREAKING: Footage in Honduras giving cash 2 women & children 2 join the caravan & storm the US border @ election time. Soros? US-backed NGOs? Time to investigate the source! pic.twitter.com/5pEByiGkkN — Rep. Matt Gaetz (@RepMattGaetz) October 17, 2018 <br/>
>622     y’all really joked around so much that tide put their tide pods in plastic boxes…smh pic.twitter.com/Z44efALcX5 — ㅤnavid (@NavidHasan\_) January 13, 2018 <br/>
>...

__Note__: tweet_id doesn't corresponds to the id the tweet has on the Twitter platform.


### Qrels file

A TAB-separated file containing all the pairs of tweet and verified claims such that the verified claim (__vclaim_id__) proves the tweet (__tweet_id__).

> tweet_id <TAB> 0 <TAB> vclaim_id <TAB> relevance

where: <br/>

* tweet_id: unique ID for a given tweet. Tweet details found in the queries file. <br/>
* 0: literally 0 (this column is needed to comply with the TREC format).
* vclaim_id: unique ID for a given verified claim. Details on the verified claim are in file data/verified_claims.qrels.tsv <br/>
* relevance: 1 if the verified claim whose id is __vclaim_id__ proves the tweet with id __tweet_id__; 0 otherwise.

__Note__: In the qrels file only pairs with relevance = 1 are reported. Relevance = 0 is assumed for all pairs not appearing in the qrels file.

Example:

>422     0       92      1 <br/>
>538     0       454     1 <br/>
>221     0       12      1 <br/>
>137     0       504     1 <br/>
>...

### Results File

Each row of the result file is related to a pair _tweet_ and _verified_claim_ and intuitively indicates the ranking of the verified claim with respect to the input tweet. 
Each row has the following format:
>tweet_id <TAB> 0 <TAB> vclaim_id <TAB> rank <TAB> score <TAB> tag

where <br>

* tweet_id: ID of the tweet as given in the tweet file
* 0: literally 0 (this column is needed to comply with the TREC format).
* vclaim_id: ID of the verified claim as given in the verified claims file (data/verified_claims.qrels.tsv)
* rank: rank of this verified claim with respect to all other verified claims for the given _tweet_id_
* score: is the score given by your model for the pair _tweet_id_ and _vclaim_id_
* tag: is a string identifier of the team.

 For example:
>359     Q0      303     1       1.1086285       elastic <br/>
>476     Q0      292     1       4.680018        elastic <br/>
>35      Q0      373     1       5.631936        elastic <br/>
>474     Q0      352     1       0.8830346       elastic <br/>
>174     Q0      408     1       0.98045605      elastic <br/>
>...

Your result file **MUST have at most 1,000 rows (each one referring to one verified claim) per input tweet**.
Otherwise the scorer will not score this result file.

## Format checkers

TBA

## Evaluation metrics and Scorers

**The official metric for the task is Mean Average Precision (MAP), more specifically MAP@5.**
The scorer reports also R-Precision, Average Precision, Reciprocal Rank, Precision@k and means of these over all verified claims.

You can use these repos as reference for the evaluation, https://github.com/joaopalotti/trectools and https://github.com/usnistgov/trec_eval.

Before using the scorers or running the baseline, make sure you have all python packages in requirements.txt installed.
If you have [pipenv](https://github.com/pypa/pipenv) installed, one way to do it is by using the following command:
> pipenv install -r requirements.txt --skip-lock <br>
> pipenv shell

The scripts [evaluate.py](/evaluate.py) evaluates a submission. 
Example:

> python3 evaluate.py -s \<prediction-scores-file\> -g data/train/tweet-vclaim-pairs.qrels <br/>

## Baseline

To use the Elastic Search baseline you need to have a locally running Elastic Search instance.
You can follow [this](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html) article for Elastic Search installation. You can then run elasticsearch using the following command:
> /path/to/elasticsearch

Alternatively, if you have docker installed, you can run elasticsearch using this command:
> docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.1

Once you have Elastic Search running you can run the baseline script using the following:

> python3 elastic_search_baseline.py --vclaims data/verified_claims.docs.tsv --tweets data/train/tweets.queries.tsv --predict-file <prediction-scores-file> <br/>

## Licensing

  These datasets are free for general research use.

## Credits

Task Organizers:

* Nikolay Babulkov, Sofia University <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval

Contact:   clef-factcheck@googlegroups.com

