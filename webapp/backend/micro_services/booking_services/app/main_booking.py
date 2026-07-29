from  fastapi import FastAPI
from models.booking_models import Incoming_Data
from functions.main_function import invoice_function
from functions.main_function import guest_function
from functions.main_function import booking_function

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/{param_a}")
def main_get_post(param_a, data: Incoming_Data):

    if param_a == 'guest':
        response_data = guest_function(data) 
        return response_data


    if param_a == 'booking':
        response_data = booking_function(data) 
        return response_data


    if param_a == 'invoice':
        response_data = invoice_function(data)
        return response_data


@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'guest':
        response_data =  guest_function(data)
        return  response_data

    if param_a == 'booking':
        response_data = booking_function(data)
        return response_data


    if param_a == 'invoice':
        response_data = invoice_function(data) 
        return response_data


@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'guest':

        return 


    if param_a == 'booking':
        
        return 


    if param_a == 'invoice':

        return 












