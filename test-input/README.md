# Submission info

## Test input

This directory contains a [test input file](./tweets.queries.tsv) with 200 tweets that will be used to test your model. The format of the file is the same as in the training set. It is further explained in the [Queries file subsection](https://github.com/sshaar/clef2020-factchecking-task2#queries-file) of the main readme.

Example for tweets [test input file](./tweets.queries.tsv):

>   tweet_content <br>
> 999     Republicans in Illinois don't want the child of a single mother to get a birth certificate. Unbelievable. https://t.co/yoEOL6vXBm — Paul Wilczynski (@PaulWilczynski) February 25, 2016 <br>
> 1000    Illinois GOP bill attacks single moms: No birth certificate or financial aid without the father https://t.co/wDGczl94dF — Morgan Fairchild (@morgfair) February 25, 2016 <br>
> 1001    michael savage who has more viewers then all media alt left,is fired because he mentions hillary clintons health.1st amendments dead,rise up — HKTK Planet (@HKTKplanet) September 28, 2016 <br>


## Submission file format

Using each of the tweets in the [test input file](./tweets.queries.tsv) and each of the verified claims (verified_claims.docs.tsv) in [v3.zip](https://github.com/sshaar/clef2020-factchecking-task2/blob/master/data/v3.zip), your model should give a score for each verified claim such that if we sort the verified claims by that score in descending order, the claims that can help verify the input claim, or a sub-claim in it, would be ranked above any claim that is not helpful to verify the input claim.

The format of the file with the score predictions is explained in the main README in the section [Results File](https://github.com/sshaar/clef2020-factchecking-task2#results-file). [This](./example-submission-scores.tsv) is a example submisson of a score file.

Example: 
> 999     Q0      6094    1       36.343285       elastic <br>
> 999     Q0      3773    1       17.714718       elastic <br>
> 999     Q0      5927    1       15.874663       elastic <br>
> 999     Q0      6096    1       15.258568       elastic <br>
> ...

NOTE: The order in which you output your predictions is irrelevant as these would be sorted by the scorer by your predicted score.

The scores in the example submission were generated using the baseline given in the [baseline script](../elastic_search_baseline.py).

We have implemented [format checker](../lib/format_checker.py), but it is still the responsibility of the participants to double-check that their submissions are correct.

You should submit the output TSV file via the [submission link](https://docs.google.com/forms/d/e/1FAIpQLSfsBfruzsYLg9mngQmLkKjBeyazxeAD-uknonXqJhVoozsKDg/viewform).

You have to submit **ONE** primary submission, and optionally you could submit up to **TWO** contrastive runns. 

If you make multiple primary/contrastive 1/contrastive 2 submissions, only the latest ones will be considered.

The official ranking will be based on the primary submission.

As a reminder, the participants can submit predictions more than once, but only the last one before the deadline 
**(5 June 2020)** will be evaluated and considered as official. 
