import time
import unittest
import random

from selenium import webdriver
from Common.Variables import VariablesClass
from Src.Pages.SignIn_page_file import SignInPageClass
from Src.Pages.Edit_profile_name_page_file import EditProfileNamePageClass
from webdrivermanager.chrome import ChromeDriverManager
from TestCases.Base_test_file import BaseTestClass

class EditProfileName(BaseTestClass):
    def setUp(self):
        self.signInPageObj = SignInPageClass(self.driver)
        self.editProfileNameObj = EditProfileNamePageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        #Sign in Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()
        self.signInPageObj.fill_password_field()
        time.sleep(3)
        self.signInPageObj.click_into_sign_in_button()

        #Account part
        self.editProfileNameObj.click_on_account_section()
        self.editProfileNameObj.go_to_your_profiles_section()
        time.sleep(3)
        self.editProfileNameObj.open_active_profile()
        self.editProfileNameObj.click_on_edit_icon()
        self.editProfileNameObj.clear_profile_name_field()
        self.editProfileNameObj.fill_random_name()
        self.editProfileNameObj.click_on_save_changes_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()
