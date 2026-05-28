from os import path

from fastapi import FastAPI, HTTPException,Path,Query
import json
 
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return{"message":"hello world"}

@app.get('/about')
def about():
    return{"message":"This is my first fastapi application"}

@app.get('/view')
def view():
    data = load_data()
    return data 



@app.get("/patient/{patient_id}")

#path parameter is used to capture the value from the url and pass it to the function as an argument.
def view_patient(
    patient_id: int = Path(
        ...,
        description="ID of the patient in the database",
        example=1
    )
):
     
    data = load_data()

    for patient in data:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(status_code = 404,detail = 'patient not found in the database')

@app.get('/sort')
def sort_patients(sort_by: str = Query(...,
                                       
                                       description = 'sort on the basis of height ,weight or bmi'),order:str = Query('asc',description = 'sort in ascending or descending order')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f'invaid_fields select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = 'invalid order select from asc or desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data