from  fastapi import FastAPI, HTTPException, Query
import httpx
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------

@app.get("/note-data/")
def get_group_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single note-data',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all note-datas',
    }
    return  http_response 

# --------------------------------------------------------------------

@app.post("/note-data/")
def manage_group_member(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'

    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create note',
            "data_pack": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update note',
            "data_pack": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete note',
            "data_pack": data
        }
        return  http_response 

# --------------------------------------------------------------------

@app.post("/ssrf/")
async def manage_ssrf(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            url_response = await client.get(f"http://{data['url']}", timeout=4.0)
            url_response.raise_for_status() 

            data_collection = {
                'url_data':url_response.json()
            }

            return data_collection
            
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code, 
                detail=f"External API error: {exc.response.text}"
            )
        except httpx.RequestError:
            raise HTTPException(
                status_code=503, 
                detail="External API is unavailable"
            )


# --------------------------------------------------------------------

@app.get("/hidden-endpoint/")
def get_hidden_endpoint(selection_type: str = 'all',session_id: str = ''):

    print('hidden-endpoint hit')

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single hidden endpoint',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all data from hidden endpoint',
    }
    return  http_response 

# --------------------------------------------------------------------



