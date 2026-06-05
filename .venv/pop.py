

from fastapi import FastAPI,Query
from unicodedata import category

app = FastAPI()

products = [
    {"id": 1, "name": "Cocos", "category": "fruits", "price": 600, "count": 6},
    {"id": 2, "name": "Banana", "category": "fruits", "price": 500, "count": 50},
    {"id": 3, "name": "Apple", "category": "fruits", "price": 300, "count": 33},
    {"id": 4, "name": "Carrot", "category": "vegetables", "price": 400, "count": 47},
    {"id": 5, "name": "Potato", "category": "vegetables", "price": 200, "count": 5000}
]

@app.get("/all_products")
def a():
    return products

@app.get("/filtir_name")
def b(name: str = Query()):
    a = []
    for x in products:
        if x['name'] == name:
            a.append(x)
    return a[:3]

@app.get("/filtir_category")
def c(category: str = Query()):
    res = []
    for x in products:
        if x['category'] == category:
            res.append(x)
    return res[:3]

@app.get("/filtir_min_pricez")
def d(mp: int = Query()):
    res = []
    for x in products:
        if x['price'] >= mp:
            res.append(x)
    return res[:3]

@app.get("/filtir_max_pricrz")
def e(mx: int = Query()):
    res = []
    for x in products:
        if x['price'] <= mx:
            res.append(x)
    return res[:3]

@app.get("/filtir_count")
def f(count: int = Query()):
    res = []
    for x in products:
        if x['count'] <= count:
            res.append(x)
    return res[:3]