from fastapi import FastAPI, HTTPException, Query
import json

app = FastAPI()

def load_json():
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/view")
def view():
    data = load_json()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_json()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/search")
def search_patients(name: str = Query(..., description="search patient by name")):
    data = load_json()
    results = {
        id: patient for id, patient in data.items() 
        if name.lower() in patient.get('name', '').lower()
    }
    if not results:
        raise HTTPException(status_code=404, detail="No patients found")
    return results

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort by height, weight or bmi"), order: str = Query('asc', description="sort in asc or desc order")):
    valid_sort_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid sort order")

    data = load_json()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data