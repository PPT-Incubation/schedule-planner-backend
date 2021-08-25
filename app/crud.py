from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
from . import mongo, schemas, security

def get_user_by_username(username : str):
    user = mongo.client.schedule_planner.users.find_one({"username" : username})
    if not user:
        return None
    return schemas.UserOutDB(**user)

def authenticate_user(user : schemas.UserIn):
    user_from_db = get_user_by_username(user.username)
    if not user_from_db:
        return None
    if not security.verify_password(user.password, user_from_db.hashed_pwd):
        return None
    return user_from_db

def get_all_matkuls():
    return mongo.client.schedule_planner.matkuls.find({})

def get_a_matkul(id : str):
    return mongo.client.schedule_planner.matkuls.find_one({"_id" : ObjectId(id)})

def create_a_matkul(matkul : schemas.MatkulCreate):
    encoded_data = jsonable_encoder(matkul)
    return mongo.client.schedule_planner.matkuls.insert_one(encoded_data).inserted_id

def update_a_matkul(matkul : schemas.MatkulUpdate):
    encoded_data = jsonable_encoder(matkul)
    updated_data = { k : v for k,v in encoded_data.items() if k!="id"}

    return mongo.client.schedule_planner.matkuls.find_one_and_update(
        {"_id" : ObjectId(encoded_data['id'])},
        { "$set" : updated_data},
        return_document=ReturnDocument.AFTER)['_id']



def delete_a_matkul(id : str):
    return mongo.client.schedule_planner.matkuls.find_one_and_delete({"_id" : ObjectId(id)})