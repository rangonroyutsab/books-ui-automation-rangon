import pytest

from utils.config import Config


@pytest.fixture
def base_url():
    return Config.BASE_URL


@pytest.fixture(autouse=True)
def set_default_timeout(page):
    page.set_default_timeout(Config.TIMEOUT)