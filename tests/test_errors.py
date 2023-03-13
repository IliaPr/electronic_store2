from utils import InstantiateError
from utils.main import Items
import pytest
import os

def test_file_no_found():
    with pytest.raises(FileNotFoundError):
        Items.instantiate_from_csv('data.csv')

def test_file_is_damaged():
    with pytest.raises(InstantiateError.InstantiateCSVError):
        Items.instantiate_from_csv(Items.instantiate_from_csv(os.path.join('utils', 'items2.csv')))