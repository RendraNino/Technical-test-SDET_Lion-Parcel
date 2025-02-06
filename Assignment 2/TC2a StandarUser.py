# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAsStandarUser():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_asStandarUser(self):
    # Test name: As Standar User
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.saucedemo.com/")
    # 2 | setWindowSize | 1296x696 | 
    self.driver.set_window_size(1296, 696)
    # 3 | click | css=*[data-test="login-credentials"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-credentials\"]").click()
    # 4 | click | css=*[data-test="username"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    # 5 | type | css=*[data-test="username"] | standard_user
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    # 6 | click | css=*[data-test="login-password"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-password\"]").click()
    # 7 | click | css=*[data-test="password"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    # 8 | type | css=*[data-test="password"] | secret_sauce
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    # 9 | click | css=*[data-test="login-button"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    # 10 | click | css=*[data-test="add-to-cart-sauce-labs-backpack"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    # 11 | click | css=*[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    # 12 | click | css=*[data-test="shopping-cart-link"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    # 13 | click | css=*[data-test="continue-shopping"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue-shopping\"]").click()
    # 14 | click | css=*[data-test="add-to-cart-sauce-labs-onesie"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    # 15 | click | css=*[data-test="shopping-cart-link"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    # 16 | click | css=*[data-test="remove-sauce-labs-backpack"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
    # 17 | click | css=*[data-test="checkout"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    # 18 | click | css=*[data-test="firstName"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    # 19 | click | css=*[data-test="firstName"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    # 20 | type | css=*[data-test="firstName"] | Re
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Re")
    # 21 | click | css=*[data-test="lastName"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
    # 22 | click | css=*[data-test="firstName"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    # 23 | type | css=*[data-test="firstName"] | Rendra
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Rendra")
    # 24 | type | css=*[data-test="lastName"] | Dwi Pranoto
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("Dwi Pranoto")
    # 25 | click | css=*[data-test="postalCode"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    # 26 | type | css=*[data-test="postalCode"] | 40125
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("40125")
    # 27 | click | css=form | 
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    # 28 | click | css=*[data-test="continue"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    # 29 | click | css=*[data-test="finish"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    # 30 | click | css=*[data-test="back-to-products"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
  
