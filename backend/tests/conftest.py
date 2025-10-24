"""
Pytest configuration and shared fixtures
"""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    """Create a test client for the FastAPI app"""
    from backend.main import app
    return TestClient(app)
