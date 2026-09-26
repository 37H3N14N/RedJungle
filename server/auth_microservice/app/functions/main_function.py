###################################################
auth_group_db = {} # key=group_id
auth_folder_db = {} # key=folder_id
auth_note_db = {} # key=note_id
###################################################


def group_auth_read(data):
    # group id existance
    # identity
    field_type = data['payload']['field_type']
    group_id = data['payload']['group_id']

    if field_type = 'existance':
        if auth_group_db[group_id]:
            response_data = {
                'status': 'successful',
                'message': 'group exists',
            }
            return response_data

        response_data = {
            'status':'failed',
            'message': 'Group with that id does not exist'
        }
        return response_data


    if field_type = 'details':

        if auth_group_db[group_id]:
            response_data = {
                'status': 'success',
                'members': auth_group_db[group_id]['members']
            }
            return response_data

        response_data = {
            'status': 'failed',
            'message': 'Group with that id does not exist'
        }
        return response_data  

###################################################

def group_auth_create(data):
    # group id existance
    # identity
    group_id = data['payload']['group_id']
    members = data['payload']['members'] # list as input

    group_existance = group_auth_read({'payload':{
        'field_type': 'existance',
        'group_id':group_id
        }})


    if group_existance['status'] == 'successful':
        response_data = {
            'status': 'failed',
            'message': 'Group ACL setup already in place'
        }
        return response_data


    group_auth_db[group_id] = {'members': members}
    response_data = {
        'status': 'successful',
        'message': 'Group ACL created'
    }
    return response_data

###################################################

def group_auth_update(data):
    # group id existance
    # member / identity
    action_type = data['payload']['action_type']
    group_id = data['payload']['group_id']
    members = data['payload']['members']

    group_existance = group_auth_read({'payload':{
        'field_type': 'existance',
        'group_id':group_id
        }})

    if group_existance['status'] == 'successful':

        if action_type == 'addition':
            for user_id in members:
                if user_id not in auth_group_db[group_id]['members']:
                    auth_group_db[group_id]['members'].append(user_id)

            response_data = {
                'status': 'successful',
                'members_added': members,
                'current_members': auth_group_db[group_id]['members']
            }


        if action_type  == 'subtraction':
            for user_id in auth_group_db[group_id]['members']:
                if user_id  in members:
                    auth_group_db[group_id]['members'].remove(user_id)

            response_data = {
                'status': 'successful',
                'members_removed': members,
                'current_members': auth_group_db[group_id]['members']
            }


        if action_type == 'replace':
            auth_group_db[group_id]['members'] = members

            response_data = {
                'status': 'successful',
                'members_replaced': members,
                'current_members': auth_group_db[group_id]['members']
            }


    response_data = {
        'status': 'failed',
        'message': 'Group does not exist'
    }
    return response_data  

###################################################

def group_auth_delete(data):
    # group id existance
    # member / identity
    group_id = data['payload']['group_id']

    group_existance = group_auth_read({'payload':{
        'field_type': 'existance',
        'group_id':group_id
        }})

    if group_existance['status'] == 'successful':
       auth_group_db[group_id] = None 

        response_data = {
            'status': 'successful',
            'message': 'Group deleted',
        }
        return response_data


    response_data = {
        'status': 'failed',
        'message': 'Group does not exist'
    }
    return response_data  



###################################################

def folder_auth_read(data):
    # folder id existance
    # member / identity
    field_type = data['payload']['field_type']
    folder_id = data['payload']['folder_id']

    if field_type = 'existance':
        if auth_folder_db[folder_id]:
            response_data = {
                'status': 'successful',
                'message': 'folder exists'
            }
            return response_data

        response_data = {
            'status':'failed',
            'message': 'Folder with that id does not exist'
        }
        return response_data


    if field_type = 'details':

        if auth_folder_db[folder_id]:
            response_data = {
                'status': 'success',
                'group_id': auth_folder_db[folder_id]['group_id'],
                'admin_id': auth_folder_db[folder_id]['admin_id'],
                'members': auth_folder_db[folder_id]['members']
            }
            return response_data

        response_data = {
            'status': 'failed',
            'message': 'Folder with that id does not exist'
        }
        return response_data  

