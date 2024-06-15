from pydantic import BaseModel

class LoanVariable(BaseModel):
    income_annum: float 
    loan_amount: float 
    loan_term: float 
    cibil_score: float 
    commercial_assets_value: float 

