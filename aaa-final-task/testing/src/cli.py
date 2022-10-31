import click
from src import pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', '-d', default=False, is_flag=True)
@click.option(
    '--size',
    '-s',
    required=True,
    type=click.Choice(pizza.Pizza.sizes, case_sensitive=False),
)
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool, size: str) -> None:
    """prepares and delivers pizza"""
    pizza_name = pizza_name.title()
    try:
        pizza_cls = getattr(pizza, pizza_name)
        if pizza_cls not in pizza.menu.list_menu:
            # raises if this attribute exists in pizza module
            # ,but it is __name__ or something like that, not real food
            raise ValueError(f'There are no {pizza_name} in our menu')
        pizza_obj = pizza_cls(size)
    except AttributeError:
        # raises if there are no such attribute in pizza module
        raise ValueError(f'There are no {pizza_name} in our menu')

    print(f'Your order is {pizza_obj} with size {size}')
    pizza.loggers['bake'](pizza_obj.bake)()  # baking pizza with log
    if delivery:
        pizza.loggers['delivery'](pizza_obj.deliver)()  # log-delivers pizza
    else:
        pizza.loggers['pickup'](pizza_obj.pickup)()  # pickup pizza with log


@cli.command()
def menu() -> None:
    """displays a menu"""
    print(pizza.menu)


if __name__ == "__main__":
    cli()