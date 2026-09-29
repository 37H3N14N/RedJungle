from  fastapi import FastAPI

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
