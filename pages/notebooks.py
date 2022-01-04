from selenium.webdriver.common.by import By
import pages.constants as const
from pages.base.pagebase import PageBase

from pages.productssum import ProductsSum


class Notebooks(ProductsSum, PageBase):
    def __init__(self):
        super(Notebooks, self).__init__()

    def sum_all_products(self):
        ans = 0
        desktops = self.driver.find_elements(By.CLASS_NAME, const.PRODUCT)
        for i in range(len(desktops)):
            hidden_id = int(self.driver.find_elements(By.CLASS_NAME, const.PRODUCT)[i].get_attribute(const.HIDDEN_ID))
            ans += hidden_id

        return ans

