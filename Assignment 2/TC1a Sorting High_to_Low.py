Feature: Shopping Cart Functionality

Scenario: Product on Inventory Sorting After User click Filter
    Title: Ensure the Product sort Descending prices High to Low

    Precondition:
        - Already open https://www.saucedemo.com web page
        - Already registered an account
        - Already logged in

    Steps:
        Enter a valid username as standard_user
		Enter a valid password
		Given I am on the homepage of the website
        When I sort for a product, such as "Price (High to Low)"

    Actual Result:
        The product is Descending Price (High to Low)	

    Expected Result:
        Display sorted Products as Descending Price (High to Low)

Test Date:
Status: (Open)
Error Category: (Low)
Evidence : *screenshot*