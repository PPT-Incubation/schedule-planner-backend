from fastapi.encoders import jsonable_encoder
from .. import security, mongo, schemas


def get_token_headers(token : str):
    return {"Authorization": f"Bearer {token}"}

def get_user_access_token(subject : str):
    return security.create_access_token(subject=subject)

def get_test_data_id():
    data = mongo.client.schedule_planner.matkuls.find_one({"nama" : "Mata Kuliah Test"})
    return str(data["_id"])

def get_test_data():
    data = mongo.client.schedule_planner.matkuls.find_one({"nama" : "Mata Kuliah Test"})
    data = schemas.MatkulOut(**data, id = get_test_data_id())
    return jsonable_encoder(data)