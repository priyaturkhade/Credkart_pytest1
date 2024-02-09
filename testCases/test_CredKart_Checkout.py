import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutClass
from pageObjects import CheckoutPage
from utilities.Logger import LogGenerator
from utilities.readConfigFile import Readconfig


@pytest.mark.usefixtures("setup")
class Test_Credkart_checkout:
    UserEmail = Readconfig.getUserEmail()  # UserEmail = Credencetest@test.com
    Password = Readconfig.getPassword()
    First_Name = Readconfig.getFirst_Name()
    LastName = Readconfig.getLastName()
    PhoneNo = Readconfig.getPhoneNo()
    Address=Readconfig.getAddress()
    Zip=Readconfig.getZip()
    State=Readconfig.getState()
    Ownername=Readconfig.getOwnername()
    CVV=Readconfig.getCVV()
    card_number01 =Readconfig.getcard_number01()
    card_number02 =Readconfig.getcard_number02()
    card_number03 = Readconfig.getcard_number03()
    card_number04 = Readconfig.getcard_number04()
    log = LogGenerator.loggen()

    def test_UserLogin001(self,setup):
        self.log.info("Testcase test_UserLogin001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        # imported page object class
        self.cp = CheckoutClass(self.driver)
        self.cp.Enter_Username(self.UserEmail)
        self.log.info(" Entering Username-->" + self.UserEmail)
        print("UserEmail-->"+ self.UserEmail)
        self.cp.Enter_Password(self.Password)
        self.log.info(" Entering Password-->" + self.Password)
        print("Password-->" + self.Password)
        # Click Login button
        self.cp.Click_LoginButton()
        self.log.info("Click on login button")
        if self.cp.Validate_Status() == "Testcase passed":
            self.log.info("Testcase test_UserLogin001 is passed")
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserLogin001_Pass.png")
            assert True
        else:
            self.log.info("Testcase test_UserLogin001 is Failed")
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserLogin001_Fail.png")
            assert False
        self.log.info("Testcase test_UserLogin001 is completed")
        self.cp.Click_Productname()
        self.log.info("Click_Productname" )
        self.cp.Click_Addtocart()
        self.log.info("Click_Addtocart")
        self.cp.Click_ProceedtoCheckout()
        self.log.info("Click_ProceedtoCheckout")
        time.sleep(5)
        self.cp.Enter_First_Name(self.First_Name)
        self.log.info(" Entering First_Name-->" + self.First_Name)
        self.log.info(" Entering First_Name-->" + self.First_Name)
        self.cp.Enter_LastName(self.LastName)
        self.log.info(" Entering LastName-->" + self.LastName)
        self.cp.Enter_PhoneNo(self.PhoneNo)
        self.log.info(" Entering PhoneNo-->" + self.PhoneNo)
        self.cp.Enter_Address(self.Address)
        self.log.info(" Entering Address-->" + self.Address)
        self.cp.Enter_Zip(self.Zip)
        self.log.info(" Entering Zip-->" + self.Zip)
        self.cp.Select_State(self.State)
        self.log.info("Entering State-->"+self.State)
        time.sleep(5)
        self.cp.Enter_Ownername(self.Ownername)
        self.log.info("Entering Ownername-->"+ self.Ownername)
        self.cp.Enter_CVV(self.CVV)
        self.log.info("Entering CVV-->" + self.CVV)
        self.cp.Enter_card_number01(self.card_number01)
        self.log.info("Entering card_number01-->" + self.card_number01)
        self.cp.Enter_card_number02(self.card_number02)
        self.log.info("Entering card_number02-->" + self.card_number02)
        self.cp.Enter_card_number03(self.card_number03)
        self.log.info("Entering card_number03-->" + self.card_number03)
        print(self.card_number03)
        self.cp.Enter_card_number04(self.card_number04)
        self.log.info("Entering card_number04-->" + self.card_number04)
        self.cp.Select_Year()
        self.log.info("Select_Year")
        self.cp.Select_Month()
        self.log.info("Select_Month")
        self.cp.Click_Checkout_button()
        self.log.info("Click_Checkout_button")
        time.sleep(5)
        print(self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)

