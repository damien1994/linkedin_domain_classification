import pytest
from domain_classification.utils import remove_accents, remove_company_name


def test_remove_accents():
    assert remove_accents('développeur react') == 'developpeur react'
    assert remove_accents('cuisinier à xxx') == 'cuisiner a xxx'


#def test_remove_company_name():
    #assert remove_company_name('developpeur chez ubisoft') == 'developpeur'
    #assert remove_company_name('cuisiner at Kebav') == 'cuisinier'

