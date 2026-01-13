from typing import List, Tuple
from models import Truck, Order
from validators import hazmat_compatible


def optimize_orders(
    truck: Truck,
    orders: List[Order]
) -> Tuple[List[Order], int, int, int]:

    n = len(orders)
    best_payout = 0
    best_mask = 0

    weights = [o.weight_lbs for o in orders]
    volumes = [o.volume_cuft for o in orders]
    payouts = [o.payout_cents for o in orders]

    for mask in range(1 << n):
        total_weight = 0
        total_volume = 0
        total_payout = 0
        selected = []

        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_volume += volumes[i]

                if total_weight > truck.max_weight_lbs:
                    break
                if total_volume > truck.max_volume_cuft:
                    break

                total_payout += payouts[i]
                selected.append(orders[i])
        else:
            if not hazmat_compatible(selected):
                continue

            if total_payout > best_payout:
                best_payout = total_payout
                best_mask = mask

    final_orders = [orders[i] for i in range(n) if best_mask & (1 << i)]

    total_weight = sum(o.weight_lbs for o in final_orders)
    total_volume = sum(o.volume_cuft for o in final_orders)

    return final_orders, best_payout, total_weight, total_volume
