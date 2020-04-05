import unittest
import os
from lib.format_checker import check_format

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

class TestFormatChecker(unittest.TestCase):
    def test_file_not_exist(self):
        test_file = os.path.join(TEST_DIR, 'non_existant_file')
        with self.assertRaises(FileNotFoundError):
            check_format(test_file)

    def test_less_columns(self):
        test_file = os.path.join(TEST_DIR, 'data/less_columns.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"Less columns than expected on line 3 in file: {test_file}")

    def test_more_columns(self):
        test_file = os.path.join(TEST_DIR, 'data/more_columns.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"More columns than expected on line 3 in file: {test_file}")

    def test_delimiter_error(self):
        test_file = os.path.join(TEST_DIR, 'data/delimiter_space.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"Wrong column delimiter on line 1 in file: {test_file}")

    def test_format_q0(self):
        test_file = os.path.join(TEST_DIR, 'data/format_q0.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"Wrong Q0 on line 3 in file: {test_file}")

    def test_rank_not_1(self):
        test_file = os.path.join(TEST_DIR, 'data/rank_not_1.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"Rank is different than 1 on line 3 in file: {test_file}")

    def test_duplicate_pairs(self):
        test_file = os.path.join(TEST_DIR, 'data/duplicate_pairs.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"Duplicate pair of tweet_id and vclaim_id on line 3 in file: {test_file}")

    def test_score_not_float(self):
        test_file = os.path.join(TEST_DIR, 'data/score_not_float.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, f"The score is not a float on line 3 in file: {test_file}")

    def test_format_ok(self):
        test_file = os.path.join(TEST_DIR, 'data/ok.tsv')
        errors = check_format(test_file)
        self.assertEqual(errors, "Format is ok")

if __name__ == '__main__':
    unittest.main()
