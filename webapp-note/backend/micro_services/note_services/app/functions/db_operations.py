from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.review_db_initialization import get_session
from databank.review_db_initialization import Message_Object
from databank.review_db_initialization import Picture_Object
from databank.review_db_initialization import Review_Object


###################################################################
session = get_session()

###################################################################
def get_uuid4():
    random_uuid = uuid.uuid4()
    return random_uuid

def get_timestamp():
   now = datetime.now()
   refined_structure = now.strftime("%Y-%m-%d %H:%M:%S")
   return refined_structure

###################################################################

def create_message(message_text_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    message_item = Message_Object(
        message_id= constant_uuid[0], 
        message_text= message_text_input,
        date_created= get_timestamp(),
        date_updated= get_timestamp() 
        )

    response_data.append({'message_id': f'{constant_uuid[0]}'})

    session.add(message_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_picture(picture_url_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    picture_item = Picture_Object(
        picture_id= constant_uuid[0], 
        picture_url= picture_url_input,
        date_created= get_timestamp()
        )

    response_data.append({'picture_id': f'{constant_uuid[0]}'})

    session.add(picture_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_review(user_id_input,tenant_id_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    review_item = Review_Object(
        review_id= constant_uuid[0],
        user_id= user_id_input,
        tenant_id= tenant_id_input,
        date_created= get_timestamp(),
        date_updated= get_timestamp()
        )

    response_data.append({'review_id': f'{constant_uuid[0]}'})

    session.add(review_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_review_picture(db_session,picture_column_name,picture_row_identifier,review_column_name,review_row_identifier):

    target_review = read_data(db_session,'review',review_column_name,review_row_identifier)
    target_picture = read_data(db_session,'picture',picture_column_name,picture_row_identifier)

    target_review.pictures.append(target_picture)

    db_session.commit()
    db_session.close()
    return


def create_link_btwn_review_message(db_session,message_column_name,message_row_identifier,review_column_name,review_row_identifier):

    target_review = read_data(db_session,'review',review_column_name,review_row_identifier)
    target_message = read_data(db_session,'message',message_column_name,message_row_identifier)

    target_review.messages.append(target_message)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'message':
        column = getattr(Message_Object,column_name)
        target_item = db_session.query(Message_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'review':
        column = getattr(Review_Object,column_name)
        target_item = db_session.query(Review_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'picture':
        column = getattr(Picture_Object,column_name)
        target_item = db_session.query(Picture_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'message':

        identify_column = getattr(Message_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Message_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'picture':

        identify_column = getattr(Picture_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Picture_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'review':

        identify_column = getattr(Review_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Review_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'message':
        target_item = db_session.query(Message_Object).filter(Message_Object.message_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'picture':
        target_item = db_session.query(Picture_Object).filter(Picture_Object.picture_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'review':
        target_item = db_session.query(Review_Object).filter(Review_Object.review_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'message':
        res_data = db_session.query(Message_Object).all()
        return res_data

    if table_name == 'picture':
        res_data = db_session.query(Picture_Object).all()
        return res_data

    if table_name == 'review':
        res_data = db_session.query(Review_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'message':
        all_rows = delete(Message_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'picture':
        all_rows = delete(Picture_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'review':
        all_rows = delete(Review_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_message('hello message from customer','15thMar','17thOct')
#create_picture('http://redjungle/picture/007','1stJan')
#create_review('user47','tenant008','2ndMonth','6thMonth')

#create_link_btwn_review_picture(session,'date_created','1stJan','user_id','user47')
#create_link_btwn_review_message(session,'date_created','15thMar','user_id','user47')

#data_one = read_all_data(session,'review')

#for singular_review in data_one:
#    print(singular_review.user_id)
#    print(singular_review.tenant_id)
#    for pic in singular_review.pictures:
#        print(pic.picture_url, pic.date_created)
#    for msg in singular_review.messages:
#        print(msg.message_text, msg.date_created)


#session.close()




