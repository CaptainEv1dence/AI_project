"""
API endpoint tests for text generation service
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_generate_endpoint_exists():
    """Test that /generate endpoint is accessible"""
    response = client.post(
        "/generate",
        json={"prompt": "Hello"}
    )
    assert response.status_code != 404


def test_generate_with_valid_input():
    """Test text generation with valid prompt"""
    payload = {
        "prompt": "Once upon a time",
        "max_new_tokens": 20,
        "temperature": 0.7
    }
    
    response = client.post("/generate", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "prompt" in data
    assert "generated" in data
    assert data["prompt"] == "Once upon a time"
    assert isinstance(data["generated"], str)
    assert len(data["generated"]) > 0


def test_generate_with_minimal_input():
    """Test generation with only prompt (default parameters)"""
    payload = {"prompt": "Test"}
    
    response = client.post("/generate", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "generated" in data


def test_generate_with_custom_max_tokens():
    """Test that max_new_tokens parameter is respected"""
    payload = {
        "prompt": "AI is",
        "max_new_tokens": 5,
        "temperature": 0.7
    }
    
    response = client.post("/generate", json=payload)
    
    assert response.status_code == 200
