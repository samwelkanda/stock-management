import json

def test_create_stock_entry(client):
    data = {"count":10}
    response = client.post("/stock",json.dumps(data))
    assert response.status_code == 201 
    assert response.json()["count"] == 10