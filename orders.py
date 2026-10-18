# This module creates an order number, records the items and customer information, saves orders to orders.json, and displays a confirmation.


import json
import uuid
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ORDERS_FILE = Path(__file__).resolve().parent / "orders.json"


def create_order(cart, customer):
    if cart.is_empty():
        raise ValueError("Cannot submit an order with an empty cart.")

    order_items = []

    for line in cart.get_items():
        item = line["item"]

        order_items.append({
            "item_id": item.item_id,
            "name": item.name,
            "unit_price": str(item.price),
            "quantity": line["quantity"],
            "subtotal": str(line["subtotal"]),
        })

    return {
        "order_id": f"QB-{uuid.uuid4().hex[:8].upper()}",
        "created_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "customer_name": customer["customer_name"],
        "contact_number": customer["contact_number"],
        "order_type": "Pickup",
        "items": order_items,
        "total": str(cart.get_total()),
        "status": "Submitted",
    }


def save_order(order):
    """Append an order to the local JSON order history."""
    if ORDERS_FILE.exists():
        try:
            with ORDERS_FILE.open("r", encoding="utf-8") as file:
                orders = json.load(file)
        except (json.JSONDecodeError, OSError) as error:
            raise RuntimeError(
                "Could not read the order history. "
                "Please check orders.json before continuing."
            ) from error

        if not isinstance(orders, list):
            raise RuntimeError(
                "The order history must contain a JSON list."
            )
    else:
        orders = []

    orders.append(order)

    # Write to a temporary file first, then replace the original.
    temporary_file = ORDERS_FILE.with_suffix(".tmp")

    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)
            file.write("\n")

        temporary_file.replace(ORDERS_FILE)
    except OSError as error:
        raise RuntimeError(
            "Could not save the order. Check folder permissions."
        ) from error

    return order


def display_confirmation(order):
    print("\n" + "=" * 55)
    print("             ORDER CONFIRMATION")
    print("=" * 55)
    print("Your pickup order has been submitted successfully!")
    print(f"Order number: {order['order_id']}")
    print(f"Customer:     {order['customer_name']}")
    print(f"Order type:   {order['order_type']}")
    print(f"Status:       {order['status']}")
    print(f"Date:         {order['created_at']}")
    print("-" * 55)

    print(f"{'Item':<23}{'Qty':>6}{'Subtotal':>13}")
    print("-" * 55)

    for item in order["items"]:
        print(
            f"{item['name']:<23}"
            f"{item['quantity']:>6}"
            f"${Decimal(item['subtotal']):>12.2f}"
        )

    print("-" * 55)
    print(f"{'TOTAL':>42} ${Decimal(order['total']):>9.2f}")
    print("=" * 55)
    print("Thank you for ordering with QuickBite!")
    print("Please keep your order number for pickup.")
