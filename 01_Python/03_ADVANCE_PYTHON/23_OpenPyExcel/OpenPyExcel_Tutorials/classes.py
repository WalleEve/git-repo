import datetime 
from dataclasses import dataclass 

@dataclass 
class Product:
    id: str 
    name: str 
    type : str
    brand: str 
    description: str 

@dataclass 
class Price:
    name: str     
    price: int 
    exp_date: datetime.datetime
    taxable: str 
