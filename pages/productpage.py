from selenium.webdriver.common.by import By
import pages.constants as const
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver=const.DRIVER, name=None):
        self.driver = driver
        self.wait = const.WAIT
        self.name = name

    def go_to_product(self):
        css = f"[title*='{self.name}']"
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




