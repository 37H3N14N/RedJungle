from  fastapi import FastAPI
from models.access_control_models import Incoming_Data
from functions.main_function import role_function
from functions.main_function import policy_function
from functions.main_function import decision_log_function
from functions.main_function import authorization_function

#####################################################################
app = FastAPI()

#####################################################################

@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'role':
        response_data = role_function(data) 
        return response_data

    if param_a == 'policy':
        response_data = policy_function(data) 
        return response_data

    if param_a == 'authorization':
        response_data = authorization_function(data) 
        return response_data

    if param_a == 'decision-log':
        response_data = decision_log_function(data) 
        return response_data


@app.put("/{param_a}")
def main_put(param_a, data: Incoming_Data):

    if param_a == 'role':
        response_data = role_function(data) 
        return response_data

    if param_a == 'policy':
        response_data = policy_function(data) 
        return response_data


@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'role':
        response_data = role_function(data) 
        return response_data

    if param_a == 'policy':
        response_data = policy_function(data) 
        return response_data

    if param_a == 'decision-log':
        response_data = decision_log_function(data) 
        return response_data



