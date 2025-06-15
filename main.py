from fastapi import FastAPI
import json

app = FastAPI()

def load_json():
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

# @app.get("/greet/{name}")
# def greet(name: str):
#     return {"message": f"Hello, {name}!"}

@app.get("/view")
def view():
    data = load_json()
    return data