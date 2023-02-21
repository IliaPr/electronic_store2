from utils.main import Items
import pytest

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
