
from models.user_model import *

def get_users():
    return get_all_users()

def get_user(user_id):
    return get_user_by_id(user_id)

def create_user(data):
    return insert_user(data['name'], data['email'], data['password'])

