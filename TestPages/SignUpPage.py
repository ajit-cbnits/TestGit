'''
Created on 05-Aug-2019

@author: NITS-D061
'''
from TestPagesLocators.TestPageLocators import Locator
import time



class SignUpPage():

    def __init__(self, driver):
        self.driver = driver

    def click_Create_Account(self):
        self.driver.find_element(*Locator.createAccountLink).click()
        time.sleep(5)

    def enter_First_Name(self, UserName):
        self.driver.find_element(*Locator.firstName).send_keys(UserName)

    def enter_Last_Name(self, LastName):
        self.driver.find_element(*Locator.lastName).send_keys(LastName)

    def enter_Email_Address(self, emailId):
        self.driver.find_element(*Locator.emailAddress).send_keys(emailId)

    def enter_Password(self, passWord):
        self.driver.find_element(*Locator.password).send_keys(passWord)

    def enter_confirm_Password(self, confirmPass):
        self.driver.find_element(*Locator.confirmPassword).send_keys(confirmPass)

    def click_On_Create_Button(self):
        self.driver.find_element(*Locator.CreateButton).click()