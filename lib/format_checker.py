import re
import argparse
from functools import partial
from color import bcolors

COLUMNS = ['qid', 'Q0', 'docno', 'rank', 'score', 'tag']

is_float = partial(re.match, r'^-?\d+(?:\.\d+)?$')

LINE_CHECKS = [
    lambda line: 'Wrong column delimiter' if len(line) == 1 else None,
    lambda line: 'Less columns than expected' if len(line) < len(COLUMNS) else None,
    lambda line: 'More columns than expected' if len(line) > len(COLUMNS) else None,
    lambda line: 'Wrong Q0' if line[COLUMNS.index('Q0')] != 'Q0' else None,
    lambda line: 'Rank is different than 1' if line[COLUMNS.index('rank')] != '1' else None,
    lambda line: 'The score is not a float' if not is_float(line[COLUMNS.index('score')]) else None,
]

def check_format(preditions_file_path):
    with open(preditions_file_path) as tsvfile:
        pair_ids = {}
        for line_no, line_str in enumerate(tsvfile, start=1):
            line = line_str.split('\t')
            for check in LINE_CHECKS:
                error = check(line)
                if error is not None:
                    return f'{error} on line {line_no} in file: {preditions_file_path}'

            tweet_id, vclaim_id = line[COLUMNS.index('qid')], line[COLUMNS.index('docno')]
            duplication = pair_ids.get((tweet_id, vclaim_id), False)
            if duplication:
                return f'Duplication of pair(tweet_id={tweet_id}, vclaim_id={vclaim_id}) ' \
                    f'on lines {duplication} and {line_no} in file: {preditions_file_path}'
            else:
                pair_ids[(tweet_id, vclaim_id)] = line_no
    return

def run_checks(prediction_file):
    error = check_format(prediction_file)
    if error:
        print(f"Format check: {bcolors.FAIL}Failed{bcolors.ENDC}")
        print(f"Cause: {bcolors.BOLD}{error}{bcolors.ENDC}")
        return False
    else:
        print(f"Format check: {bcolors.OKGREEN}Passed{bcolors.ENDC}")
        return True

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-prediction', '-m', required=True,
                        help='Path to the file containing the model predictions,\
                              which are supposed to be checked')
    return parser.parse_args()

if __name__=='__main__':
    args = parse_args()
    run_checks(args.model_prediction)
