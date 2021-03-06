from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pages.constants as const
from selenium.webdriver.support import expected_conditions as EC

# I inherited from webdriver.Chrome so i could use
# 'with' statement (which uses __enter__ and __exit__)


class PageBase(webdriver.Chrome):
    def __init__(self, driver=const.DRIVER, teardown=False):
        self.driver = driver
        driver.maximize_window()
        self.teardown = teardown
        self.wait = const.WAIT

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.close()

    def go_to_main_page(self):
        self.driver.get(const.BASE_URL)

    def _search_in_main_page(self, txt):
        search_bar = self.driver.find_element(By.ID, const.SEARCH_BAR)
        search_bar.send_keys(txt)
        submit = self.driver.find_element(By.CLASS_NAME, const.SEARCH_SUBMIT)
        submit.click()

    def _go_to_desktops(self):
        css = const.DESKTOPS
        self._go_to(css)

    def _go_to_notebooks(self):
        css = const.NOTEBOOKS
        self._go_to(css)

    def _go_to(self, css):
        css1 = css
        css2 = const.COMPUTERS
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css2)))
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.CSS_SELECTOR, css2)
        a.move_to_element(m).perform()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css1)))
        element = self.driver.find_element(By.CSS_SELECTOR, css1)
        element.click()

