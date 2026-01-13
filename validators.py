from typing import List
from app.models import Order


def filter_compatible_orders(orders: List[Order]) -> List[Order]:
    if not orders:
        return []

    base_origin = orders[0].origin
    base_destination = orders[0].destination

    filtered = []
    for o in orders:
        if o.origin != base_origin:
            continue
        if o.destination != base_destination:
            continue
        if o.pickup_date > o.delivery_date:
            continue
        filtered.append(o)

    return filtered


def hazmat_compatible(selected_orders: List[Order]) -> bool:
    if not selected_orders:
        return True

    hazmat_flags = {o.is_hazmat for o in selected_orders}
    return len(hazmat_flags) == 1
