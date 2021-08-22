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