# This file defines the food items, prices, descriptions, and menu display.


from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class MenuItem:
    item_id: int
    name: str
    description: str
    price: Decimal


MENU_ITEMS = [
    MenuItem(
        1, "Classic Burger",
        "Beef patty, lettuce, tomato, and sauce",
        Decimal("8.50")
    ),
    MenuItem(
        2, "Cheeseburger",
        "Beef patty, cheddar cheese, and sauce",
        Decimal("9.50")
    ),
    MenuItem(
        3, "Margherita Pizza",
        "Tomato sauce, mozzarella, and basil",
        Decimal("12.00")
    ),
    MenuItem(
        4, "Chicken Wrap",
        "Grilled chicken, lettuce, and dressing",
        Decimal("7.75")
    ),
    MenuItem(
        5, "French Fries",
        "Crispy golden fries",
        Decimal("3.50")
    ),
    MenuItem(
        6, "Soft Drink",
        "Chilled soft drink",
        Decimal("2.00")
    ),
]

def get_menu_item(item_id):
    """Return a menu item by ID, or None if it does not exist."""
    for item in MENU_ITEMS:
        if item.item_id == item_id:
            return item

    return None
