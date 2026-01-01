from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
from schemas import CustomerSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import CustomerModel, ProductModel, OrderModel, OrderItemModel
import random

app = FastAPI()

# connecting to db
DATABASE_URL = "sqlite:///../sqlite.db"

engine = create_engine(DATABASE_URL, connect_args= {"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

@app.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer(customer : CustomerSchema):
    new_purchase_code = random.randint(1000, 9999)
    new_customer = CustomerModel(full_name = customer.full_name, phone_number = customer.phone_number, purchase_code= new_purchase_code)
    session.add(new_customer)
    
    message = f"A new customer added with name '{customer.full_name}' and purchase_code '{new_purchase_code}'"
    session.commit()
    return JSONResponse({"message": message})

@app.get("/customers")
def retrieve_customers():
    response = session.query(CustomerModel).all()
    return response

@app.get("/customers/{id}")
def retrieve_customer(id : int):
    response = session.query(CustomerModel).filter_by(id= id).one_or_none()
    return response

@app.delete("/customers/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(id : int):
    response = session.query(CustomerModel).filter_by(id = id).one_or_none()
    if response:
        session.delete(response)
        session.commit()
        message = f"Customer {response.full_name} has been deleted from db successfully"
        return JSONResponse({"message": message})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object Not Found")

@app.post("/orders")
def make_order(purchase_code : int = Query(description="Please enter your purchase code"),
               orders : list[int] = Query(description= "Enter your product ids.")):
    customers = session.query(CustomerModel).all()
    for customer in customers:
        if customer.purchase_code == purchase_code:
            customer_id = customer.id
            break
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You don't have a purchase code.")
    

    


    items = session.query(ProductModel).all()

    
    # counting total amount
    total_amount= 0
    for order in orders:
        for item in items:
            if order == item.id:
                total_amount += item.price

    total_amount = round(total_amount, 2)

    new_order = OrderModel(customer_id= customer_id, total_amount= total_amount)

    session.add(new_order)
    session.commit()

    for order in orders:
        for item in items:
            if order == item.id:
                new_order_item = OrderItemModel(order_id= new_order.id, product_id= order)
                session.add(new_order_item)
                session.commit()
    

    

    message = f"Order for customer {customer.full_name} with price {total_amount}$ created successfully"
    return JSONResponse({"message": message})