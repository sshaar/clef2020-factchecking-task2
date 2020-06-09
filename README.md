# CLEF2020-CheckThat! Task 2: Verified Claim Retrieval

This repository contains the _data set_, _format checker, scorer and baselines_ for the [CLEF2020-CheckThat! task 2](https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval). <br>
The task, given an input claim and a set of already verified claims, consists in ranking the already verified claims such that the ones that verify the input claim, or a subclaim in it, are ranked on top. <br>
The goal of the task is to build a tool to support journalists fact-checkers when trying to determine whether a claim has been already fact-checked.
This task is part of the [CLEF2020-CheckThat!](https://sites.google.com/view/clef2020-checkthat/) lab. For more information about deadlines , updates and other related task visit the [site](https://sites.google.com/view/clef2020-checkthat/) of the lab.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Jun 8th, 2020 (Test Data Released)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 2 data set provided for the CLEF2020-CheckThat! Lab on "Automatic Identification and Verification of Claims".

The current version of the data is the release of the test data.

All changes and updates on these data sets and tools are reported in Section 1 of this document.

__Table of contents:__

- [CLEF2020-CheckThat! Task 2: Verified Claim Retrieval](#clef2020-checkthat-task-2-verified-claim-retrieval)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Contents of the Repository](#contents-of-the-repository)
  - [Data Format](#data-format)
    - [Already Verified Claims](#already-verified-claims)
    - [Queries file](#queries-file)
    - [Qrels file](#qrels-file)
    - [Results File](#results-file)
  - [Example Ranking](#example-ranking)
  - [Format checkers](#format-checkers)
  - [Evaluation metrics and Scorers](#evaluation-metrics-and-scorers)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)

## Evaluation Results

You can find the results in this spreadsheet, https://tinyurl.com/y9sjooxo.

## List of Versions

* __v1.0 [2020/03/20]__ - Version 1 of the training data: 626 Tweets and 518 already verified claims.
* __v2.0 [2020/03/29]__ - Version 2 of the training data: 1,003 Tweets and 784 already verified claims.
* __v3.0 [2020/05/11]__ - Version 3 of the training data: 1,003 Tweets and 10,373 already verified claims. Fixed some labels, in addition to extending the dataset.
* __Test [2020/05/26]__ - Release of [test input](test-input/tweets.queries.tsv): 200 Tweets to be matched against the 10,373 already verified claims released with version v.3.0 of the data.
* __v4.0 [2020/06/08]__ - Release the gold labels of test tweets.

## Contents of the Repository

We provide the following files:

* Test input folder: [test-input](test-input)
  * [Submission README](test-input/README.md)
  * [test-tweets](test-input/test-input.zip)
  * [test-gold](test-input/test-input.zip)
  * [Example submission scores](test-input/example-submission-scores.tsv)

* Main folder: [data](data)
  * Subfolder: [v2](data/v2.zip)
    * [verified_claims.docs.tsv](data/v2.zip) <br/>
    Contains all the verified claims used for fact checking released with the version 2.0 and 1.0.
    
    * Subfolder [/train](data/v2.zip) </br>
    Contains all training data released with the version 1.0 and 2.0
      * [tweets](data/v2.zip) </br>
        Contains information for training tweets (file format described in section [Queries file](#queries-file)).    
      * [tweet-vclaim-pairs.qrels](data/v2.zip) </br>
        Contains the correct pairing between the input tweet and verified claims (file format described in section [Qrels file](#qrels-file))
        
    * Subfolder [/dev](data/v2.zip) </br> 
    Contains dev data released with the version 2.0. Has the same structure as [/train](data/v2.zip).
      * [tweets](data/v1.zip)
      * [tweet-vclaim-pairs.qrels](data/v2.zip)
      
 * Subfolder: [v3](data/v3.zip)</br>
 Similar structure to subfolder [v2](data/v3.zip)
     
 * [README.md](README.md) <br/>
 this file


## Data Format

The format used in the task is inspired from [Text REtrieval Conference (TREC)](https://trec.nist.gov/)'s campaigns for information retrieval (a description of the TREC format can be found [here](https://github.com/joaopalotti/trectools#file-formats)).

The data sets are TAB separated csv files.
The text encoding for all files is UTF-8.

The data seta is separated into train and dev splits. They may be used as is or they can be combined and used with  cross-validation. It isentirely  upto the participants how the given train and dev data will be managed.

### Already Verified Claims

All the verified claims that will be used for both training and test are found in file (data/verified_claims.qrels.tsv).

The file has the following format:

> vclaim_id <TAB> vclaim <TAB> title

where <br>

* vclaim_id: unique ID of the verified claim <br/>
* vclaim: text of the verified claim <br/>
* title: title of the document fact checking the verified claim <br/>

Example:

| vclaim_id | vclaim | title |
| --- | --- | --- |
| 2 | "A ""law to separate families"" was enacted prior to April 2018, and the federal government is powerless not to enforce it." | Was the ‘Law to Separate Families’ Passed in 1997 or ‘by Democrats’? |
| 222 | Former U.S. Vice President Joe Biden owns the largest mansion in his state. | Does Joe Biden Own the Largest Mansion in His State? |
| 503 | "U.S. Sen. Bernie Sanders compared Baltimore to a ""third world country."""  | Did U.S. Sen. Bernie Sanders Say Baltimore Was Like a ‘Third World Country’? |
| ... |

__Note__: Not all verified claims in the file have a corresponding tweet.

### Queries file

TAB separated file with the input tweets.
A row of the file has the following format

> tweet_id <TAB> tweet_content

where: <br>

* tweet_id: unique ID for a given tweet <br/>
* tweet_content: text of the tweet <br/>

Example: <br/>
| tweet_id | tweet_content |
| --- | --- |
| 8 | im screaming. google featured a hoax article that claims Minecraft is being shut down in 2020 pic.twitter.com/ECRqyfc8mI — Makena Kelly (@kellymakena) January 2, 2020 |
| 335  | BREAKING: Footage in Honduras giving cash 2 women & children 2 join the caravan & storm the US border @ election time. Soros? US-backed NGOs? Time to investigate the source! pic.twitter.com/5pEByiGkkN — Rep. Matt Gaetz (@RepMattGaetz) October 17, 2018 |
| 622 | y’all really joked around so much that tide put their tide pods in plastic boxes…smh pic.twitter.com/Z44efALcX5 — ㅤnavid (@NavidHasan\_) January 13, 2018 |
|...

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
| tweet_id | 0 | vclaim_id | relevance |
|---|---|---|---|
| 422 | 0 | 92 | 1 |
| 538 | 0 | 454 | 1 |
| 221 | 0 | 12  | 1 |
| 137 | 0 | 504 | 1 |
|... |

### Results File

Each row of the result file is related to a pair _tweet_ and _verified_claim_ and intuitively indicates the ranking of the verified claim with respect to the input tweet.
Each row has the following format:
>tweet_id <TAB> 0 <TAB> vclaim_id <TAB> rank <TAB> score <TAB> tag

where <br>

* tweet_id: is ID of the tweet given in the tweet file
* Q0: is not a meaningful column (it is needed to comply with the TREC format).
* vclaim_id: is ID of the verified claim found in the verified claims file (data/verified_claims.qrels.tsv)
* rank: is the rank of the pair given based on the scores of all possible pairs for a given _tweet_id_. (Not taken into account when calculating metrics. Always equal to 1)
* score: is the score given by your model for the pair _tweet_id_ and _vclaim_id_
* tag: is a string identifier of the team.

 For example:
|tweet_id  |  Q0  |  vclaim_id  |  rank  |  score  | tag |
| --- | --- | --- | --- | --- | --- |
| 359 | Q0 | 303  | 1 | 1.1086285 | elastic |
| 476|Q0| 292|1|  4.680018|   elastic
| 35| Q0| 373|1|  5.631936|   elastic
| 474|Q0| 352|1|  0.8830346|  elastic
| 174|Q0| 408|1|  0.98045605| elastic
| ...

Your result file **MUST** have at most 1 unique pair of tweet_id and vclaim_id. You can skip pairs if you deem them not relevant.

## Example Ranking

The following is an example ranking of verified claims for given tweet.

Let's take random tweet from the data set:
> __tweet_id__:  251 <br>
> __tweet_content__: A big scandal at @ABC News. They got caught using really gruesome FAKE footage of the Turks bombing in Syria. A real disgrace. Tomorrow they will ask softball questions to Sleepy Joe Biden’s son, Hunter, like why did Ukraine & China pay you millions when you knew nothing? Payoff? — Donald J. Trump (@realDonaldTrump) October 15, 2019

Using the content of the tweet, your model should give the highest score to the veriefied claim, that matches the tweet in the [Qrels file](#qrels-file). In this case the verified claim is:

> __vclaim_id__: 115 <br>
> __vclaim__: ABC News mistakenly aired a video from a Kentucky gun range during its coverage of Turkey's attack on northern Syria in October 2019.

Example of top 5 ranked verfied claims from the baseline model in this repository:
| vclaim | score |
| --- | --- |
| ABC News mistakenly aired a video from a Kentucky gun range during its coverage of Turkey's attack on northern Syria in October 2019. | 21.218384 |
| In a speech to U.S. military personnel, President Trump said if soldiers were real patriots, they wouldn't take a pay raise. | 19.962847 |
| Former President Barack Obama tweeted: "Ask Ukraine if they found my birth certificate." | 19.414398 |
| Mark Twain said, "Do not fear the enemy, for your enemy can only take your life. It is far better that you fear the media, for they will steal your HONOR." | 16.810490 |
| Dolly Parton wrote "Jolene" and "I Will Always Love You" in one day.  | 16.005116 |

## Format checkers

The format checker verifies that the generated results file from your model complies with the expected format. To launch it run:

python3 lib/format_checker.py --model-prediction <path_to_your_results_file>

__Note__: The checker can't verify whether the prediction file you submit contain all lines/claims, because it does not have access to the corresponding gold file.

__Note__: The python files in this repo require a version of python that is at least 3.6.

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

> python3 evaluate.py -s \<results-file\> -g data/dev/tweet-vclaim-pairs.qrels <br/>

The [results file](#results-file) contains the predictions of the model.

__Note__: The metric _reciprocal_rank_ in the output of the evaluation script corresponds to Mean reciprocal rank.

## Baseline

To use the Elastic Search baseline you need to have a locally running Elastic Search instance.
You can follow [this](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html) article for Elastic Search installation. You can then run elasticsearch using the following command:
> /path/to/elasticsearch

Alternatively, if you have docker installed, you can run elasticsearch u:Wusing this command:
> docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.1

Once you have Elastic Search running you can run the baseline script using the following:

> python3 elastic_search_baseline.py --vclaims data/verified_claims.docs.tsv --tweets data/dev/tweets.queries.tsv --predict-file \<results-file\> <br/>

## Licensing

  These data sets are free for general research use.

## Credits

Task Organizers:

* Nikolay Babulkov, Sofia University <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/task-2-claim-retrieval

Contact:   clef-factcheck@googlegroups.com

