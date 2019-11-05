import logging
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestBaseSetUp.Variable import ConifigVariable
from TestPages.SettingPage import Setting
from UserTestData.UserTestDataVar import TestData


class DropBoxConnTest(unittest.TestCase):
    logging.basicConfig(filename="../LoggerReport/report.log",
                        format='%(asctime)s - %(message)s',
                        level=logging.DEBUG,
                        filemode='w')

    def setUp(self):
        self.driver = webdriver.Chrome(ConifigVariable.chromePathWin)
        print("Chrome driver opened for testing dropBox conn test")
        self.driver.maximize_window()
        logging.info("Browser launched and maximize")
        print("Chrome browser launched and maximized")
        self.driver.get(ConifigVariable.StaggingURL)
        logging.info("I2chain Application Opened")
        print("i2chain application running in backend")

    def testDropBoxCon(self):
        setting = Setting(self.driver)
        logging.info("=========Setting page initialized=====")
        print("setting page initialised")
        window_before = self.driver.window_handles[0]
        setting.clickOnSetting()
        print("clicked on setting")
        time.sleep(5)
        setting.clickDropBoxButton()
        time.sleep(10)
        window_After = self.driver.window_handles[1]

        if window_After != window_before:
            self.driver.switch_to_window(window_After)
            logging.info("getting window details" + window_After)
            print("new window found for dropBox connection user need to provide credentials")
            setting.clickOnSignWithGoogle()
            self.driver.implicitly_wait(40)
            setting.enterDropBoxEmailID(TestData.setUserName)
            time.sleep(10)
            logging.info("==entering gmail user name ==")
            print("entering drop box user name")
            setting.clickOnDropBoxUserNextButton()
            time.sleep(10)
            logging.info("==Clicking on next button==")
            print("==clicking on next button==")
            setting.enterDropBoxPassword(TestData.dropBoxPass)
            logging.info("==Entering gmail password==")
            print("entering gmail password")
            time.sleep(5)
            setting.clickOnDropBoxPassNextButton()
            time.sleep(15)

            self.driver.switch_to_window(window_before)

            dropBoxSucMessage = WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//div[@class='alert alert-success alert-dismissible fade show']")))

            logging.info(dropBoxSucMessage.text)

            text = "Successfully connected to dropbox!"

            if text in dropBoxSucMessage.text:
                logging.info("==dropBox drive connected successfully==")
                time.sleep(15)
                setting.clickDropBoxButton()
                logging.info("==clicking on gdrive button for logout connected drive==")
                print("==clicking on gdrive button for logout connected drive==")
                time.sleep(10)
                setting.clickOnDropBoxLogOutButton()
                logging.info("==clicking on logout button to log our==")
                print("==clicking on logout button to log our==")
                time.sleep(10)

                setting.clickOnGdriveLogOutyesButton()
                logging.info("==clicking on yes button==")
                print("==clicking on yes button ==")
                time.sleep(10)

                logoutSuccessMessage = WebDriverWait(self.driver, 30).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, "//div[@class='alert alert-success alert-dismissible fade show']")))

                logging.info(logoutSuccessMessage.text)

                text = "Successfully logout from dropbox!!!"
                if text in logoutSuccessMessage.text:
                    print("==Log Out Successfully=="+text)
                    logging.info("====logout successfully====")

            else:
                logging.info("==========alert Message DoesNot Match drive not connected============")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
