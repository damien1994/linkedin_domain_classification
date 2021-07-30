import numpy as np
import pandas as pd


class TextClassification:

    def __init__(self, df, col):
        self.df = df
        self.col = col

    def job_classification(self, students_voc, tech_voc):
        rules = self.make_logic_rule(students_voc, tech_voc)
        return np.select(rules.values(), rules.keys(), default='False')

    def make_logic_rule(self, students_voc, tech_voc):
        return {
            'Not defined': (self._student_logic_rule(self.df, self.col, students_voc)) |
                           (self._null_logic_rule(self.df, self.col)),
            'True': self._tech_logic_rule(self.df, self.col, tech_voc)
        }

    @staticmethod
    def _tech_logic_rule(df, feature, tech_vocabulary):
        return pd.Series(len(x) != 0 for x in df[feature].str.findall(r"|".join(tech_vocabulary)))

    @staticmethod
    def _student_logic_rule(df, feature, student_vocabulary):
        return df[feature].str.contains('|'.join(student_vocabulary))

    @staticmethod
    def _null_logic_rule(df, feature):
        return df[feature].isnull()
