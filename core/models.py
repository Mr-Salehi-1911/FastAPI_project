from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import random
# connecting to database

# DATABASE_URL = "sqlite:///./sqlite.db"

# engine = create_engine(DATABASE_URL, connect_args= {"check_same_thread": False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(55))
    phone_number = Column(String(11), unique=True)
    purchase_code = Column(Integer, unique=True)

    orders = relationship("OrderModel", back_populates="customer")


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total_amount = Column(Float)
    order_date = Column(DateTime, default=func.now())

    customer = relationship(CustomerModel, back_populates="orders", uselist=False)
    items = relationship("OrderItemModel", back_populates="order")

class OrderItemModel(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    order = relationship(OrderModel, back_populates="items", uselist=False)
    product = relationship("ProductModel", uselist=False)


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    name = Column(String)
    price = Column(Float)

# Base.metadata.create_all(engine)


# session = SessionLocal()

# pizza1 = ProductModel(type= "pizza", name= "Margherita Pizza", price= 12.99)
# pizza2 = ProductModel(type= "pizza", name= "Pepperoni Pizza", price= 14.5)
# pizza3 = ProductModel(type= "pizza", name= "BBQ Chicken Pizza", price= 16.75)

# sandwich1 = ProductModel(type= "sandwich", name= "Classic Club Sandwich", price= 8.99)
# sandwich2 = ProductModel(type= "sandwich", name= "Grilled Chicken Sandwich", price= 9.5)
# sandwich3 = ProductModel(type= "sandwich", name= "Vegetarian Sandwich", price= 7.25)
# sandwich4 = ProductModel(type= "sandwich", name= "Beff Burger", price= 10.99)
# sandwich5 = ProductModel(type= "sandwich", name= "Turkey Avocado Sandwich", price= 11.25)

# snack1 = ProductModel(type= "snack", name= "French Fries", price= 4.5)
# snack2 = ProductModel(type= "snack", name= "Onion Rings", price= 5.25)
# snack3 = ProductModel(type= "snack", name= "Mozzarella Sticks", price= 6.75)

# drink1 = ProductModel(type= "drink", name= "Mineral Water", price= 1.99)
# drink2 = ProductModel(type= "drink", name= "Cola", price= 2.99)
# drink3 = ProductModel(type= "drink", name= "Orange Juice", price= 3.5)
# drink4 = ProductModel(type= "drink", name= "Iced Tea", price= 2.75)



# session.add_all([pizza1, pizza2, pizza3, sandwich1, sandwich2, sandwich3, sandwich4, sandwich5, snack1, snack2, snack3, drink1, drink2, drink3, drink4])


# customer1 = CustomerModel(full_name= "Ali Rezaei", phone_number= "09123456789", purchase_code= random.randint(1000, 9999))
# customer2 = CustomerModel(full_name= "Sara Mohammadi", phone_number= "09129876543", purchase_code= random.randint(1000, 9999))
# customer3 = CustomerModel(full_name= "Reza Ahmadi", phone_number= "09351234567", purchase_code= random.randint(1000, 9999))
# customer4 = CustomerModel(full_name= "Maryam Abedi", phone_number= "09107654321", purchase_code= random.randint(1000, 9999))
# customer5 = CustomerModel(full_name= "Shahryar Eftekhari", phone_number= "09012345678", purchase_code= random.randint(1000, 9999))

# session.add_all([customer1, customer2, customer3, customer4, customer5])
# session.commit()