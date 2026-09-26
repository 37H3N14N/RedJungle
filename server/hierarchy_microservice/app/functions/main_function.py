######################################################
group_db = {} # key=group_id
folder_db = {} # key=folder_id
note_db = {}
###################################################

def group_read(data):
        # group existance
        # auth / identity
        # visibility
        action_type = data['payload']['action_type']
        field_type = data['payload']['field_type']

        if field_type = 'existance':
                group_id = data['payload']['group_id']

                if group_db[group_id]:
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

                if action_type == 'group_id'
                        group_id = data['payload']['group_id']
                        if group_db[group_id]:

                                response_data = {
                                    'group_id': group_id,
                                    'group_name': group_db[group_id]['group_name'],
                                    'group_owner': group_db[group_id]['group_owner'],
                                    'visibility': group_db[group_id]['visibility'],
                                }
                                return response_data


                if action_type == 'name'
                        group_name = data['payload']['group_name']
                        group_collection = []
                        for key,value in group_db.items():
                                if value['group_name'] == group_name:
                                        group_collection.append(key)

                        response_data = {
                            'group_name': group_name,
                            'group_collection': group_collection
                        }
                        return response_data


                if action_type == 'owner'
                        group_owner = data['payload']['group_owner']
                        group_collection = []
                        for key,value in group_db.items():
                                if value['group_owner'] == group_owner:
                                        group_collection.append(key)

                        response_data = {
                            'group_owner': group_owner,
                            'group_collection': group_collection
                        }
                        return response_data


                if action_type == 'visibility'
                        visibility = data['payload']['visibility']
                        group_collection = []
                        for key,value in group_db.items():
                                if value['visibility'] == visibility:
                                        group_collection.append(key)

                        response_data = {
                            'visibility': visibility,
                            'group_collection': group_collection
                        }
                        return response_data

######################################################

def group_create(data):
        # group existance
        # identity
        group_name = data['payload']['group_name']
        group_owner = data['payload']['user_id'] # //// call auth to do the thing
        visibility = data['payload']['visibility']

        group_owner_existance = group_read({'payload':{
                'field_type':'details',
                'action_type':'owner',
                'group_name':group_name
                }})

        if group_owner_existance['status'] == 'successful':
                existing_group_names = group_owner_existance['group_collection']

                for group in existing_group_names:

                        group_detail = group_read({'payload':{
                                'field_type':'details',
                                'action_type':'group_id',
                                'group_id':group
                                }})

                        if group_detail['group_name'] == group_name:
                                response_data = {
                                    'status': 'failed',
                                    'message': 'Group name already in use'
                                }
                                return response_data

                new_group_id = 'random string'
                group_db[new_group_id] = {
                        'group_name':group_name,
                        'group_owner': group_owner,
                        'visibility': visibility,
                }

                response_data = {
                        'status': 'successful',
                        'message': 'Group Created'
                }
                return response_data

        new_group_id = 'random string'
        group_db[new_group_id] = {
                'group_name':group_name,
                'group_owner': group_owner,
                'visibility': visibility,
        }

        response_data = {
                'status': 'successful',
                'message': 'Group Created'
        }
        return response_data

######################################################

def group_update(data):
        # group existance
        # auth / identity
        group_id = data['payload']['group_id']
        user_id = data['payload']['user_id']
        action_type = data['payload']['action_type']

        group_existance = group_read({'payload':{
                'field_type': 'details',
                'action_type': 'group_id',
                'group_id': group_id
        }})

        if group_existance['status'] == 'successful':
                if group_existance['group_owner'] == user_id:

                        if action_type == 'group_name':
                                new_group_name = data['payload']['new_group_name']

                                group_name_vacancy = group_read({'payload':{
                                        'field_type': 'details',
                                        'action_type': 'owner',
                                        'group_owner': user_id
                                }})

                                for group in group_name_vacancy['group_collection']:

                                        group_detail = group_read({'payload':{
                                                'field_type':'details',
                                                'action_type':'group_id',
                                                'group_id':group
                                                }})

                                        if group_detail['group_name'] == new_group_name:
                                                response_data = {
                                                    'status': 'failed',
                                                    'message': 'Group name already in use'
                                                }
                                                return response_data

                                group_db[group_id]['group_name'] = new_group_name
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Group name changed',
                                    'group_name': group_db[group_id]['group_name']
                                }
                                return response_data



                        if action_type == 'visibility':
                                new_visibility = data['payload']['new_visibility']

                                group_db[group_id]['visibility'] = new_visibility
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Group visibility changed',
                                    'group_name': group_db[group_id]['visibility']
                                }
                                return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User not Authorized'
                }
                return response_data


        response_data = {
                'status': 'failed',
                'message': 'Group does not exist'
        }
        return response_data

