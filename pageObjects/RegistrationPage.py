from selenium.webdriver.common.by import By


class RegistrationClass:
    Text_Name_ID = "name"
    Text_Email_ID = "email"
    Text_Password_Name = "password"
    Text_ConfirmPassword_Name = "password_confirmation"
    CLick_Register_Button_ClassName = "btn"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, Name):
        self.driver.find_element(By.ID, self.Text_Name_ID).send_keys(Name)

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.NAME, self.Text_Password_Name).send_keys(password)

    def Enter_ConfirmPassword(self,confirm_password):
        self.driver.find_element(By.NAME, self.Text_ConfirmPassword_Name).send_keys(confirm_password)

    def Click_RegisterButton(self):
        self.driver.find_element(By.CLASS_NAME, self.CLick_Register_Button_ClassName).click()