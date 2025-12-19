import pytest
import httpx

API_URL = "http://127.0.0.1:8000"
TEST_USERNAME = "testuser"
TEST_PASSWORD = "testpass"

async def ensure_user_exists(client, username, password):
    """Создаёт пользователя, если его ещё нет"""
    data = {
        "username": username,
        "password": password,
        "email": f"{username}@example.com",
        "name": "Test User"
    }
    response = await client.post(f"{API_URL}/api/register", json=data)
    # Если пользователь уже есть, ничего не делаем
    if response.status_code not in (200, 400):
        raise Exception(f"Unexpected status code during setup: {response.status_code}")
    return response

@pytest.mark.asyncio
async def test_register_existing_user():
    async with httpx.AsyncClient() as client:
        await ensure_user_exists(client, TEST_USERNAME, TEST_PASSWORD)

        # Пробуем зарегистрировать снова
        data = {
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
            "email": f"{TEST_USERNAME}@example.com",
            "name": "Test User"
        }
        response = await client.post(f"{API_URL}/api/register", json=data)

    assert response.status_code == 400
    assert "detail" in response.json()
    assert response.json()["detail"] == "User already exists"

@pytest.mark.asyncio
async def test_login_wrong_password():
    async with httpx.AsyncClient() as client:
        await ensure_user_exists(client, TEST_USERNAME, TEST_PASSWORD)

        data = {
            "username": TEST_USERNAME,
            "password": "wrongpassword",
            "email": f"{TEST_USERNAME}@example.com",
            "name": "Test User"
        }
        response = await client.post(f"{API_URL}/api/login", json=data)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

@pytest.mark.asyncio
async def test_register_and_login():
    async with httpx.AsyncClient() as client:
        await ensure_user_exists(client, TEST_USERNAME, TEST_PASSWORD)

        # Логин
        login_data = {
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
            "email": f"{TEST_USERNAME}@example.com",
            "name": "Test User"
        }
        login_resp = await client.post(f"{API_URL}/api/login", json=login_data)
        assert login_resp.status_code == 200
        token = login_resp.json()["access_token"]
        assert token is not None
