import requests

BASE_URL = "http://localhost:5000"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "OK"

def test_add():
    r = requests.get(f"{BASE_URL}/add/2/3")
    assert r.json()["result"] == 5
