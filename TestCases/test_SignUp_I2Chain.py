'''
Created on 05-Aug-2019

@author: NITS-D061
'''
import unittest
import logging
from selenium import webdriver
from TestBaseSetUp.Variable import ConifigVariable
from TestPages.SignUpPage import SignUpPage
import time
from UserTestData.UserTestDataVar import TestData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Utils.UtilityMethods import UtilsMethods


class SignUpTest(unittest.TestCase):
    
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
        

    def test_Registered_User_SignUp(self):
        
        signUp = SignUpPage(self.driver)
        signUp.click_Create_Account()
        time.sleep(2)
        logging.info("*******Testing signUp page********")
        signUp.enter_First_Name(TestData.AFirstname)
        logging.info("********Entering first Name*********")
        signUp.enter_Last_Name(TestData.AlastName)
        logging.info("********Entering Last Name*********")
        signUp.enter_Email_Address(TestData.AemailId)
        logging.info("********Entering Email Id *********")
        signUp.enter_Password(TestData.Apassword)
        logging.info("********Entering password*********")
        signUp.enter_confirm_Password(TestData.AconfirmPassword)
        logging.info("********Entering Confirm Password*********")
        signUp.click_On_Create_Button()
        time.sleep(5)
        
        alreadyRegisteredUserAlert =WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
            (By.XPATH,"//div[@class='alert alert-danger alert-dismissible fade show']")))

        
        logging.info(alreadyRegisteredUserAlert.text)
        
        text = "An account with the given email already exists."
        
        if text in alreadyRegisteredUserAlert.text:
        
            logging.info("**********sign up with already registered user email address PASS*************")
            print("User already registered")
         
        else:
            
            logging.info("User not registered")
            
            
            
                
    def test_New_SignUp(self):
            
        signUp = SignUpPage(self.driver)
        signUp.click_Create_Account()
        time.sleep(2)
        logging.info("*******Testing signUp page********")
        signUp.enter_First_Name(TestData.NfirstName)
        logging.info("********Entering first Name*********")
        signUp.enter_Last_Name(TestData.NlastName)
        logging.info("********Entering Last Name*********")

        RandomEmail = UtilsMethods.randomEmailId()+"@"+"yopmail.com"
        print(RandomEmail)
        logging.info(RandomEmail)
        signUp.enter_Email_Address(RandomEmail)
        logging.info("********Entering Email Id *********")
        signUp.enter_Password(TestData.Npassword)
        logging.info("********Entering password*********")
        signUp.enter_confirm_Password(TestData.NconfirmPassword)
        logging.info("********Entering Confirm Password*********")
        signUp.click_On_Create_Button()
        time.sleep(6)
            
        try:   
            time.sleep(5)
            logging.info("*********new user found for registration************")

            textSucessMessage = self.driver.find_element(By.XPATH, "//h5[@class='fs-16 mt-3']")
            print(textSucessMessage.text)

            if self.assertEqual(textSucessMessage.text,"A verification email has been sent to your registered email id. Please verify your email."):

                logging.info(textSucessMessage.text)
                print("User registered successfully")
                logging.info("********User registered successfully********")
                
            else:
                logging.info("*******Test case Failed********")
                       
        except:
            
                raise Exception("test case failed")
                logging.info("*******Test cases failed*****")
    
    def tearDown(self):
      
        self.driver.close()
        logging.info("*****************driver closing************")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()