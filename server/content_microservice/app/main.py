from  fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from functions.main_function import content_read
from functions.main_function import content_create
from functions.main_function import content_update
from functions.main_function import content_delete

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------
@app.post("/{params_b}")
def manage_content(params_b,data: dict):

    allowed_actions = ['read','create','update','delete']

    if params_b not in allowed_actions:

        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Stick to the Program Pal"}
        )

    if params_b == 'read':
        read_content = content_read(data)
        return  read_content

    if params_b == 'create':
        create_content = content_create(data)
        return  create_content

    if params_b == 'update':
        update_content = content_update(data)
        return  update_content

    if params_b == 'delete':
        delete_content = content_delete(data)
        return  delete_content



# --------------------------------------------------------------------
