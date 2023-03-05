import pytest

from utils.main import Phone, Items

item1 = Phone('iPhone 13', 60000, 4, 2)
item2 = Items("Смартфон", 45000, 33)
def test_add():
    assert item1 + item2 == 37

def test_num_sims():
    assert item1.num_sims == 2

def test_quantity_sim():
    with pytest.raises(ValueError):
        p = Phone('Samsung Galaxy S21', 799, 5, -1)
