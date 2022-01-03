from pages.base.pagebase import PageBase
from pages.desktops import Desktops
from pages.notebooks import Notebooks
from pages.productpage import ProductPage

with PageBase() as page:
    page.main_page()
    page.go_to_notebooks()
    notebooks = Notebooks()
    ids = notebooks.sum_ids()
    print(ids)
    assert ids > 5

