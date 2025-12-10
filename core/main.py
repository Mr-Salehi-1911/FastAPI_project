from fastapi import FastAPI, HTTPException, status, Query, Path

app = FastAPI()

costs = [
    {"id": 1, "page": "main_page", "cost": 5.5},
    {"id": 2, "page": "products", "cost": 12.45},
    {"id": 3, "page": "orders", "cost": 8.25},
    {"id": 4, "page": "about us", "cost": 2.75},
    {"id": 5, "page": "contact us", "cost": 3.75}
]

# ایجاد هزینه جدید با id یکتا
@app.post("/costs")
def create_cost(page_name:str, cost: float):
    new_cost = {"id": len(costs) + 1, "page": page_name, "cost": cost}
    costs.append(new_cost)

# دریافت همه ی هزینه ها
@app.get("/costs")
def retrieve_cost_list():
    return costs

# دریافت یک هزینه با id هر page
@app.get("/costs/{page_id}")
def retrieve_cost_list(page_id: int):
    for cost in costs:
        if cost["id"] == page_id:
            return cost
    return {"message": "detail not found"}

# ویرایش هزینه ی یک page با شناسه ی id
@app.put("/costs/{page_id}")
def update_cost(page_id:int, new_cost:float):
    for cost in costs:
        if cost["id"] == page_id:
            cost["cost"] = new_cost
            return {"message": f"Cost for page {cost["page"]} has changed into {cost["cost"]}"}
    return {"message": "detail not found"}

# حذف هزینه با id
@app.delete("/costs/{page_id}")
def delete_cost(page_id:int):
    for cost in costs:
        if cost["id"] == page_id:
            costs.remove(cost)
            return {"message": f"Cost for page {cost["page"]} removed successfully"}
    return {"message": "detail not found"}