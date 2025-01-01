from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test case 1: Kiểm tra route /get_version trả về phiên bản đúng
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


# Test case 2: Kiểm tra route /check_prime với số nguyên tố hợp lệ
def test_check_prime_valid_prime():
    response = client.post("/check_prime", json={"number": 7})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

# Test case 3: Kiểm tra route /check_prime với số không phải nguyên tố
def test_check_prime_invalid_prime():
    response = client.post("/check_prime", json={"number": 6})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

# Test case 4: Kiểm tra số 1 không phải là số nguyên tố
def test_check_prime_edge_case_1():
    response = client.post("/check_prime", json={"number": 1})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

# Test case 5: Kiểm tra số âm không phải là số nguyên tố
def test_check_prime_negative():
    response = client.post("/check_prime", json={"number": -5})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

# Test case 6: Kiểm tra số nguyên tố lớn (104729)
def test_check_prime_large_number():
    response = client.post("/check_prime", json={"number": 104729})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

# Test case 7: Kiểm tra số lớn không phải là số nguyên tố
def test_check_prime_large_non_prime():
    response = client.post("/check_prime", json={"number": 104728})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

# Test case 8: Kiểm tra lỗi khi nhập chuỗi thay vì số
def test_check_prime_string_input():
    response = client.post("/check_prime", json={"number": "abc"})
    assert response.status_code == 422  # Unprocessable Entity

# Test case 9: Kiểm tra khi không truyền số vào query
def test_check_prime_no_input():
    response = client.post("/check_prime", json={})
    assert response.status_code == 422  # Unprocessable Entity

# Test case 10: Kiểm tra số 0 không phải là số nguyên tố
def test_check_prime_valid_input_with_zero():
    response = client.post("/check_prime", json={"number": 0})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}
