from  fastapi import FastAPI

from functions.main_function import group_auth_read
from functions.main_function import group_auth_create
from functions.main_function import group_auth_update
from functions.main_function import group_auth_delete

from functions.main_function import folder_auth_read
from functions.main_function import folder_auth_create
from functions.main_function import folder_auth_update
from functions.main_function import folder_auth_delete

from functions.main_function import note_auth_read
from functions.main_function import note_auth_create
from functions.main_function import note_auth_update
from functions.main_function import note_auth_delete

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------
@app.post("/{params_a}/{params_b}")
def manage_auth(params_a,params_b,data: dict):

    category = ['group','folder','note']
    allowed_actions = ['read','create','update','delete']

    if params_a not in category:
        return 'Stick to the Program Pal'

    if params_b not in allowed_actions:
        return 'Stick to the Program Pal'


    if params_a == 'group':

        if params_b == 'read':
            read_group = group_auth_read(data)
            return  read_group

        if params_b == 'create':
            create_group = group_auth_create(data)
            return  create_group

        if params_b == 'update':
            update_group = group_auth_update(data)
            return  update_group

        if params_b == 'delete':
            delete_group = group_auth_delete(data)
            return  delete_group


    if params_a == 'folder':

        if params_b == 'read':
            read_folder = folder_auth_read(data)
            return  read_folder

        if params_b == 'create':
            create_folder = folder_auth_create(data)
            return  create_folder

        if params_b == 'update':
            update_folder = folder_auth_update(data)
            return  update_folder

        if params_b == 'delete':
            delete_folder = folder_auth_delete(data)
            return  delete_folder


    if params_a == 'note':

        if params_b == 'read':
            read_note = note_auth_read(data)
            return  read_note

        if params_b == 'create':
            create_note = note_auth_create(data)
            return  create_note

        if params_b == 'update':
            update_note = note_auth_update(data)
            return  update_note

        if params_b == 'delete':
            delete_note = note_auth_delete(data)
            return  delete_note


# --------------------------------------------------------------------
