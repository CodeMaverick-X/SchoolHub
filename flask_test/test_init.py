def test_home(client):
    response = client.get('/')

    assert b'SchoolHub' in response.data
