"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    b = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    b.implicitly_wait(10)
    yield b
    b.quit()