######################################################

def group_delete(data):
        # group existance
        # auth / identity
        group_id = data['payload']['group_id']
        user_id = data['payload']['user_id']

        group_existance = group_read({'payload':{
                'field_type': 'details',
                'action_type': 'group_id',
                'group_id': group_id,
        }})

        if group_existance['status'] == 'successful':
                if group_existance['group_owner'] == user_id:
                        group_db[group_id] = None

                        response_data = {
                                'status': 'successful',
                                'message': 'Group is deleted'
                        }
                        return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User Not Authorized'
                }
                return response_data

        response_data = {
                'status': 'failed',
                'message': 'Group does not exist'
        }
        return response_data

######################################################

def folder_read(data):
        # folder existance
        # auth / identity
        # visibility
        action_type = data['payload']['action_type']
        field_type = data['payload']['field_type']

        if field_type = 'existance':
                folder_id = data['payload']['folder_id']
                if folder_db[folder_id]:
                    response_data = {
                        'status': 'successful',
                        'message': 'folder exists',
                    }
                    return response_data

                response_data = {
                    'status':'failed',
                    'message': 'Folder with that id does not exist'
                }
                return response_data


        if field_type = 'details':

                if action_type == 'folder_id'
                        folder_id = data['payload']['folder_id']
                        if folder_db[folder_db]:

                                response_data = {
                                    'folder_id': folder_id,
                                    'folder_name': folder_db[folder_id]['folder_name'],
                                    'group_id': folder_db[folder_id]['group_id'],
                                    'visibility': folder_db[folder_id]['visibility']
                                }
                                return response_data


                if action_type == 'name'
                        folder_name = data['payload']['folder_name']
                        folder_collection = []
                        for key,value in folder_db.items():
                                if value['folder_name'] == folder_name:
                                        folder_collection.append(key)

                        response_data = {
                            'folder_name': folder_name,
                            'folder_collection': folder_collection
                        }
                        return response_data

                if action_type == 'group_id'
                        group_id = data['payload']['group_id']
                        folder_collection = []
                        for key,value in folder_db.items():
                                if value['group_id'] == group_id:
                                        folder_collection.append(key)

                        response_data = {
                            'group_id': group_id,
                            'folder_collection': folder_collection
                        }
                        return response_data

                if action_type == 'visibility'
                        visibility = data['payload']['visibility']
                        folder_collection = []
                        for key,value in folder_db.items():
                                if value['visibility'] == visibility:
                                        folder_collection.append(key)

                        response_data = {
                            'visibility': visibility,
                            'folder_collection': folder_collection
                        }
                        return response_data

######################################################

def folder_create(data):
        # folder existance
        # auth / identity
        folder_name = data['payload']['folder_name']
        group_id = data['payload']['group_id'] # call auth to create folder thing
        visibility = data['payload']['visibility']

        folder_owner_existance = folder_read({'payload':{
                'field_type':'details',
                'action_type':'group_id',
                'group_id':group_id
                }})

        if folder_owner_existance['status'] == 'successful':
                existing_folder_names = folder_owner_existance['folder_collection']

                for folder in existing_folder_names:

                        folder_detail = folder_read({'payload':{
                                'field_type':'details',
                                'action_type':'folder_id',
                                'folder_id':folder
                                }})

                        if folder_detail['folder_name'] == folder_name:
                                response_data = {
                                    'status': 'failed',
                                    'message': 'Folder name already in use'
                                }
                                return response_data

                new_folder_id = 'random string'
                folder_db[new_folder_id] = {
                        'folder_name': folder_name,
                        'group_id': group_id,
                        'visibility': visibility
                }

                response_data = {
                        'status': 'successful',
                        'message': 'Folder Created'
                }
                return response_data

        new_folder_id = 'random string'
        folder_db[new_folder_id] = {
                'folder_name':folder_name,
                'group_id': group_id,
                'visibility': visibility,
        }

        response_data = {
                'status': 'successful',
                'message': 'Folder Created'
        }
        return response_data

######################################################

