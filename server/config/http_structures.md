    [ HTTP STRUCTURES ]


=> /hierarchy

-------------------------------------------------------
group_read = {
    'payload':{
        'field_type':'details',
        'action_type':'name',
        'group_name':'somename' or 'group_id'/'owner'/'visibility'
    }
}

field_type = ['existance','details']
action_type = ['group_id','name','owner','visibility']

-------------------------------------------------------
group_create = {
    'payload':{
        'group_name':'somename',
        'group_owner':'user_id',
        'visibility':'public'
    }
}

-------------------------------------------------------
group_update = {
    'payload':{
        'action_type':'group_name',
        'group_id':'group_id',
        'new_group_name':'name', or  'visibility':''
        'user_id':'user_id'
    }
}

action_type = ['group_name','visibility']

-------------------------------------------------------
group_delete = {
    'payload':{
        'group_id':'group_id',
        'user_id':'user_id'
    }
}

-------------------------------------------------------
-------------------------------------------------------
folder_read = {
    'payload':{
        'field_type':'details',
        'action_type':'name',
        'folder_name':'somename' or 'folder_id'/'group_id'/'visibility'
    }
}

field_type = ['existance','details']
action_type = ['folder_id','name','group_id','visibility']

-------------------------------------------------------
folder_create = {
    'payload':{
        'folder_name':'somename',
        'group_id':'group_id',
        'user_id':'user_id',
        'visibility':'public'
    }
}

-------------------------------------------------------
folder_update = {
    'payload':{
        'action_type':'folder_name',
        'folder_id':'folder_id',
        'new_folder_name':'name', or 'new_group_id'/'new_visibility'
        'user_id':'user_id'
    }
}

action_type = ['folder_name','group_id','visibility']

-------------------------------------------------------
folder_delete = {
    'payload':{
        'folder_id':'folder_id',
        'user_id':'user_id'
    }
}

-------------------------------------------------------
-------------------------------------------------------
note_read = {
    'payload':{
        'field_type':'details',
        'action_type':'name',
        'note_name':'somename' or 'folder_id'/'note_id'/'note_owner'/'visibility'
    }
}

field_type = ['existance','details']
action_type = ['note_id','name','folder_id','owner','visibility']

-------------------------------------------------------
note_create = {
    'payload':{
        'note_name':'somename',
        'note_owner':'user_id',
        'folder_id':'folder_id',
        'content_id':'content_id',
        'visibility':'public'
    }
}

-------------------------------------------------------
note_update = {
    'payload':{
        'action_type':'note_name',
        'note_id':'note_id',
        'user_id':'user_id',
        'new_note_name':'name', or 'new_folder_id'/'new_visibility'
    }
}

action_type = ['note_name','folder_id','visibility']

-------------------------------------------------------
note_delete = {
    'payload':{
        'note_id':'note_id',
        'folder_id':'folder_id',
        'user_id':'user_id'
    }
}

-------------------------------------------------------

=> /auth 

-------------------------------------------------------
group_auth_read = {
    'payload':{
        'field_type':'details',
        'group_id':'group_id'
    }
}

field_type = ['existance','details']

-------------------------------------------------------
group_auth_create = {
    'payload':{
        'group_id':'group_id',
        'members':[]
    }
}

-------------------------------------------------------
group_auth_update = {
    'payload':{
        'action_type':'group_name',
        'group_id':'group_id',
        'members':[]
    }
}

action_type = ['addition','subtraction','replace']

-------------------------------------------------------
group_auth_delete = {
    'payload':{
        'group_id':'group_id'
    }
}

-------------------------------------------------------

-------------------------------------------------------
folder_auth_read = {
    'payload':{
        'field_type':'details',
        'folder_id':'folder_id'
    }
}

field_type = ['existance','details']

-------------------------------------------------------
folder_auth_create = {
    'payload':{
        'folder_id':'folder_id',
        'group_id':'group_id',
        'members':[],
        'admin_id':'user_id'
    }
}

