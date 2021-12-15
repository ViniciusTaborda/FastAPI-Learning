import json


def test_create_user(client):
    user_data = {
        "username": "test_username",
        "email": "test@email.com",
        "password": "123456",
    }

    response = client.post("/users/", data=json.dumps(user_data))
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert response.json()["username"] == user_data["username"]
    assert response.json()["is_active"] == True
