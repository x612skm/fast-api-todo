import pytest
import requests


@pytest.mark.asyncio
async def test_all_todo():
    response = requests.get("http://localhost:8000/api/")
    assert response.status_code == 200
    assert response.text == '"Not Yet"'


@pytest.mark.asyncio
async def test_post_todo():
    response = requests.post("http://localhost:8000/api/")
    assert response.status_code == 200
    assert response.text == '"Not Yet"'


@pytest.mark.asyncio
async def test_put_todo():
    response = requests.put("http://localhost:8000/api/1")
    assert response.status_code == 200
    assert response.text == '"Not Yet"'


@pytest.mark.asyncio
async def test_delete_todo():
    response = requests.delete("http://localhost:8000/api/1")
    assert response.status_code == 200
    assert response.text == '"Not Yet"'

