import os
import pandas as pd
import logging as lg

from domain_classification.config import CURRENT_DIR
from domain_classification.TextClassification import TextClassification

lg.basicConfig(level=lg.INFO)


class ClassificationPerformance:

    def __init__(self, path_test_data):
        self.path_test_data = path_test_data

    def load_test_data(self):
        return pd.read_csv(self.path_test_data)

    def evaluate_logic_rule(self, students_voc, tech_voc):
        df_test = self.load_test_data()
        job_tech_classification = TextClassification(df_test, 'Titre')
        predictions = job_tech_classification.job_classification(students_voc, tech_voc)
        test = pd.concat([df_test, pd.Series(predictions, name='predictions')], axis=1)
        good_predictions = test[(test['predictions']) == (test['labels'])].shape[0]
        lg.info(f'Accuracy of the logic rule on quite balanced is {good_predictions / test.shape[0]}')
        return test.to_csv(os.path.join(CURRENT_DIR, 'results/evaluation_rule_based.csv'), index=False)
