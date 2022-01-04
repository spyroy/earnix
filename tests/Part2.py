from pages.base.pagebase import PageBase
from pages.desktops import Desktops
from pages.notebooks import Notebooks


def test_part2_a():
    with PageBase(teardown=False) as page:
        page.go_to_main_page()
        page._go_to_desktops()
        desktops = Desktops()
        prices = desktops.sum_all_products()
        print("\ntotal desktops price: ", prices)
        desktops.go_to_main_page()
        assert prices > 2500, "The sum of all products price is lower than 2500"


def test_part2_b():
    with PageBase(teardown=False) as page:
        page.go_to_main_page()
        page._go_to_notebooks()
        notebooks = Notebooks()
        ids = notebooks.sum_all_products()
        print(ids)
        notebooks.go_to_main_page()
        assert ids > 5, "The sum of all products id is lower than 5"
