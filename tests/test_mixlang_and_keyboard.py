import pytest
from utils.keyboard import Keyboard

def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'

def test_mixlang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'
    with pytest.raises(AttributeError):
        kb.language = "CH"
