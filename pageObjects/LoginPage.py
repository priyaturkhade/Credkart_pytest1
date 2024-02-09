from selenium.webdriver.common.by import By


class LoginPageClass:
    Text_Username_Xpath = "//input[@name='email']"
    Text_Password_ID = "password"
    Click_Login_Button_Xpath = "//button[@type='submit']"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"

    def __init__(self, driver):
        self.driver = driver

    # conftest driver --> mention testcase -- > pageobaject method call -- > driver mentioned testcase it pointing to
    # that driver

    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.Text_Password_ID).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(By.XPATH, self.Click_Login_Button_Xpath).click()

    def Validate_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Validate_Status_Xpath)
            print("TestCase is Passed")
            return "Testcase passed"
        except:
            print("TestCase is Failed")
            return "Testcase Fail"