def folder_update(data):

        folder_id = data['payload']['folder_id']
        group_id = data['payload']['group_id']
        user_id = data['payload']['user_id']

        action_type = data['payload']['action_type']

        folder_existance = folder_read({'payload':{
                'field_type': 'details',
                'action_type': 'folder_id',
                'folder_id': folder_id
        }})

        if folder_existance['status'] == 'successful':

                folder_parent_data = group_read({'payload':{
                        'field_type': 'details',
                        'action_type': 'group_id',
                        'group_id': group_id
                }})

                if folder_parent_data['group_owner'] == user_id:

                        if action_type == 'folder_name':
                                new_folder_name = data['payload']['new_folder_name']

                                folder_name_vacancy = folder_read({'payload':{
                                        'field_type': 'details',
                                        'action_type': 'owner',
                                        'group_owner': user_id
                                }})

                                for folder in folder_name_vacancy['folder_collection']:

                                        folder_detail = folder_read({'payload':{
                                                'field_type':'details',
                                                'action_type':'folder_id',
                                                'folder_id':folder
                                                }})

                                        if folder_detail['folder_name'] == new_folder_name:
                                                response_data = {
                                                    'status': 'failed',
                                                    'message': 'Folder name already in use'
                                                }
                                                return response_data

                                folder_db[folder_id]['folder_name'] = new_folder_name

                                response_data = {
                                    'status': 'successful',
                                    'message': 'Folder name changed',
                                    'folder_name': folder_db[folder_id]['folder_name']
                                }
                                return response_data
                                

                        if action_type == 'group_id':
                                new_group_id = data['payload']['new_group_id']

                                folder_db[folder_id]['group_id'] = new_group_id

                                response_data = {
                                    'status': 'successful',
                                    'message': 'Folder group changed',
                                    'group_id': folder_db[folder_id]['group_id']
                                }
                                return response_data


                        if action_type == 'visibility':
                                new_visibility = data['payload']['new_visibility']

                                folder_db[folder_id]['visibility'] = new_visibility
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Folder visibility changed',
                                    'visibility': folder_db[folder_id]['visibility']
                                }
                                return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User not Authorized'
                }
                return response_data


        response_data = {
                'status': 'failed',
                'message': 'Group does not exist'
        }
        return response_data

######################################################

def folder_delete(data):
        # folder existance
        # auth / identity
        folder_id = data['payload']['group_id']
        group_id = data['payload']['group_id']
        user_id = data['payload']['user_id']

        folder_existance = folder_read({'payload':{
                'field_type': 'existance',
                'folder_id': folder_id
        }})

        folder_parent_details = group_read({'payload':{
                'field_type': 'details',
                'action_type': 'group_id',
                'group_id': group_id,
        }})

        if folder_existance['status'] == 'successful':
                if folder_parent_details['group_owner'] == user_id:
                        group_db[group_id] = None

                        response_data = {
                                'status': 'successful',
                                'message': 'Group is deleted'
                        }
                        return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User Not Authorized'
                }
                return response_data

        response_data = {
                'status': 'failed',
                'message': 'Group does not exist'
        }
        return response_data


######################################################

def note_read(data):
        # note existance
        # auth / identity
        # visibility

        action_type = data['payload']['action_type']
        field_type = data['payload']['field_type']

        if field_type = 'existance':
                if note_db[note_id]:
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

                if action_type == 'note_id'
                        note_id = data['payload']['note_id']
                        if note_db[note_id]:

                                response_data = {
                                    'note_id': note_id,
                                    'note_name': note_db[note_id]['note_name'],
                                    'note_owner': note_db[note_id]['note_owner'],
                                    'folder_id': note_db[note_id]['folder_id'],
                                    'content_id': note_db[note_id]['content_id'],
                                    'visibility': note_db[note_id]['visibility']
                                }
                                return response_data


                if action_type == 'name'
                        note_name = data['payload']['note_name']
                        note_collection = []
                        for key,value in note_db.items():
                                if value['note_name'] == note_name:
                                        note_collection.append(key)

                        response_data = {
                            'note_name': note_name,
                            'note_collection': note_collection
                        }
                        return response_data


                if action_type == 'folder_id'
                        folder_id = data['payload']['folder_id']
                        note_collection = []
                        for key,value in note_db.items():
                                if value['folder_id'] == folder_id:
                                        note_collection.append(key)

                        response_data = {
                            'folder_id': folder_id,
                            'note_collection': note_collection
                        }
                        return response_data


                if action_type == 'owner'
                        note_owner = data['payload']['note_owner']
                        note_collection = []
                        for key,value in note_db.items():
                                if value['note_owner'] == note_owner:
                                        note_collection.append(key)

                        response_data = {
                            'note_owner': note_owner,
                            'note_collection': note_collection
                        }
                        return response_data


                if action_type == 'visibility'
                        visibility = data['payload']['visibility']
                        note_collection = []
                        for key,value in note_db.items():
                                if value['visibility'] == visibility:
                                        note_collection.append(key)

                        response_data = {
                            'visibility': visibility,
                            'note_collection': note_collection
                        }
                        return response_data


