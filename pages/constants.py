from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = "https://demo.nopcommerce.com/"
DRIVER = webdriver.Chrome()
WAIT = WebDriverWait(DRIVER, 20)
