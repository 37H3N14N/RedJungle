from  fastapi import FastAPI
from models.analytics_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/analytic/{param_a}")
def main_get_post(param_a,data: Incoming_Data):
    if param_a == 'event-log':
        respond = {
            "endpoint":"get event log",
            "data": data
        }
        return respond

    if param_a == 'metric':
        respond = {
            "endpoint":"get metric",
            "data": data
        }
        return respond


@app.post("/analytic/{param_a}")
def main_post(param_a,data: Incoming_Data):
    if param_a == 'event-log':
        respond = {
            "endpoint":"post event log",
            "data": data
        }
        return respond

    if param_a == 'metric':
        respond = {
            "endpoint":"post metric",
            "data": data
        }
        return respond



@app.put("/analytic/metric")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint":"put metric",
        "data": data
    }
    return respond


@app.delete("/analytic/{param_a}")
def main_delete(param_a,data: Incoming_Data):
    if param_a == 'event-log':
        respond = {
            "endpoint":"delete event log",
            "data": data
        }
        return respond

    if param_a == 'metric':
        respond = {
            "endpoint":"delete metric",
            "data": data
        }
        return respond





