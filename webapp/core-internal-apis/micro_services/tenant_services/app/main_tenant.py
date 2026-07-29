from  fastapi import FastAPI
from models.tenant_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/{param_a}")
def main_get_post(param_a, data: Incoming_Data):

    if param_a == 'tenant':
        respond = {
            "endpoint": 'get tenant',
            "echo_data": data
        }
        return  respond

    if param_a == 'billing':
        respond = {
            "endpoint": 'get billing',
            "echo_data": data
        }
        return  respond


@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'tenant':
        respond = {
            "endpoint": 'post tenant',
            "echo_data": data
        }
        return  respond

    if param_a == 'billing':
        respond = {
            "endpoint": 'post billing',
            "echo_data": data
        }
        return  respond



@app.put("/tenant")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put tenant',
        "echo_data": data
    }
    return  respond




@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'tenant':
        respond = {
            "endpoint": 'delete tenant',
            "echo_data": data
        }
        return  respond

    if param_a == 'billing':
        respond = {
            "endpoint": 'delete billing',
            "echo_data": data
        }
        return  respond











