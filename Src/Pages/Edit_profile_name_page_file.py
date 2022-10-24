from Common.Custom_find_file import CustomFind
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random, string
import names

class EditProfileNamePageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)
        self.locators = EditProfileNamePageLocatorsClass()

    def click_on_account_section(self):
        accountSectionElement = self.find.custom_find_element(self.locators.accountSectionLocator)
        accountSectionElement.click()

    def go_to_your_profiles_section(self):
        yourProfilesSectionElement = self.find.custom_find_element(self.locators.yourProfilesLocator)
        yourProfilesSectionElement.click()

    def open_active_profile(self):
        activeProfileElement = self.find.custom_find_element(self.locators.activeProfileLocator)
        activeProfileElement.click()

    def click_on_edit_icon(self):
        editIconElement = self.find.custom_find_element(self.locators.editIconNameLocator)
        editIconElement.click()

    def clear_profile_name_field(self):
        profileInputFieldElement = self.find.custom_find_element(self.locators.profileNameInputLocator)
        profileInputFieldElement.click()
        profileInputFieldElement.clear()
        profileInputFieldElement.click()


    def fill_random_name(self):
        fillRandomName = self.find.custom_find_element(self.locators.profileNameInputLocator)
        fillRandomName.send_keys(names.get_full_name())

    def click_on_save_changes_button(self):
        saveChangesElement = self.find.custom_find_element(self.locators.saveChangesButtonLocator)
        saveChangesElement.click()



class EditProfileNamePageLocatorsClass():
    accountSectionLocator = (By.XPATH, '//*[@id="nav-link-accountList"]')
    yourProfilesLocator = (By.XPATH, '(//*[@class="a-spacing-none ya-card__heading--rich a-text-normal"])[6]')
    activeProfileLocator = (By.XPATH, '//div[@class="a-column a-span12"]')
    editIconNameLocator = (By.ID, "name-edit-modal-link")
    profileNameInputLocator = (By.ID, "profile-name-text-input")
    saveChangesButtonLocator = (By.CLASS_NAME, "a-button-input")



