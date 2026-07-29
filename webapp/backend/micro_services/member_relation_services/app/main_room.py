from  fastapi import FastAPI
from models.room_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/{param_a}")
def main_get_post(param_a,data: Incoming_Data):

    if param_a == 'room':
        respond = {
            "endpoint": 'get room',
            "echo_data": data
        }
        return respond
    
    if param_a == 'amenity':
        respond = {
            "endpoint": 'get amenity',
            "echo_data": data
        }
        return respond

@app.post("/get/amenity/picture")
def main_get_post(data: Incoming_Data):
    respond = {
        "endpoint": 'get picture',
        "echo_data": data
    }
    return respond


@app.post("/{param_a}")
def main_post(param_a,data: Incoming_Data):

    if param_a == 'room':
        respond = {
            "endpoint": 'post room',
            "echo_data": data
        }
        return respond
    
    if param_a == 'amenity':
        respond = {
            "endpoint": 'post amenity',
            "echo_data": data
        }
        return respond

@app.post("/amenity/picture")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post picture',
        "echo_data": data
    }
    return respond


@app.put("/{param_a}")
def main_put(param_a,data: Incoming_Data):

    if param_a == 'room':
        respond = {
            "endpoint": 'put room',
            "echo_data": data
        }
        return respond
    
    if param_a == 'amenity':
        respond = {
            "endpoint": 'put amenity',
            "echo_data": data
        }
        return respond

@app.put("/amenity/picture")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put picture',
        "echo_data": data
    }
    return respond


@app.delete("/{param_a}")
def main_delete(param_a,data: Incoming_Data):

    if param_a == 'room':
        respond = {
            "endpoint": 'delete room',
            "echo_data": data
        }
        return respond
    
    if param_a == 'amenity':
        respond = {
            "endpoint": 'delete amenity',
            "echo_data": data
        }
        return respond

@app.delete("/amenity/picture")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete picture',
        "echo_data": data
    }
    return respond














