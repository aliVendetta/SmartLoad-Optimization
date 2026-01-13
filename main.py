from fastapi import FastAPI
from models import OptimizeRequest
from optimizer import optimize_orders
from validators import filter_compatible_orders
from utils import percent

app = FastAPI(title="SmartLoad Optimization API")


@app.get("/healthz")
def health():
    return {"status": "ok"}


@app.post("/api/v1/load-optimizer/optimize")
def optimize(request: OptimizeRequest):

    orders = filter_compatible_orders(request.orders)

    if not orders:
        return {
            "truck_id": request.truck.id,
            "selected_order_ids": [],
            "total_payout_cents": 0,
            "total_weight_lbs": 0,
            "total_volume_cuft": 0,
            "utilization_weight_percent": 0,
            "utilization_volume_percent": 0
        }

    selected_orders, payout, weight, volume = optimize_orders(
        request.truck, orders
    )

    return {
        "truck_id": request.truck.id,
        "selected_order_ids": [o.id for o in selected_orders],
        "total_payout_cents": payout,
        "total_weight_lbs": weight,
        "total_volume_cuft": volume,
        "utilization_weight_percent": percent(weight, request.truck.max_weight_lbs),
        "utilization_volume_percent": percent(volume, request.truck.max_volume_cuft),
    }