######################################################

def note_create(data):
        # note existance
        # auth / identity
        # save 2 copies for owner & folder
        note_name = data['payload']['note_name']
        note_owner = data['payload']['user_id']
        folder_id = data['payload']['folder_id']
        content_id = data['payload']['content_id']
        visibility = data['payload']['visibility']

        note_owner_existance = note_read({'payload':{
                'field_type':'details',
                'action_type':'owner',
                'note_name':note_name
                }})

        if note_owner_existance['status'] == 'successful':
                existing_note_names = note_owner_existance['note_collection']

                for note in existing_note_names:

                        note_detail = note_read({'payload':{
                                'field_type':'details',
                                'action_type':'note_id',
                                'note_id':note
                                }})

                        if note_detail['note_name'] == note_name:
                                response_data = {
                                    'status': 'failed',
                                    'message': 'Note name already in use'
                                }
                                return response_data

                new_note_id = 'random string'
                note_db[new_note_id] = {
                        'note_name':note_name,
                        'note_owner': note_owner,
                        'folder_id': folder_id,
                        'content_id': content_id,
                        'visibility': visibility
                }

                response_data = {
                        'status': 'successful',
                        'message': 'Note Created'
                }
                return response_data

        new_note_id = 'random string'
        note_db[new_note_id] = {
                'note_name':note_name,
                'note_owner': note_owner,
                'folder_id': folder_id,
                'content_id': content_id,
                'visibility': visibility
        }

        response_data = {
                'status': 'successful',
                'message': 'Note Created'
        }
        return response_data

######################################################

def note_update(data):
        # note existance
        # auth / identity
        # replace old entry data with new one
        note_id = data['payload']['note_id']
        user_id = data['payload']['user_id']
        action_type = data['payload']['action_type']

        note_existance = note_read({'payload':{
                'field_type': 'details',
                'action_type': 'note_id',
                'note_id': note_id
        }})

        if note_existance['status'] == 'successful':
                if note_existance['note_owner'] == user_id:

                        if action_type == 'note_name':
                                new_note_name = data['payload']['new_note_name']

                                note_name_vacancy = note_read({'payload':{
                                        'field_type': 'details',
                                        'action_type': 'owner',
                                        'note_owner': user_id
                                }})

                                for note in note_name_vacancy['note_collection']:

                                        note_detail = note_read({'payload':{
                                                'field_type':'details',
                                                'action_type':'note_id',
                                                'note_id':note
                                                }})

                                        if note_detail['note_name'] == new_note_name:
                                                response_data = {
                                                    'status': 'failed',
                                                    'message': 'Note name already in use'
                                                }
                                                return response_data

                                note_db[note_id]['note_name'] = new_note_name
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Note name changed',
                                    'note_name': note_db[note_id]['note_name']
                                }
                                return response_data


                        if action_type == 'folder_id':
                                new_folder_id = data['payload']['new_folder_id']

                                note_db[note_id]['folder_id'] = new_folder_id
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Note visibility changed',
                                    'folder_id': note_db[note_id]['folder_id']
                                }
                                return response_data


                        if action_type == 'visibility':
                                new_visibility = data['payload']['new_visibility']

                                note_db[note_id]['visibility'] = new_visibility
                                response_data = {
                                    'status': 'successful',
                                    'message': 'Note visibility changed',
                                    'visibility': note_db[note_id]['visibility']
                                }
                                return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User not Authorized'
                }
                return response_data


        response_data = {
                'status': 'failed',
                'message': 'Note does not exist'
        }
        return response_data


######################################################

def note_delete(data):
        # note existance
        # auth / identity
        note_id = data['payload']['note_id']
        folder_id = data['payload']['folder_id']
        user_id = data['payload']['user_id']

        note_existance = note_read({'payload':{
                'field_type': 'details',
                'action_type': 'note_id',
                'note_id': note_id,
        }})


        if note_existance['status'] == 'successful':

                note_parent_details = folder_read({'payload':{
                        'field_type': 'details',
                        'action_type': 'folder_id',
                        'folder_id': folder_id
                }})

                folder_parent_details = group_read({'payload':{
                        'field_type': 'details',
                        'action_type': 'folder_id',
                        'folder_id': note_parent_details['group_id']
                }})

                if note_existance['note_owner'] == user_id or folder_parent_details['group_owner'] == user_id:
                        note_db[note_id] = None

                        response_data = {
                                'status': 'successful',
                                'message': 'Note is deleted'
                        }
                        return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'User Not Authorized'
                }
                return response_data

        response_data = {
                'status': 'failed',
                'message': 'Note does not exist'
        }
        return response_data


######################################################






















