from Common.Custom_find_file import CustomFind
from selenium.webdriver.common.by import By

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)
        self.locators = MainPageLocatorsClass()

    def fill_in_search_field(self, text="Agv Helmet"):
        searchField = self.find.custom_find_element(self.locators.searchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)

    def click_into_submit_button(self):
        submitButton = self.find.custom_find_element(self.locators.submitButton)
        submitButton.click()

class MainPageLocatorsClass():
    searchFieldLocator = (By.ID, "twotabsearchtextbox")
    submitButton = (By.ID, "nav-search-submit-button")