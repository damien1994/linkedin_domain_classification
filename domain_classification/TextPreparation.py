import re
import pandas as pd
from domain_classification.utils import remove_accents


class TextPreparation:

    def __init__(self, df, col):
        self.df = df
        self.col = col

    def text_preparation(self):
        self.df[self.col] = self.lowercase(self.df, self.col)
        self.df[self.col] = self._apply_remove_accents(self.df, self.col)
        return self.remove_company_name(self.df, self.col, 'chez | at')

    @staticmethod
    def remove_company_name(dataframe: pd.DataFrame, col: str, pattern: str) -> pd.Series:
        """
        Remove company name in pandas dataframe rows for a specific column
        :param dataframe: A dataframe
        :param col: col in dataframe to transform
        :param pattern: pattern to identify company names in sentences
        :return a pandas series with company name removed
        """
        return dataframe[col].apply(lambda x: re.split(pattern, x)[0])

    @staticmethod
    def _apply_remove_accents(dataframe: pd.DataFrame, col: str):
        """
        TO DO
        """
        return dataframe[col].apply(remove_accents)

    @staticmethod
    def lowercase(dataframe: pd.DataFrame, col: str):
        """
        TO DO
        """
        return dataframe[col].str.lower()
