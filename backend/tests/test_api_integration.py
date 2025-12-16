# This is the unit test file for the files and stuff

"""
Title: test_api_integration.py
Purpose: performing integration tests on Flask API endpoints woo wee
"""
import os
import multiprocessing
import time
import requests
import pytest
from main import create_app # The main.py file.

test_port = os.getenv("test_port", "5000")
base_url = f"http://127.0.0.1:{test_port}"
app = create_app()

def run_server():
    """Helper function to start Flask app (used for Windows-safe multiprocessing)."""
    app.run(port=5000)


@pytest.fixture(scope="session", autouse=True)
def start_test_server():
    """Start Flask app once in background for all tests (Windows-compatible)."""
    server = multiprocessing.Process(target=run_server)
    server.start()
    time.sleep(1)  # Give it a moment to start

    yield

    server.terminate()
    server.join()


base_url = "http://127.0.0.1:5000"
TIMEOUT = 5

# ------------------------------
# Root endpoint test
# ------------------------------

def test_home_endpoint():
    """Make a successful connection."""
    response = requests.get(f"{base_url}/", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Marketplace API is running successfully"

# ------------------------------
# Items endpoints
# ------------------------------

def test_get_items():
    """Check that item listings are set properly."""
    response = requests.get(f"{base_url}/api/items", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert {"id", "name", "price"}.issubset(data[0].keys())

def test_get_item_by_id():
    """Try grabbing an item by it's ID."""
    response = requests.get(f"{base_url}/items/101", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 101
    assert "name" in data

def test_add_item():
    """Try adding an item."""
    new_item = {"id": 200, "name": "Keyboard", "price": 49.99}
    response = requests.post(f"{base_url}/api/add_item", json=new_item, timeout=TIMEOUT)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Item added successfully"
    assert data["item"] == new_item

def test_get_item_invalid_id():
    """Requesting a non-existent item should return 404."""
    response = requests.get(f"{base_url}/items/999999", timeout=TIMEOUT)
    assert response.status_code == 404

def test_add_item_missing_fields():
    """Adding an item with missing fields should fail."""
    incomplete_item = {"id": 201, "name": "Mouse"}
    response = requests.post(f"{base_url}/items", json=incomplete_item, timeout=TIMEOUT)
    assert response.status_code == 400

def test_add_duplicate_item():
    """Adding an item with an existing ID should fail."""
    duplicate_item = {"id": 101, "name": "Mouse", "price": 29.99}
    response = requests.post(f"{base_url}/items", json=duplicate_item, timeout=TIMEOUT)
    assert response.status_code == 400

# ------------------------------
# User endpoints
# ------------------------------

def test_get_users():
    """Try getting users information."""
    response = requests.get(f"{base_url}/api/users", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert {"id", "name", "email"}.issubset(data[0].keys())

def test_login_success():
    """Try login method."""
    payload = {"username": "admin", "password": "123"}
    response = requests.post(f"{base_url}/api/login", json=payload, timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Login successful"
    assert "token" in data

def test_login_failure():
    """Make sure login method can fail."""
    payload = {"username": "wrong", "password": "bad"}
    response = requests.post(f"{base_url}/login", json=payload, timeout=TIMEOUT)
    assert response.status_code == 401
    data = response.json()
    assert data["message"] == "Invalid credentials"

def test_login_empty_payload():
    """Login endpoint should fail if payload is empty."""
    response = requests.post(f"{base_url}/login", json={}, timeout=TIMEOUT)
    assert response.status_code == 400

def test_login_sql_injection():
    """Ensure login endpoint is resistant to SQL injection."""
    payload = {"username": "' OR '1'='1", "password": "anything"}
    response = requests.post(f"{base_url}/login", json=payload, timeout=TIMEOUT)
    assert response.status_code == 401
