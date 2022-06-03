import json
import pytest

def test_create_stock_entry(client):
    data = {"count":10}
    response = client.post("/stock",json.dumps(data))
    assert response.status_code == 201 
    assert response.json()["count"] == 10
    
def test_create_stock_entry_invalid(client):
    data = {"count":-1}
    response = client.post("/stock",json.dumps(data))
    assert response.status_code == 400
    
def test_update_stock_entry_invalid_count(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    data2 = {"count":-1}
    response = client.put("/stock/1",json.dumps(data2))
    assert response.status_code == 400
    
def test_update_stock_entry_invalid_id(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    
    data2 = {"count":10}
    response = client.put("/stock/5",json.dumps(data2))
    assert response.status_code == 404
 
@pytest.mark.asyncio   
async def test_update_stock_entry(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    
    data2 = {"count":20}
    data3 = {"count":30}
    response1 = await client.put("/stock/1",json.dumps(data2))
    response2 = await client.put("/stock/1",json.dumps(data3))
    
    assert response1.status_code == 200
    assert response1.json()['count'] == 20
    
    assert response2.status_code == 200
    assert response2.json()['count'] == 30
        
def test_purchase_stock_entry_invalid_id(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    
    data2 = {"count":10}
    response = client.put("/stock/5/purchase",json.dumps(data2))
    assert response.status_code == 404
    
def test_purchase_stock_entry_invalid_id(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    
    data2 = {"count":1}
    response = client.put("/stock/1/purchase",json.dumps(data2))
    assert response.status_code == 200
    assert response.json()['count'] == 9
    
@pytest.mark.asyncio   
async def test_update_stock_entry(client):
    data = {"count":10}
    client.post("/stock",json.dumps(data))
    
    data2 = {"count":3}
    data3 = {"count":2}
    response1 = await client.put("/stock/1/purchase",json.dumps(data2))
    response2 = await client.put("/stock/1/purchase",json.dumps(data3))
    
    assert response1.status_code == 200
    assert response1.json()['count'] == 7
    assert response2.status_code == 200
    assert response2.json()['count'] == 5
    
    

    
