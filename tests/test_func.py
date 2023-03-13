from utils.main import Items
import pytest
import os

def test_total_price():
    item1 = Items('Компьютер', 10000, 3)
    assert item1.total_price() == 30000

def test_total_price_2():
    item2 = Items('Phone', 'Phone', 'Phone')
    with pytest.raises(TypeError):
        item2.total_price()

def test_new_price():
    item3 = Items('Смартфон', 10000, 4)
    assert item3.new_price() == 8500

def test_new_price2():
    item4 = Items('Phone', 'Phone', 9)
    with pytest.raises(TypeError):
        item4.new_price()

def test_name_setter():
    item5 = Items('СуперСмартфон', 10000, 2)
    with pytest.raises(Exception):
        item5.name()

def test_is_integer():
    x = 5.0
    y = 4.7
    assert Items.is_integer(x) == True
    assert Items.is_integer(y) == False


def test_repr():
    item1 = Items("Смартфон", 10000, 20)
    assert item1.__repr__() == 'Item("Смартфон", 10000, 20)'

def test_str():
    item1 = Items("Смартфон", 10000, 20)
    assert item1.__str__() == "Смартфон"
