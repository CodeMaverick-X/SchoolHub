#!/usr/bin/python3
"""test flask pages"""

import json
from models import storage
from models.user import User



def test_index_home(client):
    """test landing page"""
    response = client.get('/')

    assert b'<title>SchoolHub</title>' in response.data


def test_register(client, app):
    """test client registration"""
    username = "reinhard"
    password = "super_secrete"
    response = client.post("/register", data={"username": username, "password": password})

    with app.app_context():
        user = storage.get_user(username)
        assert user.username == username
        assert user.password != password # password has been hashed
        assert user.id != ""

def test_register_existing_user(client, app):
    """test that user name is unique"""
    username = "reinhard"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    response2 = client.post("/register", data={"username": username, "password": password})
    rep = json.loads(response2.data.decode('utf-8'))
    assert rep.get("success") == False


def test_wrong_poass_login(client):
    """test password authentication"""
    username = "reinhard"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    response2 = client.post("/", data={"username": username, "password": "wrong_password"})
    rep = json.loads(response2.data.decode('utf-8'))

    assert response2.status_code == 400
    assert rep.get("success") == False
