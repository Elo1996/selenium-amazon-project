from Common.Custom_find_file import CustomFind


class BasePageClass:
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)

    def click_to_element(self, element):
        element.click()

    def double_click(self):
        pass

    def click_and_hold(self):
        pass

    def set_text(self):
        pass

    def get_text(self):
        pass

    def clear_text(self):
        pass

    def find_element(self, locator):
        # todo MIGRATE OUR CUSTOM FIND FUNCTIONALITY HERE VAHAG
        return self.find.custom_find_element(locator)

    def find_elements(self, locator):
        # todo MIGRATE OUR CUSTOM FIND FUNCTIONALITY HERE VAHAG
        pass

    def open(self, url):
        pass
        # url = self.base_url + url
        # self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url