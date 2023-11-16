import httpx
import pytest


@pytest.mark.asyncio
async def test_get_form_contact():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://web:80/get_form",
            json={
                "user_email": "johndoe@example.com",
                "user_phone": "+7 234 567 88 89"
            }
        )
        assert response.status_code == 200
        assert "application/json" in response.headers["content-type"]
        assert response.json().get("template_name") == "ContactForm"


@pytest.mark.asyncio
async def test_get_form_registration():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://web:80/get_form",
            json={
                "user_name": "John Doe",
                "user_email": "johndoe@example.com",
                "phone": "+7 234 567 88 89"
            }
        )
        assert response.status_code == 200
        assert "application/json" in response.headers["content-type"]

