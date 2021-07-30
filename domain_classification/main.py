"""
Main file
"""

import os
import sys
import pandas as pd

from domain_classification.config import BASIC_TECH_VOCABULARY, CURRENT_DIR, STUDENTS_VOC
from domain_classification.utils import parse_args, remove_accents, remove_company_name
from domain_classification.TextPreparation import TextPreparation
from domain_classification.TextClassification import TextClassification
from domain_classification.TextEvaluation import ClassificationPerformance


def main(input_file, output_path):
    # load job title file
    df_job_title = pd.read_csv(input_file)
    original_job_title = df_job_title['Titre']

    # load complementary tech vocabulary to improve our dictionary maturity
    # this file has been created by scrapping bluecoders website

    df_voc_tech = pd.read_csv(os.path.join(CURRENT_DIR, 'data/scrap_tech_voc.csv'),
                              delimiter=';')

    # construct our full tech glossary
    tech_vocabulary_completed = BASIC_TECH_VOCABULARY.union(set(df_voc_tech.technos_name))
    del df_voc_tech

    # define exact matching pattern to avoid cases like:
    # technicien -> defined like Tech because you can find 'tech' in 'technicien'
    glossary_tech = {r"\b" + word + r"\b" for word in tech_vocabulary_completed}

    # text data preparation
    textprep = TextPreparation(df_job_title, 'Titre')
    df_job_title['Titre'] = textprep.text_preparation()

    # text classification
    text_classification = TextClassification(df_job_title, 'Titre')
    predictions = text_classification.job_classification(STUDENTS_VOC, glossary_tech)

    # logic rule performance evaluation
    test_data_path = os.path.join(CURRENT_DIR, 'data/test.csv')
    evaluation = ClassificationPerformance(test_data_path)
    evaluation.evaluate_logic_rule(STUDENTS_VOC, glossary_tech)

    return pd.concat([original_job_title, pd.Series(predictions, name='predictions')], axis=1).\
        to_csv(output_path, index=False)


if __name__ == '__main__':
    # get everything after the script name
    ARGS = parse_args(args=sys.argv[1:])
    INPUT_FILE = ARGS.input_file
    OUTPUT_FILENAME = ARGS.output_filename
    OUTPUT_DIR = 'results'

    OUTPUT_PATH = os.path.join(CURRENT_DIR, OUTPUT_DIR, OUTPUT_FILENAME)
    main(INPUT_FILE, OUTPUT_PATH)
