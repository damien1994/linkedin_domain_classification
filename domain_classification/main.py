"""
Main file
"""

import os
import sys
import pandas as pd
import numpy as np

from domain_classification.config import BASIC_TECH_VOCABULARY, CURRENT_DIR
from domain_classification.utils import parse_args, remove_accents, remove_company_name


def main(input_file):
    # load job title file
    df_job_title = pd.read_csv(input_file)

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

    # some data preparation
    # lowercase
    df_job_title['Titre'] = df_job_title['Titre'].str.lower()
    # remove accents
    df_job_title['Titre'] = df_job_title['Titre'].apply(remove_accents)
    # remove company name
    df_job_title['Titre'] = remove_company_name(df_job_title, 'Titre', 'chez | at')

    # job title Tech / Non Tech classification
    df_job_title['label'] = np.where(df_job_title['Titre'].str.findall(r"|".join(glossary_tech)),
                                     True,
                                     False)

    return df_job_title.to_csv(os.path.join(CURRENT_DIR,
                                            'results/job_title_classification.csv'))


if __name__ == '__main__':
    # get everything after the script name
    ARGS = parse_args(args=sys.argv[1:])
    INPUT_FILE = ARGS.input_file
    main(INPUT_FILE)
