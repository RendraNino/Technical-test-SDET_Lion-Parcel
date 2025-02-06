Feature: Shopping Cart Functionality

Scenario: Product on Inventory Sorting After User click Filter
    Title: Ensure the Product sort Ascending A to Z

    Precondition:
        - Already open https://www.saucedemo.com web page
        - Already registered an account
        - Already logged in

    Steps:
        Enter a valid username as standard_user
		Enter a valid password
		Given I am on the homepage of the website
        When I sort for a product, such as "Name (A to Z)"

    Actual Result:
        The product is Ascending A to Z	

    Expected Result:
        Display sorted Products as Ascending A to Z

Test Date:
Status: (Open)
Error Category: (Low)
Evidence : *screenshot*