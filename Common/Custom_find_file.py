from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CustomFind():
    def __init__(self,driver):
        self.driver = driver

    def custom_find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            print("Error 200: Element not found Exception")
            print(e)
            exit(3)