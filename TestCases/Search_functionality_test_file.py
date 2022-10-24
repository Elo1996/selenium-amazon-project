import time
import unittest
from Src.Pages.Search_functionalit_page_file import SearchFuncClass
from TestCases.Base_test_file import BaseTestClass
from Src.Pages.SignIn_page_file import SignInPageClass
from Common.Variables import VariablesClass


class SearchFunctionality(BaseTestClass):
    def setUp(self):
        self.searchPageObj = SearchFuncClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_search_functionality(self):
        # Sign in part
        self.driver.get(VariablesClass.amazonSignInUrl)
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()
        self.signInPageObj.fill_password_field()
        time.sleep(6)
        self.signInPageObj.click_into_sign_in_button()

        # Searching part

        self.searchPageObj.fill_in_search_field()
        self.searchPageObj.click_into_submit_button()

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()