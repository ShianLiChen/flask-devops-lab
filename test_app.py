from app import app


def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'DevOps' in res.data


def test_motivator():
    client = app.test_client()
    res = client.get('/motivator')
    assert res.status_code == 200
    assert res.data
