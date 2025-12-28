from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse

app = FastAPI()

# This is a list of dicts for creating a website that contains prices for each page to create.
prices = [
    {"id": 1, "page": "main_page", "price": 5.5},
    {"id": 2, "page": "products", "price": 12.45},
    {"id": 3, "page": "orders", "price": 8.25},
    {"id": 4, "page": "about us", "price": 2.75},
    {"id": 5, "page": "contact us", "price": 3.75}
]

# ایجاد هزینه جدید برای ساخت پیج جدید با شناسه آیدی یکتا
@app.post("/prices", status_code= status.HTTP_201_CREATED)
def create_price(page:str = Query(description="name of the page"), price: float = Query(description="price for create the page")):
    new_price = {"id": len(prices) + 1, "page": page, "price": price}
    prices.append(new_price)

# دریافت هزینه ی ساخت همه ی پیج ها
@app.get("/prices")
def retrieve_price_list():
    return prices

# دریافت هزینه ی ساخت یک پیج
@app.get("/prices/{id}")
def retrieve_price_list(id: int):
    for price in prices:
        if price["id"] == id:
            return JSONResponse(price)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object Not Found")

# ویرایش هزینه ی ساخت یک پیج با شناسه آیدی یکتا
@app.put("/prices/{id}")
def change_price(id:int, new_price:float = Path(description="add a new price for named page")):
    for price in prices:
        if price["id"] == id:
            price["price"] = new_price
            message = f"Price for page {price["page"]} has changed into {price["price"]} dollars"
            return {"message": message}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object Not Found")

# حذف هزینه برای ساخت یک پیج با شناسه آیدی یکتا
@app.delete("/prices/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_price(id:int = Path(description="insert id of related page to delete the price")):
    for price in prices:
        if price["id"] == id:
            message = f"Price for page {price["page"]} removed successfully"
            prices.remove(price)
            return JSONResponse({"message": message})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object Not Found")