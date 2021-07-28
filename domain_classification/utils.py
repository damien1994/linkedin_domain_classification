"""
File that contains functions to use in job titles classification
"""

import argparse

import re
import pandas as pd
import unidecode


def create_parser():
    """
    Parser
    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_file',
        help='csv file to process',
        required=True
    )
    return parser


def parse_args(args):
    """
    Parse arguments
    :param args: raw args
    :return: Parsed arguments
    """
    parser = create_parser()
    return parser.parse_args(args=args)


def remove_accents(input_str: str) -> str:
    """
    Remove accent from string
    :param input_str: a sentence - in our case, a job title
    :return: a string without accents
    """
    return unidecode.unidecode(str(input_str))


def remove_company_name(dataframe: pd.DataFrame, col: str, pattern: str) -> pd.Series:
    """
    Remove company name in pandas dataframe rows for a specific column
    :param dataframe: A dataframe
    :param col: col in dataframe to transform
    :param pattern: pattern to identify company names in sentences
    :return a pandas series with company name removed
    """
    return dataframe[col].apply(lambda x: re.split(pattern, x)[0])
