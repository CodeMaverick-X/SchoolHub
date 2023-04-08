#!/usr/bin/python3
"""tests for event routes"""

import json

def test_event_get(client):
    """test the get event route"""
    username = "reinhardC"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    response2 = client.get('api/v1/events')
    rep = json.loads(response2.data.decode('utf-8'))

    assert len(rep) == 35

def test_event_put(client):
    """test the put event route"""
    username = "reinhardD"
    password = "super_secrete"
    response1 = client.post("/register", data={"username": username, "password": password})

    event_info = {'name': 'Read', 'tag': 'MON_8-10'}

    response2 = client.put('api/v1/events', data=event_info)

    assert response2.status_code == 200

    response3 = client.get('api/v1/events')
    rep = json.loads(response3.data.decode('utf-8'))

    c_evnt = [event for event in rep if event.get('tag') == 'MON_8-10'][0]
    assert c_evnt.get('name') == 'Read'
