Feature: Shopping Cart Functionality

Scenario: Product on Inventory Sorting After User click Filter
    Title: Ensure the Product sort Descending Z to A

    Precondition:
        - Already open https://www.saucedemo.com web page
        - Already registered an account
        - Already logged in

    Steps:
        Enter a valid username as standard_user
		Enter a valid password
		Given I am on the homepage of the website
        When I sort for a product, such as "Name (Z to A)"

    Actual Result:
        The product is Descending Z to A	

    Expected Result:
        Display sorted Products as Descending Z to A

Test Date:
Status: (Open)
Error Category: (Low)
Evidence : *screenshot*