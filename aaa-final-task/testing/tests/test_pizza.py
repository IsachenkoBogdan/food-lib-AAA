from src import pizza
import pytest


def test_dict():
    assert pizza.Margherita(size='L').dict() == \
           {"tomato sauce": 100, "mozzarella": 200, "tomatoes": 100}
    assert pizza.Pepperoni(size='L').dict() == \
           {"tomato sauce": 100, "mozzarella": 100, "pepperoni": 100}
    assert pizza.Hawaiian(size='XL').dict() == \
           {
               "tomato sauce": 100,
               "mozzarella": 100,
               "chicken": 100,
               "pineapples": 100,
           }


def test_eq():
    assert pizza.Margherita(size='L') != pizza.Margherita(size='XL')
    assert pizza.Margherita(size='XL') != pizza.Pepperoni(size='XL')


def test_wrong_size():
    with pytest.raises(ValueError):
        pizza.Margherita(size='BIG VERY BIG')


def test_get_name():
    assert pizza.Margherita.get_name() == 'Margherita'


def test_to_str():
    assert pizza.Margherita.to_str() == "Margherita 🧀"
