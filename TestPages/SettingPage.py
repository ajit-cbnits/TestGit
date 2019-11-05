from TestPages.logInPage import LogInPage
from TestPagesLocators.TestPageLocators import Locator
from UserTestData.UserTestDataVar import TestData
import time


class Setting():

    def __init__(self, driver):
        self.driver = driver


    def clickOnSetting(self):

        login = LogInPage(self.driver)
        login.logIn_to_I2chain(TestData.userValidEmail, TestData.userValidPass)
        time.sleep(10)
        self.driver.find_element(*Locator.imageButton).click()
        time.sleep(5)
        self.driver.find_element(*Locator.settingOption).click()
        time.sleep(8)

#Google drive methods and locator binding

    def clickOnGdriveButton(self):
        self.driver.find_element(*Locator.googleDriveButton).click()
        time.sleep(10)

    def enterGDriveEmail(self,userEmail):
        self.driver.find_element(*Locator.googledriveEmail).send_keys(userEmail)
#        time.sleep(5)

    def clickOnUserNextButton(self):
        self.driver.find_element(*Locator.GdriveUserNextButton).click()
#        time.sleep(10)

    def enterGDrivePassword(self,userPass):
        self.driver.find_element(*Locator.googledrivePass).send_keys(userPass)
#        time.sleep(5)

    def clickOnPassNextButton(self):
        self.driver.find_element(*Locator.GdrivePassNextButton).click()
#        time.sleep(10)


    def clickOnAdvanceLink(self):
        self.driver.find_element(*Locator.advanceLink).click()


    def clickOnI2chainUnsafeLink(self):
        self.driver.find_element(*Locator.goToI2chainInfoUnsafe).click()

    def clickOnAllowButton(self):
        self.driver.find_element(*Locator.AllowButton).click()


    def clickOnGDriveLogOutButton(self):
        self.driver.find_element(*Locator.GDriveLogOutButton).click()


    def clickOnGdriveLogOutyesButton(self):
        self.driver.find_element(*Locator.GDriveLogoutYesButton).click()

#One drive methods and locator binding below

    def clickOnOnedriveButton(self):
        self.driver.find_element(*Locator.OneDriveButton).click()
        time.sleep(10)

    def clickonedriveUserNextButton(self):
        self.driver.find_element(*Locator.OneDriveUserNextButton).click()

    def oneDrivePassword(self,userPass):
        self.driver.find_element(*Locator.OneDrivePass).send_keys(userPass)

#Drop box methods and element binding

    def clickDropBoxButton(self):
        self.driver.find_element(*Locator.DropBoxButton).click()

    def clickOnSignWithGoogle(self):
        self.driver.find_element(*Locator.signWithGoogle).click()

    def enterDropBoxEmailID(self, userEmail):
        self.driver.find_element(*Locator.googledriveEmail).send_keys(userEmail)

    def clickOnDropBoxUserNextButton(self):
        self.driver.find_element(*Locator.NextButtonEmail).click()

    def enterDropBoxPassword(self,userPassword):
        self.driver.find_element(*Locator.dropBoxPassword).send_keys(userPassword)

    def clickOnDropBoxPassNextButton(self):
        self.driver.find_element(*Locator.dropBoxNextButtonPass).click()

    def clickOnDropBoxLogOutButton(self):
        self.driver.find_element(*Locator.dropBoxLogOutButton).click()

