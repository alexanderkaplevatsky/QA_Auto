"""Perform health checks on applications in an environment feature tests."""

from Pages import MainPage


def test_validate_that_search_returns_results(browser):
    """Validate that clicking on search button with search text finds repositories."""
    MainPage.SearchPage(browser).load("http://localhost:3000/")
    MainPage.SearchPage(browser).enter_serch("Python")
    MainPage.SearchPage(browser).click_button()
    MainPage.SearchPage(browser).verify_found_repos()

    print("done")


def test_validate_that_repos_link_works(browser):
    """Validate that clicking ona repository link opens a Github page with that repository"""
    print("done")
    MainPage.SearchPage(browser).verify_cpython_repo()

    print("done")
