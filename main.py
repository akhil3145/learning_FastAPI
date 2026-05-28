from fastapi import FastAPI
import json
 
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)



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