from src import cli
from click.testing import CliRunner
import pytest

runner = CliRunner()


@pytest.mark.parametrize(
    'args, result',
    [(['pepperoni', '-s', 'l'],
      'Your order is Pepperoni 🍕 with size L\n'
      'Your pizza is 🔥baked🔥 in 0s\n'
      'Your 🍕pizza🍕 is served in 0s\n'),
     (['pepperoni', '-d', '-s', 'l'],
      'Your order is Pepperoni 🍕 with size L\n'
      'Your pizza is 🔥baked🔥 in 0s\n'
      'Your pizza is 🏃delivered🏃 in 0s\n')]
)
def test_order_with_pepperoni(args: list, result: str):
    real_result = runner.invoke(cli.order, args)
    assert real_result.output == result


@pytest.mark.parametrize(
    'args',
    [['pizza', '-s', 'l'],
     ['water', '-s', 'l']]
)
def test_order_raises_error(args: list):
    result = runner.invoke(cli.order, args)
    assert result.exc_info[0] is ValueError


def test_menu():
    real_result = runner.invoke(cli.menu)
    with open('tests/menu_result.txt', 'r') as f:
        assert real_result.output == f.read()

# python -m pytest cli
