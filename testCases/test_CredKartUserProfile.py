import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects import LoginPage
from pageObjects.LoginPage import LoginPageClass
from pageObjects.RegistrationPage import RegistrationClass
from utilities.readConfigFile import Readconfig
from utilities.Logger import LogGenerator


# from folder_name.filename import class_name

@pytest.mark.usefixtures("setup")
class Test_UserProfile:
    UserEmail = Readconfig.getUserEmail()  # UserEmail = Credencetest@test.com
    Password = Readconfig.getPassword()
    log = LogGenerator.loggen()

    def test_UserLogin001(self, setup):
        # self.log.debug("This is debug")
        # self.log.info("This is Info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        # Open browser
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # # Go to Url
        # driver.get("https://automation.credence.in/login")
        # this is the fixture captured from conftest
        self.log.info("Testcase test_UserLogin001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        # imported page object class
        self.lp = LoginPageClass(self.driver)
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.lp.Enter_Username(self.UserEmail)  # hard code values replace
        self.log.info(" Entering Username-->" + self.UserEmail)
        # print("UserEmail-->"+ self.UserEmail)
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.lp.Enter_Password(self.Password)
        self.log.info(" Entering Password-->" + self.Password)
        # print("Password-->" + self.Password)
        # Click Login button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.lp.Click_LoginButton()
        self.log.info("Click on login button")
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Login TestCase is Passed")
        # except:
        #     print("Login TestCase is Failed")
        if self.lp.Validate_Status() == "Testcase passed":
            self.log.info("Testcase test_UserLogin001 is passed")
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserLogin001_Pass.png")
            assert True
        else:
            self.log.info("Testcase test_UserLogin001 is Failed")
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserLogin001_Fail.png")
            assert False
        self.log.info("Testcase test_UserLogin001 is completed")

    def test_UserRegistration002(self, setup):
        # # 1 Open Browser
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # # 2 Go to Url
        self.driver = setup
        self.rp = RegistrationClass(self.driver)
        self.driver.get("https://automation.credence.in/register")
        # 3 Enter Name
        # self.driver.find_element(By.ID, "name").send_keys("Credence")
        self.rp.Enter_Name("Credence")
        # 5 Enter Email
        # self.driver.find_element(By.ID, "email").send_keys("Credence_tpest@test.com")
        email = Generate_Email()
        self.rp.Enter_Email(email)
        print(email)
        # 6 Enter Password
        # self.driver.find_element(By.NAME, "password").send_keys("Credence@123")
        self.rp.Enter_Password("Credence@123")
        # 7 Enter Confirm Password
        # self.driver.find_element(By.NAME, "password_confirmation").send_keys("Credence@123")
        self.rp.Enter_ConfirmPassword("Credence@123")
        # 8 Click Register button
        # self.driver.find_element(By.CLASS_NAME, "btn").click()
        self.rp.Click_RegisterButton()
        # Verify Registration status # page.title # success message
        # a= driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        # print(a)
        # # if  a == "CredKart" :
        # #     print("Registration TestCase is Passed")
        # # else:
        # #     print("Registration TestCase is Failed")

        # try:
        #     a = self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']").text
        #     print("Registration TestCase is Passed")
        # except:
        #     print("Registration TestCase is Failed")
        self.lp = LoginPageClass(self.driver)
        if self.lp.Validate_Status() == "Testcase passed":
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserRegistration002_pass.png")
            assert True
        else:
            self.driver.save_screenshot("F:\\Pycharm projects\\Credkart_pytest1\\Screenshots\\test_UserRegistration002_fail.png")
            # "D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jan 24\Credkart_Pytest\Screenshots"
            assert False


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))  # random 4 char lower case e.g gfhd
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])  #
    return f"{username}@{domain}"  # random 4 char + domain

# pytest -v -s --html=HtmlReports/report.html -n=2 --browser firefox

# command liner --> info --broswer
# --broswer --> chrome, firefox, edge
# common values
#
# 12,1,2,3,6 6:30
# 30 --> 30 unit
# 1 day - 1 unit
# 10 day --> 1 day --> 3 unit
# 1 day --> 6 unit --> 4 unit
# 1 night --> 4 unit
# Time schedule # 12th fail--> stop watch timer


# 7am to 10am


# jenkins
# git
# allure
# 3 candidates
