from  fastapi import FastAPI
from models.payment_gateway_models import Incoming_Data
from functions.main_function import transaction_function
from functions.main_function import bank_function
from functions.main_function import customer_function
from functions.main_function import account_function

#####################################################################
app = FastAPI()

#####################################################################

@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'transaction':
        response_data = transaction_function(data) 
        return response_data


    if param_a == 'bank':
        response_data = bank_function(data) 
        return response_data


    if param_a == 'account':
        response_data = account_function(data) 
        return response_data


    if param_a == 'customer':
        response_data = customer_function(data) 
        return response_data
    

@app.delete("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'transaction':
        response_data = transaction_function(data) 
        return response_data


    if param_a == 'bank':
        response_data = bank_function(data) 
        return response_data


    if param_a == 'account':
        response_data = account_function(data) 
        return response_data


    if param_a == 'customer':
        response_data = customer_function(data) 
        return response_data

