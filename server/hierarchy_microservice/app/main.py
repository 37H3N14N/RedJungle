from  fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from functions.main_function import group_read
from functions.main_function import group_create
from functions.main_function import group_update
from functions.main_function import group_delete

from functions.main_function import folder_read
from functions.main_function import folder_create
from functions.main_function import folder_update
from functions.main_function import folder_delete

from functions.main_function import note_read
from functions.main_function import note_create
from functions.main_function import note_update
from functions.main_function import note_delete

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------
@app.post("/{params_a}/{params_b}")
def manage_hierarchy(params_a,params_b,data: dict):

    category = ['group','folder','note']
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


    if params_a == 'group':

        if params_b == 'read':
            read_group = group_read(data)
            return  read_group

        if params_b == 'create':
            create_group = group_create(data)
            return  create_group

        if params_b == 'update':
            update_group = group_update(data)
            return  update_group

        if params_b == 'delete':
            delete_group = group_delete(data)
            return  delete_group


    if params_a == 'folder':

        if params_b == 'read':
            read_folder = folder_read(data)
            return  read_folder

        if params_b == 'create':
            create_folder = folder_create(data)
            return  create_folder

        if params_b == 'update':
            update_folder = folder_update(data)
            return  update_folder

        if params_b == 'delete':
            delete_folder = folder_delete(data)
            return  delete_folder


    if params_a == 'note':

        if params_b == 'read':
            read_note = note_read(data)
            return  read_note

        if params_b == 'create':
            create_note = note_create(data)
            return  create_note

        if params_b == 'update':
            update_note = note_update(data)
            return  update_note

        if params_b == 'delete':
            delete_note = note_delete(data)
            return  delete_note


# --------------------------------------------------------------------
