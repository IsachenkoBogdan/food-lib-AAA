from abc import ABCMeta, abstractmethod
from time import sleep
from src.test_time_config import baking_time, delivery_time, waiting_time
from src.menu_class import MenuObject
from src.helper_funcs import Logging
from src.food import Food

loggers = {
    "bake": Logging("Your pizza is 🔥baked🔥 in {}s"),
    "delivery": Logging("Your pizza is 🏃delivered🏃 in {}s"),
    "pickup": Logging("Your 🍕pizza🍕 is served in {}s"),
}


# convenient way to use loggers for functions from the pizza module

class Pizza(Food, metaclass=ABCMeta):
    """
    abstract pizza class
    """

    sizes: list[str] = ["XL", "L"]

    def __init__(self, size: str):
        if size not in self.sizes:
            raise ValueError(f"There are no {size} size.")
            # raises error if somebody trying to
            # create pizza with not implemented size
        self.size = size

    @property
    @abstractmethod
    def recipes_dict(self) -> dict:
        pass

    @property
    @abstractmethod
    def icon(self) -> str:
        pass

    @abstractmethod
    def bake(self) -> None:
        """
        implements pizza baking logic
        """
        pass

    @staticmethod
    def deliver() -> None:
        """
        implements the logic of pizza delivery to the customer
        """
        # Some Delivering logic, emulating delivering time with sleep
        sleep(delivery_time)

    @staticmethod
    def pickup() -> None:
        """
        implements the pickup logic for the customer
        """
        # Some logic of pizza giving to customer
        sleep(waiting_time)

    def dict(self) -> dict:
        """
        returns the pizza recipe as a dictionary,
        where the keys are the ingredients
        and the values are the quantity in grams
        """
        return self.recipes_dict[self.size]

    def __eq__(self, other) -> bool:
        """
        method for comparing two pizzas
        """
        return self.dict() == other.dict()


class Margherita(Pizza):
    icon: str = "🧀"
    recipes_dict = {
        "XL": {"tomato sauce": 100, "mozzarella": 100, "tomatoes": 100},
        "L": {"tomato sauce": 100, "mozzarella": 200, "tomatoes": 100},
    }

    def bake(self) -> None:
        # Some logic for Margherita baking
        sleep(baking_time[self.get_name()][self.size])


class Pepperoni(Pizza):
    icon: str = "🍕"
    recipes_dict = {
        "XL": {"tomato sauce": 100, "mozzarella": 200, "pepperoni": 100},
        "L": {"tomato sauce": 100, "mozzarella": 100, "pepperoni": 100},
    }

    def bake(self) -> None:
        # Some logic for Pepperoni baking
        sleep(baking_time[self.get_name()][self.size])


class Hawaiian(Pizza):
    icon: str = "🍍"
    recipes_dict = {
        "XL": {
            "tomato sauce": 100,
            "mozzarella": 100,
            "chicken": 100,
            "pineapples": 100,
        },
        "L": {
            "tomato sauce": 100,
            "mozzarella": 50,
            "chicken": 100,
            "pineapples": 100,
        },
    }

    def bake(self) -> None:
        # Some logic for Hawaiian baking
        sleep(baking_time[self.get_name()][self.size])


menu = MenuObject(menu_text="PIZZA MENU",
                  menu_width=80,
                  module_name=__name__,
                  food_base_class=Pizza)
