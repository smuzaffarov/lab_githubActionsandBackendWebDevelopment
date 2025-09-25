from DifferentExpressionsNumbers import app
import pytest


@pytest.fixture()
def client():
    return app.test_client()

def test_divide(client):
    response = client.get("/divide/10/2")
    assert b"Here is your quotient: 5.0" in response.data

devision = [(a,b, a/b) for a in range(1, 10) for b in range (1, 10)]

@pytest.mark.parametrize("a,b,expected", devision)
def test_DevisionParametrize(client, a, b, expected):
    response = client.get(f"/divide/{a}/{b}")
    assert f"Here is your quotient: {expected}".encode() in response.data


devisionByZero = [(a, 0) for a in range(1, 10)]

@pytest.mark.parametrize("a,b", devisionByZero)
def test_DevisionByZeroParametrize(client, a, b):
    response = client.get(f"/divide/{a}/{b}")
    assert b"Error: division by zero" in response.data


multiplications = [(a,b, a*b) for a in range(0, 5) for b in range (0, 5)]

@pytest.mark.parametrize("a,b,expected", multiplications)
def test_numberMultiplications(client, a, b, expected):
    response = client.get(f"/multiplication/{a}/{b}")
    assert f"Here is your quotient: {expected}".encode() in response.data




