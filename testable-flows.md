The main functionality of the application is to retrieve students' repositories based on search.
Thus, the search has to work and if a valid search term is entered, a list of valid repositories has to be shown.
Clicking on the repository link should open a valid GitHub repository with that name.

Top two scenarios:

1. Enter a valid search item, like "Python". Clicking on the "Go" button should show a text message with "Found" 
   and "Repos" in it. (Clicking "Enter" is a similar test not currently implemented.)
2. Click on one of the links retrieved in step 1 that contains a word "Cpython". If it's a valid
   link, a new tab should open up that will be a GitHub repository with a title "python/cpython".

Other scenarios:

1. Verify that acceptance criteria on the UI elements are met:
   a. Search form is present
   b. Header is present and contains text "Get Github Repos"
   c. Search button is present and is functional.
   d. "GitHub Username" label is present.

2. A text can be entered into the text box. Clicking go button or hitting "Enter" will start search.
3. When search has found valid repositories the results are displayed as a list with links to the 
   repositories on the left and description on the right. A label under the search form shows how many repositories 
   were found.
4. When a search was performed and no repositories were found the label shows "No Repos" and the list 
   is blank.
5. 
6. 
