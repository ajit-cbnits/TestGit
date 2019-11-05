
from TestPagesLocators.TestPageLocators import Locator
import time

#This is LogIn page having all action methods of logIn page 
class LogInPage():
    
    def __init__(self,driver):
        
        self.driver=driver
    
    def enter_text_userName(self,userName):
        
        self.driver.find_element(*Locator.userNameElement).send_keys(userName)
        
    def enter_text_Password(self,password):
        self.driver.find_element(*Locator.passwordElemenmt).send_keys(password)
    
    def click_signIn_Button(self):
        self.driver.find_element(*Locator.submittButtonElement).click()
        
    
    def logIn_to_I2chain(self,userName,password):
        
        login=LogInPage(self.driver)
        login.enter_text_userName(userName)
        login.enter_text_Password(password)
        login.click_signIn_Button()
        time.sleep(5)
        
       
        
      
        