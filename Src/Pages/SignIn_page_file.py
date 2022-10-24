from Common.Custom_find_file import CustomFind
from selenium.webdriver.common.by import By
from Common.Variables import VariablesClass
from Src.Pages.Base_page_file import BasePageClass

class SignInPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)
        self.locators = SignInPageLocatorsClass()

    def fill_username_field(self, userName="elen.hakobyan96@gmail.com"):
        userNameTextBoxElement = self.find.custom_find_element(self.locators.userNameTextFieldLocator)
        userNameTextBoxElement.send_keys(userName)

    def click_into_continue_button(self):
        continueButtonElement = self.find.custom_find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password="Elen*1996"):
        passwordTextBoxElement = self.find.custom_find_element(self.locators.passwordTextFieldLocator)
        passwordTextBoxElement.send_keys(password)

    def click_into_sign_in_button(self):
        signInButtonElement = self.find.custom_find_element(self.locators.signInButtonLocator)
        signInButtonElement.click()

    def check_to_keep_me_signed_in_checkbox(self):
        keepMeSignedInElement = self.find.custom_find_element(self.locators.keepMeSignedInLocator)
        keepMeSignedInElement.click()


class SignInPageLocatorsClass():
    #Username Part
    userNameTextFieldLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")

    #Password Part
    passwordTextFieldLocator = (By.ID, "ap_password")
    signInButtonLocator = (By.ID, "signInSubmit")
    keepMeSignedInLocator = (By.NAME, "rememberMe")