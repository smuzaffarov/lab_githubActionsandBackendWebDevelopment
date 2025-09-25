from DifferentExpressionsNumbers import app
import pytest


@pytest.fixture()
def client():
    return app.test_client()

def test_divide(client):
    response = client.get("/divide/10/2")
    assert b"Here is your quotient: 5.0" in response.data

def test_divide_fail(client):
    response = client.get("/divide/10/2")
    assert b"Here is your quotient: 10000" in response.data

devision = [(a,b, a/b) for a in range(1, 100) for b in range (1, 100)]

@pytest.mark.parametrize("a,b,expected", devision)
def testDevisionParametrize(client, a, b, expected):
    response = client.get(f"/divide/{a}/{b}")
    assert f"Here is your quotient: {expected}".encode() in response.data


devisionByZero = [(a, 0) for a in range(1, 10)]

@pytest.mark.parametrize("a,b", devisionByZero)
def testDevisionByZeroParametrize(client, a, b):
    response = client.get(f"/divide/{a}/{b}")
    assert b"Error: division by zero" in response.data





