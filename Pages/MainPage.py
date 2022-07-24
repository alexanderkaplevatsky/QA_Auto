
from selenium.webdriver.common.by import By
from Pages import BasePage


class SearchPage(BasePage):
    browser = ""

    INPUT_TEXT = (By.ID, 'username')
    GO_BUTTON = (By.CLASS_NAME, 'submit')
    REPO_AMOUNT_TEXT = (By.CLASS_NAME, 'repo-amount')
    CPYTHON_LABEL = (By.XPATH, "//*[contains(text(), 'cpython')]")


    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def enter_serch(self, text):
        searchtext = self.browser.find_element(*self.INPUT_TEXT)
        searchtext.send_keys(text)

    def click_button(self):
        searchtext = self.browser.find_element(*self.GO_BUTTON)
        searchtext.click()

    def verify_found_repos(self):
        repoamount = self.browser.find_element(*self.REPO_AMOUNT_TEXT)
        repoamount.screenshot("./screenshots/repositories.png")
        assert "Found" in repoamount.text
        assert "Repos" in repoamount.text

    def verify_cpython_repo(self):
        repocpython = self.browser.find_element(*self.CPYTHON_LABEL)
        repocpython.screenshot("./screenshots/python_repo.png")
        repocpython.click()
        handles = self.browser.window_handles
        size = len(handles)
        self.browser.switch_to.window(handles[1])
        title = self.browser.title
        assert "python/cpython" in title
