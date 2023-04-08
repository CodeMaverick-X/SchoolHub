#!/usr/bin/python3
"""tests for the courses manupulation endpoints"""

import json

def test_courses_get(client):
    """test the get courses route"""
    username = "reinhard8"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    course_list = client.get('/api/v1/courses')
    rep = json.loads(course_list.data.decode('utf-8'))

    assert type(rep) == list
    assert rep == []

def test_course_post(client):
    """test that courses are created"""
    username = "reinhard9"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    course_details = {"name": "Eng 100", "description": "engineering society"}
    response2 = client.post('/api/v1/courses', data=course_details)
    assert response2.status_code == 201

    course_list = client.get('/api/v1/courses')
    rep = json.loads(course_list.data.decode('utf-8'))

    assert rep[0].get("name") == "Eng 100"
    assert rep[0].get("description") == "engineering society"


def test_course_delete(client):
    """test the delete course route"""
    username = "reinhardA"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    course_details = {"name": "Eng 100", "description": "engineering society"}
    response2 = client.post('/api/v1/courses', data=course_details)
    assert response2.status_code == 201

    course_list = client.get('/api/v1/courses')
    rep = json.loads(course_list.data.decode('utf-8'))

    course_id = rep[0].get('id')

    response3 = client.delete(f'/api/v1/courses/{course_id}')

    assert response3.status_code == 200

    course_list_2 = client.get('/api/v1/courses')
    rep_2 = json.loads(course_list_2.data.decode('utf-8'))
    assert rep_2 == []

def test_set(client):
    """test the put set route"""
    username = "reinhardB"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    response1.status_code == 200
    set_details = {"year": 2, "semester": 1}
    headers = {'content-type': 'application/json'}
    response2 = client.put('/api/v1/set', data=json.dumps(set_details), headers=headers)
    rep_2 = response2.data.decode('utf-8')
    assert response2.status_code == 200
    # test get

    set_info = client.get('/api/v1/set')
    rep_3 = json.loads(set_info.data.decode('utf-8'))

    assert rep_3.get('semester') == 1
    assert rep_3.get('year') == 2
