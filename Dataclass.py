from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    isbn:str
    price:float
b=Book("The Great Gatsby","F. Scott Fitzgerald","9780743273565",500)    
print(b)
