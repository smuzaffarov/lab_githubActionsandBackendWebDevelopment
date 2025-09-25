from DifferentExpressionsNumbers import app
import pytest


@pytest.fixture()
def client():
    return app.test_client()

# Test independent function - divide
def test_divide(client):
    response = client.get("/divide/10/2")
    assert b"Here is your answer: 5.0" in response.data # I think if I use b or .encode it will format it into bytes anyway

# Test functions - divide
devision = [(a,b, a/b) for a in range(1, 10) for b in range (1, 10)]

@pytest.mark.parametrize("a,b,expected", devision)
def test_DevisionParametrize(client, a, b, expected):
    response = client.get(f"/divide/{a}/{b}")
    assert f"Here is your answer: {expected}".encode() in response.data

# Test functions - divide by zero
devisionByZero = [(a, 0) for a in range(1, 10)]

@pytest.mark.parametrize("a,b", devisionByZero)
def test_DevisionByZeroParametrize(client, a, b):
    response = client.get(f"/divide/{a}/{b}")
    assert b"Error: division by zero" in response.data # I feel here it would be easier to use "b" instead .encode

# Test functions - multiplications
multiplications = [(a,b, a*b) for a in range(0, 5) for b in range (0, 5)]

@pytest.mark.parametrize("a,b,expected", multiplications)
def test_numberMultiplications(client, a, b, expected):
    response = client.get(f"/multiplication/{a}/{b}")
    assert f"Here is your answer: {expected}".encode() in response.data


# Test functions - sqroot
sqroot = [(a, a ** 0.5) for a in range(0, 5)]

@pytest.mark.parametrize("a,expected", sqroot)
def test_numberSqRoot(client, a, expected):
    response = client.get(f"/sqrt/{a}")
    assert f"Here is your answer: {expected}".encode() in response.data

# P.S For me (py -m pytest)
