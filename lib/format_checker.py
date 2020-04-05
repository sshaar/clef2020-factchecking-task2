import re
import argparse
from functools import partial

from lib.logger import logger

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
        for line_no, line_str in enumerate(tsvfile, start=1):
            line = line_str.split('\t')
            for check in LINE_CHECKS:
                error = check(line)
                if error is not None:
                    return f'{error} on line {line_no} in file: {preditions_file_path}'
    return 'Format is ok'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-prediction', '-m', required=True,
                        help='Path to the file containing the model predictions,\
                              which are supposed to be checked')
    parser.add_argument('--output', '-o', default=None,
                        help='Output file with errors from the prediction file.\
                             If not specified, prints output in stdout.')
    return parser.parse_args()

def main(args):
    errors = check_format(args.model_prediction)
    if args.output:
        # SAVE
        logger.info(f"Saved results to file: {args.output}")
    else:
        print(errors)

if __name__=='__main__':
    args = parse_args()
    main(args)
