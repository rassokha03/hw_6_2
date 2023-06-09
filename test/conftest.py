import pytest
from selene import browser


@pytest.fixture(scope="class", autouse=True)
def brows_size():
    browser.config.window_width = 1900
    browser.config.window_height = 800