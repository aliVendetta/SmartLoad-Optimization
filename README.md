# SmartLoad Optimization API

Stateless load optimization service that selects the optimal combination
of shipment orders for a truck.

## Features
- Bitmask DP optimization (n ≤ 22)
- Weight + volume constraints
- Hazmat compatibility
- Route compatibility
- Integer-only money handling
- Dockerized & stateless

## Run Locally

```bash
git clone <your-repo>
cd smartload-optimizer
docker compose up --build
