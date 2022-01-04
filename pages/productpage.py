from selenium.webdriver.common.by import By
import pages.constants as const
from selenium.webdriver.support import expected_conditions as EC

from pages.base.pagebase import PageBase


class ProductPage(PageBase):
    def __init__(self, name=None):
        super(ProductPage, self).__init__()
        self._name = name

    def go_to_product(self):
        css = f"[title*='{self._name}']"
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        product = self.driver.find_element(By.CSS_SELECTOR, css)
        product.click()

    def short_description(self):
        class_name = "short-description"
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        description = self.driver.find_element(By.CLASS_NAME, class_name).text
        return description

    def long_description(self):
        class_name = "full-description"
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        description = self.driver.find_element(By.CLASS_NAME, class_name).text
        return description

    def product_price(self):
        css = "[id*=price]"
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        description = self.driver.find_element(By.CSS_SELECTOR, css).text.split('$')
        price = float(description[1].replace(',', ''))
        return price




