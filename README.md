# QA_Auto
QA Automation Project

This is a project that implements 2 automated tests for GitHub sample application

To install it do the following.

1. Have Python installed on your computer
2. Do git clone of your project into your target folder
3. Install the requirements for this project by running : pip install -r /path/to/requirements.txt

In order to run the tests in the root of this folder run :
pytest tests/test_frontend.py

This will run 2 tests from test_frontend file and save screenshots into the screenshot folder.

If both tests passed you will see this (time will vary):
..                                                                                                                                     [100%]

======================================================================== 2 passed in 9.45s ========================================================================= 

If tests didn't pass you will see exceptions explaining where it failed.

The two tests implemented are (both run on Chrome browser)

1. test_validate_that_search_returns_results. This test performs search for a repository with a word Python in its name. It passes if a repository with the word Python in it was found.
2. test_validate_that_repos_link_works. This test validates that a link to a repository with a word "Python" is functional and it opens a valid repository when clicked.
