import time
import unittest

from selenium import webdriver
from Common.Variables import VariablesClass
from Src.Pages.SignIn_page_file import SignInPageClass
from webdrivermanager.chrome import ChromeDriverManager
from TestCases.Base_test_file import BaseTestClass

class SignIn(BaseTestClass):
    def setUp(self):
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get(VariablesClass.amazonSignInUrl)
        #Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        #Password Part
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        #This Sleep Should not be there but we add becose Amazon detect that it is a Robot
        time.sleep(6)
        self.signInPageObj.click_into_sign_in_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()