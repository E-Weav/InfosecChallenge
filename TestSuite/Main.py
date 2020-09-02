import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InfoSecLogin(unittest.TestCase):

    def setUp(self):
        """Setup chrome browser."""
        #Spins up a chrome browser and maximizes the window.  This will happen for each test case.
        self.driver = webdriver.Chrome("C:\PythonWork\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()

    def test_signin_nav(self):
        """Validates that a user can navigate to the sign in page"""
        self.driver.find_element_by_class_name("login").click()
        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "SubmitCreate"))
            )
            print("Test Passed!  Successful navigation!")
            #Checks that the submit create button appears on the next form in order to validate successful navigation.
        except:
            print("Test Failed!  Page didnt navigate!")
            self.driver.quit()

    def test_new_account(self):
        """Test to validate a user can be created"""
        self.driver.find_element_by_class_name("login").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("email_create").send_keys("tester1@gmail.com")
        self.driver.find_element_by_id("SubmitCreate").click()

        #Inputs an email into the create an account field and clicks the 'Create an account' button

        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "account_creation"))
            )
            #Checks that the personal information box loads
        except:
            print("Test Failed!  Account already exists!")
            self.driver.quit()
            #Returns error if the page doesn't load in 10 seconds

        #Adding personal information of new user
        self.driver.find_element_by_id("id_gender1").click()
        self.driver.find_element_by_id("customer_firstname").send_keys("Eliot")
        self.driver.find_element_by_id("customer_lastname").send_keys("Weaver")
        self.driver.find_element_by_id("email").click()
        self.driver.find_element_by_id("passwd").send_keys("Password1234")
        self.driver.find_element_by_id("firstname").send_keys("Eliot")
        self.driver.find_element_by_id("lastname").send_keys("Weaver")
        self.driver.find_element_by_id("address1").send_keys("1234 North Plateau")
        self.driver.find_element_by_id("city").send_keys("Milwaukee")

        statedrop = self.driver.find_element_by_id("id_state")
        statedrop.send_keys("Wisconsin")
        statedrop.send_keys(Keys.RETURN)
        
        self.driver.find_element_by_id("postcode").send_keys("53202")

        countrydrop = self.driver.find_element_by_id("id_country")
        countrydrop.send_keys("United States")
        countrydrop.send_keys(Keys.RETURN)

        self.driver.find_element_by_id("phone_mobile").send_keys("2623334444")
        self.driver.find_element_by_id("submitAccount").click()

        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "info-account"))
            )
            print("Test Passed! New Account Created!")
            #Checks that the personal information box loads after clicking register
        except:
            print("Test Failed! Account already exists!")
            self.driver.quit()
            #Returns error if the personal information box doesn't load in 10 seconds

    def test_existing_account(self):
        try:
            self.driver.find_element_by_class_name("login").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id("email").send_keys("jigsaw238@hotmail.com")
            self.driver.find_element_by_id("passwd").send_keys("Password123")
            self.driver.find_element_by_id("SubmitLogin").click()

            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "info-account"))
            )
            print("Test Passed!  Successful Sign in!")
        except:
            print("Test Failed!  Unable to Sign in!")

    def test_error_message(self):
        """Validates duplicate email's cannot be used"""
        self.driver.find_element_by_class_name("login").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("email_create").send_keys("adc@gmail.com")
        self.driver.find_element_by_id("SubmitCreate").click()

        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "create_account_error"))
            )
            print("Test Passed!  Error message appeared!")
        except:
            print("Test Failed!  Error message missing!")
            self.driver.quit()

    def tearDown(self):
        """Closes the chrome window at the end of each test."""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()