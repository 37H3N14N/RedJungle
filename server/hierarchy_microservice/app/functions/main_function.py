######################################################
group_db = {} # key=group_id
folder_db = {} # key=folder_id
note_db = {}
###################################################

def group_read(data):
        # group existance
        # auth / identity
        # visibility
        assosiation_type = data['payload']['assosiation_type']
        field_type = data['payload']['field_type']

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

                if assosiation_type == 'group_id'
                        group_id = data['payload']['group_id']
                        if group_db[group_id]:

                                response_data = {
                                    'group_id': group_id,
                                    'group_name': group_db[group_id]['group_name'],
                                    'group_owner': group_db[group_id]['group_owner'],
                                    'visibility': group_db[group_id]['visibility'],
                                }
                                return response_data


                if assosiation_type == 'name'
                        group_name = data['payload']['group_name']
                        group_collection = []
                        for key,value in group_db:
                                if value['group_name'] == group_name:
                                        group_collection.append(key)

                        response_data = {
                            'group_name': group_name,
                            'group_collection': group_collection
                        }
                        return response_data


                if assosiation_type == 'owner'
                        group_owner = data['payload']['group_owner']
                        group_collection = []
                        for key,value in group_db:
                                if value['group_owner'] == group_owner:
                                        group_collection.append(key)

                        response_data = {
                            'group_owner': group_owner,
                            'group_collection': group_collection
                        }
                        return response_data


                if assosiation_type == 'visibility'
                        visibility = data['payload']['visibility']
                        group_collection = []
                        for key,value in group_db:
                                if value['visibility'] == visibility:
                                        group_collection.append(key)

                        response_data = {
                            'visibility': visibility,
                            'group_collection': group_collection
                        }
                        return response_data





def group_create(data):
        # group existance
        # identity
        field_type = data['payload']['field_type']
        group_id = data['payload']['group_id']

        group_existance = group_read({field_type='existance','group_id':group_id})


def group_update(user_id, data):
        # group existance
        # auth / identity
        pass

def group_delete(user_id, data):
        # group existance
        # auth / identity
        pass

######################################################

def folder_read(user_id, data):
        # folder existance
        # auth / identity
        # visibility
        pass

def folder_create(user_id, data):
        # folder existance
        # auth / identity
        pass

def folder_update(user_id, data):
        # replace old entry data with new one
        pass

def folder_delete(user_id, data):
        # folder existance
        # auth / identity
        pass


######################################################

def note_read(user_id, data):
        # note existance
        # auth / identity
        # visibility
        pass

def note_create(user_id, data):
        # note existance
        # auth / identity
        # save 2 copies for owner & folder
        pass

def note_update(user_id, data):
        # note existance
        # auth / identity
        # replace old entry data with new one
        pass

def note_delete(user_id, data):
        # note existance
        # auth / identity
        pass

######################################################






