-------------------------------------------------------
folder_auth_update = {
    'payload':{
        'field_type':'group_id',
        'folder_id':'folder_id',
        'group_id':'group_id' or 'admin_id'
    }
}

field_type = ['admin_id','group_id','members']

folder_auth_update = {
    'payload':{
        'field_type':'members',
        'folder_id':'folder_id',
        'action_type':'addition'
        'members':[]
    }
}

action_type = ['addition','subtraction','replace']

-------------------------------------------------------
folder_auth_delete = {
    'payload':{
        'folder_id':'folder_id'
    }
}

-------------------------------------------------------
-------------------------------------------------------
note_auth_read = {
    'payload':{
        'field_type':'details',
        'note_id':'note_id'
    }
}

field_type = ['existance','details']

-------------------------------------------------------
note_auth_create = {
    'payload':{
        'note_id':'note_id',
        'group_id':'group_id',
        'folder_id':'folder_id',
        'collaborators':[]
    }
}

-------------------------------------------------------
note_auth_update = {
    'payload':{
        'field_type':'group_id',
        'note_id':'note_id',
        'group_id':'group_id' or 'folder_id'
    }
}

field_type = ['folder_id','group_id','collaborators']

note_auth_update = {
    'payload':{
        'field_type':'collaborators',
        'note_id':'note_id',
        'action_type':'addition',
        'collaborators':[]
    }
}

action_type = ['addition','subtraction','replace']

-------------------------------------------------------
note_delete = {
    'payload':{
        'note_id':'note_id'
    }
}

-------------------------------------------------------

=> /content

-------------------------------------------------------
content_read = {
    'payload':{
        'field_type':'existance',
        'action_type':'name',
        'content_id':'content_id' or 'group_id'/'folder_id'
    }
}

field_type = ['existance','details']
action_type = ['content_id','group_id','folder_id']

-------------------------------------------------------
content_create = {
    'payload':{
        'note_id':'note_id',
        'group_id':'group_id',
        'folder_id':'folder_id',
        'contents':[]
    }
}

-------------------------------------------------------
content_update = {
    'payload':{
        'content_id':'content_id',
        'action_type':'contents',
        'new_contents':'some text' or 'new_group_id'/'new_folder_id'
    }
}

action_type = ['contents','group_id','folder_id']

-------------------------------------------------------
content_delete = {
    'payload':{
        'content_id':'content_id'
    }
}

-------------------------------------------------------

=> /identity

-------------------------------------------------------
user_read = {
    'payload':{
        'field_type':'details',
        'user_id':'user_id'
    }
}

field_type = ['existance','details']

user_read = {
    'payload':{
        'field_type':'details',
        'action_type':'name',
        'user_id':'somename' or 'group_id'/'owner'/'visibility'
    }
}

action_type = ['email','user_id']

-------------------------------------------------------
user_create = {
    'payload':{
        'email':'someemail',
        'hashcode':'passcode'
    }
}

-------------------------------------------------------
user_update = {
    'payload':{
        'session_id':'session_id',
        'old_hashcode':'passcode',
        'new_hashcode':'passcode'
    }
}

-------------------------------------------------------
user_delete = {
    'payload':{
        'session_id':'session_id',
        'hashcode':'passcode'
    }
}

-------------------------------------------------------
-------------------------------------------------------
session_read = {
    'payload':{
        'field_type':'details',
        'sesion_id':'session_id'
    }
}

field_type = ['existance','details']

user_read = {
    'payload':{
        'field_type':'existance',
        'action_type':'session_id',
        'session_id':'session_id' or 'user_id'
    }
}

action_type = ['session_id','user_id']

-------------------------------------------------------
session_create = {
    'payload':{
        'user_id':'user_id'
    }
}

-------------------------------------------------------
session_delete = {
    'payload':{
        'session_id':'session_id',
        'hashcode':'passcode'
    }
}

-------------------------------------------------------







