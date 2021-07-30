import pandas as pd
import pytest
from domain_classification.utils import remove_accents
from domain_classification.TextPreparation import TextPreparation


def test_remove_accents():
    assert remove_accents('développeur react') == 'developpeur react'
    assert remove_accents('cuisinier à xxx') == 'cuisinier a xxx'

'''
def test_text_preparation():
    input_data = {
        'Text': [
            'Ingénieur systèmes et réseaux',
            'Ingénieur système chez BRGM'
        ]
    }
    result_data = [
            'ingenieur systemes et reseaux',
            'ingenieur systeme'
        ]
    textprep = TextPreparation(pd.DataFrame(input_data), 'Text')
    assert all(textprep.text_preparation() == pd.Series(result_data, name='Text'))
'''


