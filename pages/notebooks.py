from selenium.webdriver.common.by import By
import pages.constants as const

from pages.productpage import ProductPage


class Notebooks:
    def __init__(self, driver=const.DRIVER):
        self.driver = driver
        self.wait = const.WAIT

    def sum_ids(self):
        ans = 0
        desktops = self.driver.find_elements(By.CLASS_NAME, 'product-item')
        for i in range(len(desktops)):
            hidden_id = int(self.driver.find_elements(By.CLASS_NAME, 'product-item')[i].get_attribute("data-productid"))
            ans += hidden_id

        return ans
