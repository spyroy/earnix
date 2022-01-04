from selenium.webdriver.common.by import By
import pages.constants as const
from pages.base.pagebase import PageBase
from pages.productssum import ProductsSum

# reusing the ProductPage class to find the price of each product.
from pages.productpage import ProductPage


class Desktops(ProductsSum, PageBase):
    def __init__(self):
        super(Desktops, self).__init__()

    def sum_all_products(self):
        ans = 0
        desktops = self.driver.find_elements(By.CLASS_NAME, const.TITLE)
        for i in range(len(desktops)):
            element = self.driver.find_elements(By.CLASS_NAME, const.TITLE)[i]
            product_page = ProductPage(name=element.text)
            product_page.go_to_product()
            price = product_page.product_price()
            ans += price
            self.driver.back()

        return ans

