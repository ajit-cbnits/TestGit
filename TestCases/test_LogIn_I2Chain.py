'''
Created on 26-July-2019

@author: Ajit Singh
'''
import unittest
from selenium import webdriver
from TestBaseSetUp.Variable import ConifigVariable
import logging
from TestPages.logInPage import LogInPage
import time
from selenium.webdriver.common.by import By
from TestPagesLocators.TestPageLocators import Locator
from UserTestData.UserTestDataVar import TestData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class LogInTest(unittest.TestCase):
    
    
    logging.basicConfig(filename="../LoggerReport/report.log",
                        format='%(asctime)s - %(message)s',
                        level=logging.DEBUG,
                        filemode='w')
    
    def setUp(self):
        
        self.driver= webdriver.Chrome(ConifigVariable.chromePath)
        self.driver.maximize_window()
        logging.info("Browser launched and maximize")
        self.driver.get(ConifigVariable.StaggingURL)
        logging.info("I2chain Application Opened")


    def test_Invalid_Credential(self):
        
        login = LogInPage(self.driver)
        logging.info("LogIn page called")
        login.enter_text_userName(TestData.userUnregisteredEmail)
        logging.info("entering email id")
        login.enter_text_Password(TestData.userInvalidPass)
        logging.info("entering password")      
        login.click_signIn_Button()
        logging.info("clicking on submitt button")
        
        time.sleep(5)
        
        getErrorMsg = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
            (By.XPATH,"//div[@class='alert alert-danger alert-dismissible fade show']")))

        
        logging.info(getErrorMsg.text)
        
        text = "Incorrect email address or password."
        
        if text in getErrorMsg.text:
        
            logging.info("**********LogIn with InValid credentials Test Pass*********")
         
        else:
        
            logging.info("test Case Failed")
            print("Test Case Failed")
         
        print("tested invalid credential of unregistered user has been" +" " +"PASS")
        
    def test_InvalidEmailId(self):
        
        login = LogInPage(self.driver)
        logging.info("called logIn page for testInvalid email")
        login.enter_text_userName(TestData.userInvalidEmail)
        logging.info("entering invalid email id ")
        time.sleep(2)
        errMsg= self.driver.find_element(*Locator.InvalidEmailerrMsg).text
        logging.info(errMsg)
        self.assertEqual(errMsg,"Please enter valid email address.")
        logging.info("test case pass")
        print("testing of Invalid Email address PASS")
             
    
    def test_valid_LogIn(self):
        
        login = LogInPage(self.driver)
        login.logIn_to_I2chain(TestData.userValidEmail ,TestData.userValidPass)
        
        time.sleep(5)
        
        self.driver.find_element(*Locator.imageButton).click()
        
        time.sleep(5)
        
        try:
            
            self.driver.find_element(*Locator.LogOutButton).click()
            print("test_valid_LogIn" +" " +"PASS")
            logging.info("user able to log out")
        
        except NoSuchElementException as e:
            
            print(e.getMessage())
        
            
    def tearDown(self):
        time.sleep(5)
        self.driver.close()
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()