import pytest
import fastapi


# from http import AsyncClient
import sys

from api.api import api

client = fastapi.testclient.TestClient(api)


# we test if the API works and the get operation send the good result
def test_get_customer(create_db):
    response = client.get(
        "/customer/{id}".format(1)
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == [["marie"]]
