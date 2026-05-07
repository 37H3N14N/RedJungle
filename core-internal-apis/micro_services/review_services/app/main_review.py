from  fastapi import FastAPI
from models.review_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/review")
def main_get_post(data: Incoming_Data):
    respond = {
        "endpoint": 'get review',
        "echo_data": data
    }
    return  respond


@app.post("/review")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post review',
        "echo_data": data
    }
    return  respond


@app.put("/review")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put review',
        "echo_data": data
    }
    return  respond


@app.delete("/review")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete review',
        "echo_data": data
    }
    return  respond






