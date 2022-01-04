from pages.base.pagebase import PageBase
from pages.productpage import ProductPage
import pages.constants as const


def test_part1():
    with PageBase(teardown=False) as page:
        page.go_to_main_page()
        page._search_in_main_page("macbook")
        product_page = ProductPage(name="Apple MacBook Pro 13-inch")
        product_page.go_to_product()
        short_description = product_page.short_description()
        print("short description: ", short_description)
        long_description = product_page.long_description()
        print("long description: ", long_description)
        price = product_page.product_price()
        print("product price is: ", price)
        product_page.go_to_main_page()
        assert short_description == const.SHORT_DESCRIPTION, 'The description didnt match'
        assert long_description == const.LONG_DESCRIPTION, 'The description didnt match'
        assert price > 1000, 'Price of product is lower than 1000'


