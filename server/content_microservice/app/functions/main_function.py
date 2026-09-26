###################################################
content_db = {}
###################################################

def content_read(data):
    # content existance
    # auth / identity 
    # visibility
    action_type = data['payload']['action_type']
    field_type = data['payload']['field_type']
    user_id = data['payload']['user_id']

        if field_type = 'existance':
                content_id = data['payload']['content_id']

                if content_db[content_id]:
                    response_data = {
                        'status': 'successful',
                        'message': 'content exists',
                    }
                    return response_data

                response_data = {
                    'status':'failed',
                    'message': 'content with that id does not exist'
                }
                return response_data


        if field_type = 'details':

                if action_type == 'content_id'
                        content_id = data['payload']['content_id']
                        if content_db[content_id]:

                                response_data = {
                                    'content_id': content_id,
                                    'note_id': content_db[content_id]['note_id'],
                                    'group_id': content_db[content_id]['group_id'],
                                    'folder_id': content_db[content_id]['folder_id'],
                                    'contents': content_db[content_id]['contents']
                                }
                                return response_data


                if action_type == 'group_id'
                        group_id = data['payload']['group_id']

                        content_collection = []
                        for key,value in content.items():
                                if value['group_id'] == group_id:
                                        content_collection.append(key)

                        response_data = {
                            'group_id': group_id,
                            'content_collection': content_collection
                        }
                        return response_data

                if action_type == 'folder_id'
                        folder_id = data['payload']['folder_id']

                        content_collection = []
                        for key,value in content.items():
                                if value['folder_id'] == folder_id:
                                        content_collection.append(key)

                        response_data = {
                            'folder_id': folder_id,
                            'content_collection': content_collection
                        }
                        return response_data


###################################################

def content_create(data):
    # content existance
    # auth / identity 
    note_id = data['payload']['note_id']
    group_id = data['payload']['group_id']
    folder_id = data['payload']['folder_id']
    contents = data['payload']['contents']

    new_content_id = 'random string'

    content_db[new_content_id] = {
            'content_id':new_content_id,
            'note_id':note_id,
            'group_id':group_id,
            'folder_id':folder_id,
            'contents':contents,
    }

    response_data = {
            'status' : 'successful',
            'message' : 'Note Created',
            'Note' : content_db[new_content_id]
    }
    return response_data


###################################################

def content_update(data):
    # content existance
    # auth / identity 
    content_id = data['payload']['content_id']
    action_type = data['payload']['action_type']
    user_id = data['payload']['user_id']

    content_existance = content_read({'payload':{
            'field_type': 'existance',
            'content_id': content_id
    }})

    if content_existance['status'] == 'successful':

        if action_type == 'contents':
            new_contents = data['payload']['new_contents']

            content_db[content_id]['contents'] = new_contents
            response_data = {
                'status': 'successful',
                'message': 'Note contents changed',
                'contents': content_db[content_id]['contents']
            }
            return response_data


        if action_type == 'group_id':
            new_group_id = data['payload']['new_group_id']

            content_db[content_id]['group_id'] = new_group_id
            response_data = {
                'status': 'successful',
                'message': 'Note group_id changed',
                'group_id': content_db[content_id]['group_id']
            }
            return response_data


        if action_type == 'folder_id':
            new_folder_id = data['payload']['new_folder_id']

            content_db[content_id]['folder_id'] = new_folder_id
            response_data = {
                'status': 'successful',
                'message': 'Note folder_id changed',
                'folder_id': content_db[content_id]['folder_id']
            }
            return response_data



    response_data = {
        'status': 'failed',
        'message': 'Content does not exist'
    }
    return response_data 


###################################################

def content_delete(data):
    # content existance
    # auth / identity 
    content_id = data['payload']['content_id']
    user_id = data['payload']['user_id']

    content_existance = content_read({'payload':{
        'field_type': 'existance',
        'content_id': content_id,
    }})

    if note_existance['status'] == 'successful':
        content_db[content_id] = None

        response_data = {
                'status': 'successful',
                'message': 'Content is deleted'
        }
        return response_data

    response_data = {
       'status': 'failed',
       'message': 'Content does not exist'
    }
    return response_data

###################################################

















































