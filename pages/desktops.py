from selenium.webdriver.common.by import By
import pages.constants as const

from pages.productpage import ProductPage


# reusing the ProductPage class to find the price of each product.

class Desktops:
    def __init__(self, driver=const.DRIVER):
        self.driver = driver
        self.wait = const.WAIT

    def sum_all_desktops(self):
        ans = 0
        desktops = self.driver.find_elements(By.CLASS_NAME, "product-title")
        for i in range(len(desktops)):
            element = self.driver.find_elements(By.CLASS_NAME, "product-title")[i]
            product_page = ProductPage(name=element.text)
            product_page.go_to_product()
            price = product_page.product_price()
            ans += price
            self.driver.back()

        return ans
