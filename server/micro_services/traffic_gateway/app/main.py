from  fastapi import FastAPI, HTTPException, Query
import httpx
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

identity_user_endpoint = "http://192.168.1.103:9012/user/"
identity_session_endpoint = "http://192.168.1.103:9012/session/"

hierarchy_group_endpoint = "http://192.168.1.103:9013/group/"
hierarchy_folder_endpoint = "http://192.168.1.103:9013/folder/"
hierarchy_note_endpoint = "http://192.168.1.103:9013/note/"

member_group_endpoint = "http://192.168.1.103:9014/member/group/"
member_super_endpoint = "http://192.168.1.103:9014/member/super/"
member_folder_endpoint = "http://192.168.1.103:9014/member/folder/"
member_note_endpoint = "http://192.168.1.103:9014/member/note/"

note_data_endpoint = "http://192.168.1.103:9015/note-data/"

#####################################################################


@app.get("/ssrf/")
async def get_ssrf(url: str = 'super',selection_type: str = '',session_id: str = ''):

    async with httpx.AsyncClient() as client:
        try:
            url_response = await client.get(f'http://192.168.1.103:9014/member/{url}', params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            url_response.raise_for_status() 

            data_collection = {
                'url_response':url_response.json()
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

@app.get("/group/")
async def get_group(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            group_response = await client.get(hierarchy_group_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            group_response.raise_for_status() 

            data_collection = {
                'group':group_response.json()
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

@app.post("/group/")
async def manage_group(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            group_response = await client.post(hierarchy_group_endpoint, json=data, timeout=4.0)
            group_response.raise_for_status() 

            data_collection = {
                'group':group_response.json()
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

@app.get("/folder/")
async def get_folder(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            folder_response = await client.get(hierarchy_folder_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            folder_response.raise_for_status() 

            data_collection = {
                'folder':folder_response.json()
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

@app.post("/folder/")
async def manage_folder(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            folder_response = await client.post(hierarchy_folder_endpoint, json=data, timeout=4.0)
            folder_response.raise_for_status() 

            data_collection = {
                'folder':folder_response.json()
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

@app.get("/note/")
async def get_note(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            note_response = await client.get(hierarchy_note_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            note_response.raise_for_status() 

            data_collection = {
                'note':note_response.json()
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

@app.post("/note/")
async def manage_note(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            note_response = await client.post(hierarchy_note_endpoint, json=data, timeout=4.0)
            note_response.raise_for_status() 

            data_collection = {
                'note':note_response.json()
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

@app.get("/note-data/")
async def get_note_data(selection_type: str = '', session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            note_data_response = await client.get(note_data_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            note_data_response.raise_for_status() 

            data_collection = {
                'note-data':note_data_response.json()
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

@app.post("/note-data/")
async def manage_note_data(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            note_data_response = await client.post(note_data_endpoint, json=data, timeout=4.0)
            note_data_response.raise_for_status() 

            data_collection = {
                'note-data':note_data_response.json()
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

@app.get("/member/super/")
async def get_member_super(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            member_super_response = await client.get(member_super_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            member_super_response.raise_for_status() 

            data_collection = {
                'member_super':member_super_response.json(),
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

@app.post("/member/super/")
async def manage_member_super(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            member_super_response = await client.post(member_super_endpoint, json=data, timeout=4.0)
            member_super_response.raise_for_status() 

            data_collection = {
                'member_super':member_super_response.json()
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

@app.get("/member/group/")
async def get_member_group(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            member_group_response = await client.get(member_group_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            member_group_response.raise_for_status() 

            data_collection = {
                'member_group':member_group_response.json(),
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

@app.post("/member/group/")
async def manage_member_group(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            member_group_response = await client.post(member_group_endpoint, json=data, timeout=4.0)
            member_group_response.raise_for_status() 

            data_collection = {
                'member_group':member_group_response.json()
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

@app.get("/member/folder/")
async def get_member_folder(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            member_folder_response = await client.get(member_folder_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            member_folder_response.raise_for_status() 

            data_collection = {
                'member_folder':member_folder_response.json(),
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

@app.post("/member/folder/")
async def manage_member_folder(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            member_folder_response = await client.post(member_folder_endpoint, json=data, timeout=4.0)
            member_folder_response.raise_for_status() 

            data_collection = {
                'member_folder':member_folder_response.json()
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

@app.get("/member/note/")
async def get_member_note(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            member_note_response = await client.get(member_note_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            member_note_response.raise_for_status() 

            data_collection = {
                'member_note':member_note_response.json()
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

@app.post("/member/note/")
async def manage_member_note(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            member_note_response = await client.post(member_note_endpoint, json=data, timeout=4.0)
            member_note_response.raise_for_status() 

            data_collection = {
                'member_note':member_note_response.json()
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

@app.get("/identity/user")
async def get_identity_user(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            identity_user_response = await client.get(identity_user_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            identity_user_response.raise_for_status() 

            data_collection = {
                'identity_user':identity_user_response.json(),
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

@app.post("/identity/user/")
async def manage_identity_user(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            identity_user_response = await client.post(identity_user_endpoint, json=data, timeout=4.0)
            identity_user_response.raise_for_status() 

            data_collection = {
                'identity_user':identity_user_response.json()
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

@app.get("/identity/session/")
async def get_identity_session(selection_type: str = '',session_id: str = ''):
    
    async with httpx.AsyncClient() as client:
        try:
            identity_session_response = await client.get(identity_session_endpoint, params={'selection_type':selection_type,'session_id':session_id},timeout=4.0)
            identity_session_response.raise_for_status() 

            data_collection = {
                'identity_session':identity_session_response.json()
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

@app.post("/identity/session/")
async def manage_identity_session(data: dict):

    async with httpx.AsyncClient() as client:
        try:
            identity_session_response = await client.post(identity_session_endpoint, json=data, timeout=4.0)
            identity_session_response.raise_for_status() 

            data_collection = {
                'identity_session':identity_session_response.json()
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














################################################



















