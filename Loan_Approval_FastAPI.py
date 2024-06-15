import uvicorn 
from fastapi import FastAPI
# Here we are using LoanVariable python file which we created and using LoanVariable class from it.
from LoanVariable import LoanVariable
import numpy as np 
import pandas as pd
import pickle


app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to Krishna Salve Web': f'{name}'}


@app.post('/predict')
def predict_LoanStatus(data:LoanVariable):
    data = data.dict()
    print(data)
    income_annum=data['income_annum']
    loan_amount=data['loan_amount']
    loan_term=data['loan_term']
    cibil_score=data['cibil_score']
    commercial_assets_value=data['commercial_assets_value']
    
    prediction = classifier.predict([[income_annum,loan_amount,loan_term,cibil_score,commercial_assets_value]])
    if (prediction[0]<0.5):
        prediction='Loan Approved'
    else:
        prediction='Loan Rejected'
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
## To run this API use
### uvicorn Loan_Approval_FastAPI:app --reload
## Here Loan_Approval_FastAPI is our python file name and app is our API app name
## Run this in Anaconda Prompt.