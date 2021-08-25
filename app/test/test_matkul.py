from fastapi.testclient import TestClient
from . import utils


def test_create_matkul(client: TestClient):
    access_token = utils.get_user_access_token("admin")
    response = client.post(
        "/api/matkul",
        headers=utils.get_token_headers(access_token),
        json={
            "nama": "Mata Kuliah Test",
            "dosen": "TEST",
            "hari": "test",
            "jam": "12:00",
            "kelas": "A",
            "ruang": "IF-TEST",
            "sks": 6
        })

    assert response.status_code == 201
    assert response.json() == utils.get_test_data_id()


def test_get_matkuls(client: TestClient):
    access_token = utils.get_user_access_token("admin")
    response = client.get(
        "/api/matkuls",
        headers=utils.get_token_headers(access_token))

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_matkul(client: TestClient):
    access_token = utils.get_user_access_token("admin")
    test_data_id = utils.get_test_data_id()
    test_data = utils.get_test_data()

    response = client.get(
        "/api/matkul?id="+test_data_id,
        headers=utils.get_token_headers(access_token))

    assert response.status_code == 200
    assert response.json() == test_data


def test_update_matkul(client: TestClient):
    access_token = utils.get_user_access_token("admin")
    test_data_id = utils.get_test_data_id()

    response = client.put(
        "/api/matkul",
        headers=utils.get_token_headers(access_token),
        json={
            "id": test_data_id,
            "nama": "Mata Kuliah Test",
            "dosen": "TEST-UPDATED",
            "hari": "test",
            "jam": "12:00",
            "kelas": "A",
            "ruang": "IF-TEST",
            "sks": 6
        })

    assert response.status_code == 200
    assert response.json() == test_data_id


def test_delete_matkul(client: TestClient):
    access_token = utils.get_user_access_token("admin")
    test_data_id = utils.get_test_data_id()
    test_data = utils.get_test_data()

    response = client.delete(
        "/api/matkul?id="+test_data_id,
        headers=utils.get_token_headers(access_token))

    assert response.status_code == 200
    assert response.json() == test_data