###################################################

def folder_auth_create(data):
    # folder id existance
    # member / identity
    folder_id = data['payload']['folder_id']
    group_id = data['payload']['group_id']
    members = data['payload']['members']
    admin_id = ''

    folder_existance = folder_auth_read({'payload': {
        'field_type':'existance',
        'folder_id': folder_id
        }})

    if folder_existance['status'] == 'successful':
        response_data = {
            'status': 'failed',
            'message': 'Folder ACL setup already in place'
        }
        return response_data

    if folder_existance['status'] == 'failed':

        auth_folder_db[folder_id] = {
            'group_id': group_id,
            'admin_id': admin_id,
            'members': members
            }

        response_data = {
            'status': 'successful',
            'message': 'Folder ACL created'
        }
        return response_data

###################################################

def folder_auth_update(data):
    # folder id existance
    # member / identity
    folder_id = data['payload']['folder_id']
    field_type = data['payload']['field_type']

    folder_existance = folder_auth_read({'payload': {
        'field_type':'existance',
        'folder_id': folder_id
        }})

    if folder_existance['status'] == 'successful':

        if field_type == 'group_id':
            group_id = data['payload']['group_id']
            auth_folder_db[folder_id]['group_id'] = group_id

            response_data = {
                'status': 'success',
                'group_id': auth_folder_db[folder_id]['group_id']
            }
            return response_data


        if field_type == 'admin_id':
            admin_id = data['payload']['admin_id']
            auth_folder_db[folder_id]['admin_id'] = admin_id

            response_data = {
                'status': 'success',
                'group_id': auth_folder_db[folder_id]['admin_id']
            }
            return response_data


        if field_type == 'members':
            members = data['payload']['members']
            action_type = data['payload']['action_type']

            if action_type == 'addition':
                for user_id in members:
                    if user_id not in auth_folder_db[folder_id]['members']:
                        auth_folder_db[folder_id]['members'].append(user_id)

                response_data = {
                    'status': 'successful',
                    'members_added': members,
                    'current_members': auth_folder_db[folder_id]['members']
                }


            if action_type == 'subtraction':
                for user_id in auth_folder_db[folder_id]['members']:
                    if user_id  in members:
                        auth_folder_db[folder_id]['members'].remove(user_id)

                response_data = {
                    'status': 'successful',
                    'members_removed': members,
                    'current_members': auth_folder_db[folder_id]['members']
                }


            if action_type == 'replace':
                auth_folder_db[folder_id]['members'] = members

                response_data = {
                    'status': 'successful',
                    'members_replaced': members,
                    'current_members': auth_folder_db[folder_id]['members']
                }


    response_data = {
        'status': 'failed',
        'message': 'Folder does not exist'
    }
    return response_data  

###################################################

def folder_auth_delete(data):
    # folder id existance
    # member / identity
    folder_existance = folder_auth_read({'payload': {
        'field_type':'existance',
        'folder_id': folder_id
        }})

    if folder_existance['status'] == 'successful':
       auth_folder_db[folder_id] = None 

        response_data = {
            'status': 'successful',
            'message': 'Folder deleted',
        }
        return response_data


    response_data = {
        'status': 'failed',
        'message': 'Folder does not exist'
    }
    return response_data  


###################################################

