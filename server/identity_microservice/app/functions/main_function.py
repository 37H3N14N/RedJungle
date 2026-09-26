#################################################
user_db = {} # key=email 
session_db = {} # key=session_id

#################################################

def user_read(data):
        # email existance
        # passcode match
        field_type = data['payload']['field_type']

        if field_type == 'existance':
                user_id = data['payload']['user_id']
                for key,value in user_db.items():
                        if value['user_id'] == user_id:
                                response_data = {
                                        'status': 'successful',
                                        'user_id': user_id,
                                        'message': 'user exists'
                                }
                                return  response_data

                response_data = {
                        'status': 'failed',
                        'user_id': user_id,
                        'message': 'user_id does not exists'
                }
                return  response_data
                

        if field_type == 'details':
                action_type = data['payload']['action_type']

                if action_type == 'email':
                        email = data['payload']['email']

                        if user_db[email]:
                                response_data = {
                                        'status': 'successful',
                                        'user_id': user_db['email']['user_id'],
                                        'hashcode': user_db['email']['hashcode']
                                }
                                return response_data

                        response_data = {
                                'status': 'failed',
                                'email': email,
                                'message': 'email is invalid'
                        }
                        return  response_data

                if action_type == 'user_id':
                        user_id = data['payload']['user_id']

                        for key,value in user_db.items():
                                if value['user_id'] == user_id:
                                        response_data = {
                                                'status': 'successful',
                                                'email': key,
                                                'hashcode': value['hashcode']
                                        }
                                        return response_data

                        response_data = {
                                'status': 'failed',
                                'user_id': user_id,
                                'message': 'No user with that user_id'
                        }
                        return response_data




#################################################

def user_create(data):
        # email existance
        email = data['payload']['email']
        hashcode = data['payload']['hashcode']

        user_existance = user_read({'payload':{
                'field_type': 'detail',
                'action_type': 'email',
                'email': email
        }})

        if user_existance['status'] == successful:
                response_data = {
                        'status': 'failed',
                        'message': 'email already in use'
                }
                return response_data

        user_db[email] = {
                'user_id': 'random_string',
                'hashcode': current_hashcode
                }
        session_id = session_create(user_db[email]['user_id'])

        response_data = {
                'status': 'successful',
                'message': 'new user created',
                'session_id': session_id['session_id']
        }
        return  response_data

#################################################

def user_update(data):
        # session existance / match
        session_id = data['payload']['session_id']
        old_hashcode = data['payload']['old_hashcode']
        new_hashcode = data['payload']['new_hashcode']

        session_existance = session_read({'payload': {
                'field_type': 'details',
                'action_type': 'session_id',
                'session_id': session_id
                }})

        if session_existance['status'] == 'successful':
                session_user_id = session_existance['user_id']
                saved_user_data = user_read({'payload': {
                        'field_type': 'details',
                        'action_type': 'user_id',
                        'user_id':session_user_id
                }})

                saved_session_hashcode = saved_user_data['hashcode']
                
                if saved_user_data == old_hashcode:
                        user_db[session_user_id]['hashcode'] == new_hashcode

                        response_data = {
                                'status': 'successful',
                                'message': 'hashcode updated'
                        }
                        return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'Lack of authorization to update user'
                }
                return response_data 

        response_data = {
                'status': 'failed',
                'message': 'session_id does not exist'
        }
        return response_data 


#################################################

def user_delete(data):
        # session existance 
        session_id = data['payload']['session_id']
        hashcode = data['payload']['hashcode']

        session_existance = session_read({'payload': {
                'field_type': 'details',
                'action_type': 'session_id',
                'session_id': session_id
                }})

        if session_existance['status'] == 'successful':
                session_user_id = session_existance['user_id']
                session_user_data = user_read({'payload': {
                        'field_type': 'details',
                        'action_type': 'user_id',
                        'user_id': session_user_id
                }})
                session_user_hashcode = session_user_data['hashcode']
                session_user_email = session_user_data['email']

                if session_user_hashcode == hashcode:
                        user_db[session_user_email] == None

                        response_data = {
                                'status': 'successful',
                                'message': 'user has been deleted'
                        }
                        return response_data 

                response_data = {
                        'status': 'failed',
                        'message': 'Lack of authorization to delete user'
                }
                return response_data 

        response_data = {
                'status': 'failed',
                'message': 'session does not exist'
        }
        return response_data 



#################################################

def session_read(data):
        # session existance
        # user existance & match
        field_type = data['payload']['field_type']

        if field_type == 'details':
                session_id = data['payload']['session_id']

                if session_db[session_id]: 
                        response_data = {
                                'status': 'successful',
                                'user_id': session_db[session_id]['user_id'],
                                'session_status': session_db[session_id]['status']
                        }
                        return response_data

                response_data = {
                        'status': 'failed',
                        'message': 'session_id does not exist'
                }
                return  response_data

        if field_type == 'existance':
                action_type = data['payload']['action_type']

                if action_type == 'session_id':
                        session_id = data['payload']['session_id']

                        if session_db[session_id]: 
                                response_data = {
                                        'status': 'successful',
                                        'session_id': session_id
                                }
                                return response_data
        
                        response_data = {
                                'status': 'failed',
                                'message': 'session_id does not exist'
                        }
                        return  response_data
                        
                if action_type == 'user_id':
                        user_id = data['payload']['user_id']

                        for key,value in session_db.items():
                                if value['user_id'] == user_id:
                                        response_data = {
                                                'status': 'successful',
                                                'session_id': key
                                        }
                                        return response_data
        
                        response_data = {
                                'status': 'failed',
                                'message': 'No session id with that user_id'
                        }
                        return response_data
        

#################################################

def session_create(data):
        # session existance
        # user existance 
        user_id = data['payload']['user_id']

        session_existance = session_read({'payload': {
                'field_type': 'existance',
                'action_type': 'user_id'
                'user_id': user_id
                }})

        if session_existance['status'] == 'successful':
                response_data = {
                        'status': 'failed',
                        'message': 'session already exists'
                        'session_id': session_existance['session_id']
                }
                return response_data


        if session_existance['status'] == 'failed':
                new_session_id = 'random string'

                session_db[new_session_id] = {
                        'user_id': user_id,
                        'status': 'active'
                        }

                response_data = {
                        'status': 'successful',
                        'session_id': new_session_id
                }
                return response_data


#################################################

def session_delete(data):
        session_id = data['payload']['session_id']
        hashcode = data['payload']['hashcode']

        session_existance = session_read({'payload': {
                'field_type': 'details',
                'action_type': 'session_id',
                'session_id': session_id
                }})

        if session_existance['status'] == 'successful':
                session_user_id = session_existance['user_id']
                session_user_data = user_read({'payload': {
                        'field_type': 'details',
                        'action_type': 'user_id',
                        'user_id': session_user_id
                }})
                session_user_hashcode = session_user_data['hashcode']
                session_user_email = session_user_data['email']

                if session_user_hashcode == hashcode:
                        session_db[session_id] == None

                        response_data = {
                                'status': 'successful',
                                'message': 'session has been deleted'
                        }
                        return response_data 

                response_data = {
                        'status': 'failed',
                        'message': 'Lack of authorization to delete session'
                }
                return response_data 

        response_data = {
                'status': 'failed',
                'message': 'session does not exist'
        }
        return response_data 



#################################################



