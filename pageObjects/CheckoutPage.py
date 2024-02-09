

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutClass:
    Text_Username_Xpath = "//input[@name='email']"
    Text_Password_ID = "password"
    Click_Login_Button_Xpath = "//button[@type='submit']"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"
    Click_Productname_Xpath = "/html/body/div/div[2]/div[3]/div/div/a[2]/h3"
    Click_add_to_cart_Xpath = "//input[@value='Add to Cart']"
    Click_Proceed_to_Checkout_Xpath = "//a[@class='btn btn-success btn-lg']"
    Text_First_Name_Xpath = "//input[@id='first_name']"
    Text_LastName_Xpath = "//input[@id='last_name']"
    Text_PhoneNo_Xpath = "//input[@id='phone']"
    Text_Address_Xpath = "//textarea[@id='address']"
    Text_Zip_Xpath = "//input[@id='zip']"
    Select_State_Xpath = "//select[@id='state']"
    Enter_Ownername_Xpath="//input[@id='owner']"
    Enter_CVV_Xpath="//input[@id='cvv']"
    Select_Year_Xpath="//select[@id='exp_year']"
    Select_Month_Xpath="//select[@id='exp_month']"
    Enter_card_number01_Xpath="//input[@id='cardNumber']"
    Enter_card_number02_Xpath = "//input[@id='cardNumber']"
    Enter_card_number03_Xpath = "//input[@id='cardNumber']"
    Enter_card_number04_Xpath = "//input[@id='cardNumber']"
    Click_Checkout_button_Xpath="//button[@id='confirm-purchase']"

    # # Enter card number\
    # # 5281 0370 4891 6168

    # print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)
    #
    # driver.close()

    def __init__(self, driver):
        self.driver = driver

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

    def Click_Productname(self):
        self.driver.find_element(By.XPATH,self.Click_Productname_Xpath).click()

    def Click_Addtocart(self):
         self.driver.find_element(By.XPATH,self.Click_add_to_cart_Xpath).click()
    def Click_ProceedtoCheckout(self):
        self.driver.find_element(By.XPATH,self.Click_Proceed_to_Checkout_Xpath).click()

    def Enter_First_Name(self,First_Name):
        self.driver.find_element(By.XPATH,self.Text_First_Name_Xpath).send_keys(First_Name)
    def Enter_LastName(self,last_name):
        self.driver.find_element(By.XPATH,self.Text_LastName_Xpath).send_keys(last_name)
    def Enter_PhoneNo(self,phoneno):
        self.driver.find_element(By.XPATH,self.Text_PhoneNo_Xpath).send_keys(phoneno)
    def Enter_Address(self,address):
        self.driver.find_element(By.XPATH,self.Text_Address_Xpath).send_keys(address)
    def Enter_Zip(self,zip):
        self.driver.find_element(By.XPATH,self.Text_Zip_Xpath).send_keys(zip)
    def Select_State(self,state):
        Select(self.driver.find_element(By.XPATH,self.Select_State_Xpath)).select_by_visible_text(state)

    def Enter_Ownername(self,Ownername):
        self.driver.find_element(By.XPATH, self.Enter_Ownername_Xpath).send_keys(Ownername)
    def Enter_CVV(self,CVV):
        self.driver.find_element(By.XPATH, self.Enter_CVV_Xpath).send_keys(CVV)

    def Select_Year(self):
        Select(self.driver.find_element(By.XPATH, self.Select_Year_Xpath)).select_by_index(2)

    def Select_Month(self):
        Select(self.driver.find_element(By.XPATH, self.Select_Month_Xpath)).select_by_index(2)
    def Enter_card_number01(self,card_number01):
        self.driver.find_element(By.XPATH, self.Enter_card_number01_Xpath).send_keys(card_number01)

    def Enter_card_number02(self, card_number02):
        self.driver.find_element(By.XPATH, self.Enter_card_number02_Xpath).send_keys(card_number02)

    def Enter_card_number03(self, card_number03):
            self.driver.find_element(By.XPATH, self.Enter_card_number03_Xpath).send_keys(card_number03)

    def Enter_card_number04(self, card_number04):
                self.driver.find_element(By.XPATH, self.Enter_card_number01_Xpath).send_keys(card_number04)

    def Click_Checkout_button(self):
        self.driver.find_element(By.XPATH, self.Click_Checkout_button_Xpath).click()



