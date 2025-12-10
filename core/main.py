from fastapi import FastAPI, HTTPException, status, Query, Path

app = FastAPI()

costs = [
    {"id": 1, "page": "main_page", "cost": 5.5},
    {"id": 2, "page": "products", "cost": 12.45},
    {"id": 3, "page": "orders", "cost": 8.25},
    {"id": 4, "page": "about us", "cost": 2.75},
    {"id": 5, "page": "contact us", "cost": 3.75}
]