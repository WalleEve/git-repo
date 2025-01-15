import datetime
from dataclasses import dataclass

@dataclass
class Product:
    product_id: str
    product_name: str
    product_type: str
    product_brand: str
    measure_unit: str
    unit_price: int
    product_mrp: int
    tax_catagory:str

@dataclass
class Review:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime