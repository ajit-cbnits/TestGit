import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestBaseSetUp.Variable import ConifigVariable
from UserTestData.UserTestDataVar import TestData
import logging
from TestPages.SettingPage import Setting
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SettingPageTest(unittest.TestCase):

    logging.basicConfig(filename="../LoggerReport/report.log",
                        format='%(asctime)s - %(message)s',
                        level=logging.DEBUG,
                        filemode='w')

    def setUp(self):
        self.driver = webdriver.Chrome(ConifigVariable.chromePathWin)
        self.driver.maximize_window()
        logging.info("Browser launched and maximize")
        self.driver.get(ConifigVariable.StaggingURL)
        logging.info("I2chain Application Opened")


    def testConnectGoogleDrive(self):
        setting = Setting(self.driver)
        logging.info("=========Setting page initialized=====")
        window_before = self.driver.window_handles[0]
        setting.clickOnSetting()
        time.sleep(10)
        setting.clickOnGdriveButton()
        window_After = self.driver.window_handles[1]

        if window_After != window_before:
            self.driver.switch_to_window(window_After)
            logging.info("getting window details" + window_After)
            print("=========gettinng window details for connect drive===============")
            setting.enterGDriveEmail(TestData.setUserName)
            time.sleep(10)
            logging.info("========entering gmail user name ========")
            print("=============entering gmail user name for google drive connection==========")
            setting.clickOnUserNextButton()
            time.sleep(10)

            logging.info("=======Clicking on next button=========")
            print("================clicking on next button============")
            setting.enterGDrivePassword(TestData.GDrivePassword)
            logging.info("=========Entering gmail password========")
            print("==============entering gmail password===========")
            setting.clickOnPassNextButton()
            time.sleep(15)

            setting.clickOnAdvanceLink()
            time.sleep(15)
            logging.info("===========Clicking on advance button============")
            print("================clicking on advance link for connect GDrive===========")

            setting.clickOnI2chainUnsafeLink()
            print("====clicking on unsafe Link====")
            logging.info("=====clicking on unsafe link to connect with gDrive========")
            time.sleep(20)

            setting.clickOnAllowButton()
            logging.info("=========clicking on allow button========")
            print("======clicking on allow button======")
            time.sleep(15)
            self.driver.switch_to_window(window_before)

            successMessageAlert = WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
            (By.XPATH,"//div[@class='alert alert-success alert-dismissible fade show']")))

            logging.info(successMessageAlert.text)

            text = "Successfully connected to google drive"

            if text in successMessageAlert.text:
                logging.info("========drive connected successfully=======")
                time.sleep(15)
                setting.clickOnGdriveButton()
                logging.info("========clicking on gdrive button for logout connected drive======")
                print("========clicking on gdrive button for logout connected drive======")
                time.sleep(10)
                setting.clickOnGDriveLogOutButton()
                logging.info("=======clicking on logout button to log our======")
                print("=======clicking on logout button to log our======")
                time.sleep(10)

                setting.clickOnGdriveLogOutyesButton()
                logging.info("====clicking on yes button======")
                print("=====clicking on yes button =========")
                time.sleep(10)

                logoutSuccessMessage = WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                        (By.XPATH, "//div[@class='alert alert-success alert-dismissible fade show']")))

                logging.info(logoutSuccessMessage.text)

                text = "Successfully logout from google drive!!!"
                if text in logoutSuccessMessage.text:
                    print("=====Log Out Successfully===")
                    logging.info("====logout successfully====")

            else:
                logging.info("==========alert Message DoesNot Match drive not connected============")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
