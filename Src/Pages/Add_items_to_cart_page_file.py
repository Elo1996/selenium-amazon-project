from Common.Custom_find_file import CustomFind
from selenium.webdriver.common.by import By

class AddItemsToCartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)
        self.locators = AddItemsToCartPageLocatorsClass()

    def select_item(self):
        itemSelectElement = self.find.custom_find_element(self.locators.itemSelectLocator)
        itemSelectElement.click()

    def add_to_cart(self):
        addToCartElemenet = self.find.custom_find_element(self.locators.addToCartLocator)
        addToCartElemenet.click()

    def second_item_select(self):
        secondItemElement = self.find.custom_find_element(self.locators.secondItemSelectLocator)
        secondItemElement.click()



class AddItemsToCartPageLocatorsClass():
    itemSelectLocator = (By.XPATH,'(//div[@class="a-section aok-relative s-image-square-aspect"])[2]')
    addToCartLocator = (By.ID, "add-to-cart-button")
    secondItemSelectLocator = (By.XPATH,'(//div[@class="a-section aok-relative s-image-square-aspect"])[3]')





