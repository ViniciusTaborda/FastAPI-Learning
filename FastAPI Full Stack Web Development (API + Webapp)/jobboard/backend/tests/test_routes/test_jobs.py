import json


def test_create_job(client):
    data = {
        "title": "Sde 1 Yahoo",
        "company": "Testhoo",
        "company_url": "https://www.test.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200


def test_retreive_by_id(client):
    data = {
        "title": "Sde 1 Yahoo",
        "company": "Testhoo",
        "company_url": "https://www.test.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20",
    }

    response_post = client.post("/job/create-job", json.dumps(data))
    assert response_post.status_code == 200
    response = client.get("/job/get/1")
    assert response.status_code == 200
