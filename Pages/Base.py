from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, browser):
        self.browser = browser
