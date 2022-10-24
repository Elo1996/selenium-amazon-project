from Src.Pages.Base_page_file import BasePageClass
from Common.Custom_find_file import CustomFind
from selenium.webdriver.common.by import By


class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()

        self.navigationBarObj = CartPageClass(driver)

    def click_on_cart_button(self):
        cartItemElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        cartItemElement.click()


    def get_cart_products_quantity(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        return int(cartButtonElement.text)

    def remove_first_element_from_cart(self):
        itemDeleteElement = self.find.custom_find_element(self.locators.itemDeleteLocator)
        itemDeleteElement.click()

    def remove_all_elements_from_cart(self):
        """Removes all elements from cart"""
        while self.navigationBarObj.get_cart_products_quantity() > 0:
            self.remove_first_element_from_cart()

class CartPageLocatorsClass():
    itemDeleteLocator = (By.XPATH, '//input[@value="Delete"]')
    cartButtonLocator = (By.ID, "nav-cart-count")