def note_auth_read(data):
    # note id existance
    # member / identity
    field_type = data['payload']['field_type']
    note_id = data['payload']['note_id']

    if field_type = 'existance':
        if auth_note_db[note_id]:
            response_data = {
                'status': 'successful',
                'message': 'note exists',
            }
            return response_data

        response_data = {
            'status':'failed',
            'message': 'Note with that id does not exist'
        }
        return response_data


    if field_type = 'details':

        if auth_note_db[note_id]:
            response_data = {
                'status': 'success',
                'group_id': auth_note_db[note_id]['group_id'],
                'folder_id': auth_note_db[note_id]['folder_id'],
                'content_id': auth_note_db[note_id]['content_id'],
                'collaborators': auth_note_db[note_id]['collaborators']
            }
            return response_data

        response_data = {
            'status': 'failed',
            'message': 'Note with that id does not exist'
        }
        return response_data  

###################################################

def note_auth_create(data):
    # note id existance
    # member / identity
    note_id = data['payload']['note_id']
    group_id = data['payload']['group_id']
    folder_id = data['payload']['folder_id']
    collaborators = data['payload']['collaborators']

    note_existance = note_auth_read({'payload': {
        'field_type':'existance',
        'note_id': note_id
        }})

    if note_existance['status'] == 'successful':
        response_data = {
            'status': 'failed',
            'message': 'Note ACL setup already in place'
        }
        return response_data

    if note_existance['status'] == 'failed':

        auth_note_db[note_id] = {
            'group_id': group_id,
            'folder_id': folder_id,
            'collaborators': collaborators
            }

        response_data = {
            'status': 'successful',
            'message': 'Note ACL created'
        }
        return response_data

###################################################

def note_auth_update(data):
    # note id existance
    # member / identity
    note_id = data['payload']['note_id']

    note_existance = note_auth_read({'payload': {
        'field_type':'existance',
        'note_id': note_id
        }})


    if note_existance['status'] == 'successful':

        if field_type == 'group_id':
            group_id = data['payload']['group_id']
            auth_note_db[note_id]['group_id'] = group_id

            response_data = {
                'status': 'success',
                'group_id': auth_note_db[note_id]['group_id']
            }
            return response_data


        if field_type == 'folder_id':
            folder_id = data['payload']['folder_id']
            auth_note_db[note_db]['folder_id'] = folder_id

            response_data = {
                'status': 'success',
                'folder_id': auth_note_db[note_id]['folder_id']
            }
            return response_data


        if field_type == 'collaborators':
            collaborators = data['payload']['collaborators']
            action_type = data['payload']['action_type']

            if action_type == 'addition':
                for user_id in collaborators:
                    if user_id not in auth_note_db[note_id]['collaborators']:
                        auth_note_db[note_id]['collaborators'].append(user_id)

                response_data = {
                    'status': 'successful',
                    'collabs_added': collaborators,
                    'current_collabs': auth_note_db[note_id]['collaborators']
                }


            if action_type == 'subtraction':
                for user_id in auth_note_db[note_id]['collaborators']:
                    if user_id  in collaborators:
                        auth_note_db[note_id]['collaborators'].remove(user_id)

                response_data = {
                    'status': 'successful',
                    'collabs_removed': collaborators,
                    'current_collabs': auth_note_db[note_id]['collaborators']
                }


            if action_type == 'replace':
                auth_note_db[note_id]['collaborators'] = collaborators

                response_data = {
                    'status': 'successful',
                    'collabs_replaced': collaborators,
                    'current_collabs': auth_note_db[note_id]['collaborators']
                }


    response_data = {
        'status': 'failed',
        'message': 'Folder does not exist'
    }
    return response_data  


###################################################

def note_auth_delete(data):
    # note id existance
    # member / identity
    note_existance = note_auth_read({'payload': {
        'field_type':'existance',
        'note_id': note_id
        }})

    if note_existance['status'] == 'successful':
       auth_note_db[note_id] = None 

        response_data = {
            'status': 'successful',
            'message': 'Note deleted',
        }
        return response_data


    response_data = {
        'status': 'failed',
        'message': 'Note does not exist'
    }
    return response_data  

###################################################







