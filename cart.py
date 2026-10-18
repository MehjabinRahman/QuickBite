# This module handles adding products, updating quantities, removing products, and calculating totals.


from decimal import Decimal

class Cart:
    def __init__(self):
        # Each dictionary entry maps a menu item ID to its quantity.
        self._items = {}

    def add_item(self, menu_item, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        item_id = menu_item.item_id

        if item_id in self._items:
            self._items[item_id]["quantity"] += quantity
        else:
            self._items[item_id] = {
                "item": menu_item,
                "quantity": quantity,
            }

    def set_quantity(self, item_id, quantity):
        if item_id not in self._items:
            raise KeyError("That item is not in the cart.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if quantity == 0:
            self.remove_item(item_id)
        else:
            self._items[item_id]["quantity"] = quantity

    def remove_item(self, item_id):
        if item_id not in self._items:
            raise KeyError("That item is not in the cart.")

        del self._items[item_id]

    def clear(self):
        self._items.clear()

    def is_empty(self):
        return len(self._items) == 0

    def get_items(self):
        """Return cart lines with item, quantity, and subtotal."""
        result = []

        for entry in self._items.values():
            item = entry["item"]
            quantity = entry["quantity"]

            result.append({
                "item": item,
                "quantity": quantity,
                "subtotal": item.price * quantity,
            })

        return result

    def get_total(self):
        total = Decimal("0.00")

        for entry in self._items.values():
            item = entry["item"]
            quantity = entry["quantity"]
            total += item.price * quantity

        return total
