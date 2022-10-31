from helper_funcs import get_classes_from_module
from food import Food


class MenuObject:
    """
    class for storing the menu. Aimed at easier scalability,
    you can create menus for different food modules.

    bound_text this is what will be written above and below
    when the menu is displayed.

    bound_width - menu width
    """

    def __init__(self,
                 menu_text: str,
                 menu_width: int,
                 module_name: str,
                 food_base_class):
        """
        initializes the menu with all food
        that are created as classes in this module.
        This is convenient because the end user
        does not need to think about whether
        there is a food type on the menu -
        as soon as the customer adds a new food
        with a new recipe here as a class - everything will already work.
        In addition to this it is a separate class
        that does not shit the module
        """
        self.bound_text = menu_text
        self.bound_width = menu_width
        self.list_menu: list = []
        for cls in get_classes_from_module(module_name):
            if cls not in [food_base_class, Food]:
                self.update(cls)

    def update(self, eat_cls) -> None:
        """
        adds an object to the menu,
        takes all the necessary data from the passed class,
        corresponding to the type of food
        """
        self.list_menu.append(eat_cls)

    def __str__(self) -> str:
        """
        method for printing menu
        """
        text = self.bound_text.center(self.bound_width, "-") + "\n"
        for pos in self.list_menu:
            addition = f"- {pos.to_str()}: " + ", ".join(pos.ingredients())
            addition = addition.ljust(self.bound_width)
            text += addition + "✅\n"
        return text + text[: self.bound_width]
