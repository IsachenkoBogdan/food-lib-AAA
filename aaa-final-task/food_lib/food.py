from abc import ABCMeta, abstractmethod


class Food(metaclass=ABCMeta):
    @property
    @abstractmethod
    def recipes_dict(self) -> dict[str, dict[str, int]]:
        """
        returns a dictionary from ingredients to recipe quantities with sizes
        it is abstract, because we want to prohibit to make classes of food
        without recipe
        """
        return {'l': {'cheese': 100}, 'xl': {'cheese': 200}}

    @property
    @abstractmethod
    def icon(self) -> str:
        """
        food icon in cli
        """
        return "smile"

    @classmethod
    def get_name(cls) -> str:
        """
        returns the name of the food type that the class corresponds to.
        uses for simplifications, in general, one could do without it,
        but this method can be useful when using the module
        """
        return cls.__name__

    @classmethod
    def to_str(cls) -> str:
        return f"{cls.get_name()} {cls.icon}"

    @classmethod
    def ingredients(cls) -> list:
        """
        returns a list of ingredients in a recipe
        """
        return list(list(cls.recipes_dict.values())[0].keys())

    def __str__(self):
        return self.to_str()
