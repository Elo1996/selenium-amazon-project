import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Common.Variables import VariablesClass
from Src.Pages.SignIn_page_file import SignInPageClass
from Src.Pages.Add_items_to_cart_page_file import AddItemsToCartPageClass
from webdrivermanager.chrome import ChromeDriverManager
from Src.Pages.SignIn_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Search_functionalit_page_file import SearchFuncClass


class AddItems(BaseTestClass):
    def setUp(self):
        self.addItemsPageObj = AddItemsToCartPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)
        self.searchPageObj = SearchFuncClass(self.driver)

    def test_amazon_add_items(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        time.sleep(2)

        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        # Password Part
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        time.sleep(2)
        self.signInPageObj.click_into_sign_in_button()

        # Searching part
        self.searchPageObj.fill_in_search_field()
        self.searchPageObj.click_into_submit_button()

        # select & add first item
        self.addItemsPageObj.select_item()
        self.addItemsPageObj.add_to_cart()

        # back to previous page with back()
        self.driver.back()

        # select & add second item
        self.addItemsPageObj.second_item_select()
        self.addItemsPageObj.add_to_cart()

        time.sleep(2)

    def tearDown(self):
        self.driver.close()
