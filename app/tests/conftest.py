from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
