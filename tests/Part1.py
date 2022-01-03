from pages.base.pagebase import PageBase
from pages.productpage import ProductPage


def test_part1():
    with PageBase(teardown=True) as page:
        page.main_page()
        page.search_in_main_page("macbook")
        product_page = ProductPage(name="Apple MacBook Pro 13-inch")
        product_page.go_to_product()
        short_description = product_page.short_description()
        print("short description: ", short_description)
        long_description = product_page.long_description()
        print("long description: ", long_description)
        price = product_page.product_price()
        print("product price is: ", price)
        assert short_description == "A groundbreaking Retina display. A new force-sensing trackpad. All-flash " \
                                    "architecture. Powerful dual-core and quad-core Intel processors. Together, " \
                                    "these features take the notebook to a new level of performance. And they will do " \
                                    "the same for you in everything you create."
        assert long_description == "With fifth-generation Intel Core processors, the latest graphics, and faster " \
                                   "flash storage, the incredibly advanced MacBook Pro with Retina display moves even " \
                                   "further ahead in performance and battery life.* *Compared with the previous " \
                                   "generation." + "\nRetina display with 2560-by-1600 resolution" \
               + "\nFifth-generation dual-core Intel Core i5 processor" + "\nIntel Iris Graphics" \
               + "\nUp to 9 hours of battery life1" + "\nFaster flash storage2" + "\n802.11ac Wi-Fi" \
               + "\nTwo Thunderbolt 2 ports for connecting high-performance devices and transferring data at " \
                 "lightning speed" + "\nTwo USB 3 ports (compatible with USB 2 devices) and HDMI" \
               + "\nFaceTime HD camera" + "\nPages, Numbers, Keynote, iPhoto, iMovie, GarageBand included" \
               + "\nOS X, the world's most advanced desktop operating system"
        assert price > 1000

