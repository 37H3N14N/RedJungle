from  fastapi import FastAPI, status
from fastapi.responses import JSONResponse


from functions.main_function import user_read
from functions.main_function import user_create
from functions.main_function import user_update
from functions.main_function import user_delete

from functions.main_function import session_read
from functions.main_function import session_create
from functions.main_function import session_delete

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------
@app.post("/{params_a}/{params_b}")
def manage_identity(params_a,params_b,data: dict):

    category = ['user','session']
    allowed_actions = ['read','create','update','delete']

    if params_a not in category:

        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Stick to the Program Pal"}
        )

    if params_b not in allowed_actions:

        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Stick to the Program Pal"}
        )


    if params_a == 'user':

        if params_b == 'read':
            read_user = user_read(data)
            return  read_user

        if params_b == 'create':
            create_user = user_create(data)
            return  create_user

        if params_b == 'update':
            update_user = user_update(data)
            return  update_user

        if params_b == 'delete':
            delete_user = user_delete(data)
            return  delete_user


    if params_a == 'session':

        if params_b == 'read':
            read_session = session_read(data)
            return  read_session

        if params_b == 'create':
            create_session = session_create(data)
            return  create_session

        if params_b == 'delete':
            delete_session = session_delete(data)
            return  delete_session




# --------------------------------------------------------------------
