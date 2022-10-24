import unittest
from unittest import TestLoader, TextTestRunner, TestSuite
import HtmlTestRunner
from TestCases.SignIn_test_file import SignIn
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Add_items_to_cart_test_file import AddItems
from TestCases.Delete_items_from_cart_test_file import ClearCart
from TestCases.Edit_profile_name_test_file import EditProfileName
class RunnerClass:
    pass
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestCases/Run/Reports'))
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignIn),
        loader.loadTestsFromTestCase(SearchFunctionality),
        loader.loadTestsFromTestCase(AddItems),
        loader.loadTestsFromTestCase(ClearCart),
        loader.loadTestsFromTestCase(EditProfileName)
    ))
    # run test
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
