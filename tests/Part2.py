from pages.base.pagebase import PageBase
from pages.desktops import Desktops
from pages.notebooks import Notebooks


def test_part2_a():
    with PageBase(teardown=True) as page:
        page.main_page()
        page.go_to_desktops()
        desktops = Desktops()
        prices = desktops.sum_all_desktops()
        print("\ntotal desktops price: ", prices)
        assert prices > 2500


def test_part2_b():
    with PageBase(teardown=True) as page:
        page.main_page()
        page.go_to_notebooks()
        notebooks = Notebooks()
        ids = notebooks.sum_ids()
        print(ids)
        assert ids > 5
