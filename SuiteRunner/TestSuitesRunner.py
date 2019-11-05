'''
Created on 12-Aug-2019

@author: NITS-D061
'''

   
import unittest

from TestCases.TestDropBoxConnection import DropBoxConnTest
from TestCases.testOneDriveConnection import TestOneDriveConnect
from TestCases.test_LogIn_I2Chain import LogInTest
from TestCases.test_SignUp_I2Chain import SignUpTest
from TestCases.TestGoogleDriveConnection import SettingPageTest
import os
from HTMLRunner import HTMLTestRunner

direct = os.getcwd()

    
#LogIn_Test = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
#SignUp_Test = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
TestGDriveConn = unittest.TestLoader().loadTestsFromTestCase(SettingPageTest)
TestDropBoxConn=unittest.TestLoader().loadTestsFromTestCase(DropBoxConnTest)
#connect_One_Drive=unittest.TestLoader().loadTestsFromTestCase(TestOneDriveConnect)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([TestGDriveConn,TestDropBoxConn])

outfile = open(direct + "\SmokeTest.html", "w")

runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

runner1.run(test_suite)

