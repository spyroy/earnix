from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = "https://demo.nopcommerce.com/"
DRIVER = webdriver.Chrome()
WAIT = WebDriverWait(DRIVER, 20)
SEARCH_BAR = 'small-searchterms'
SEARCH_SUBMIT = 'search-box-button'
DESKTOPS = "[href='/desktops']"
COMPUTERS = "[href='/computers']"
NOTEBOOKS = "[href='/notebooks']"
PRODUCT = 'product-item'
HIDDEN_ID = "data-productid"
TITLE = "product-title"
SHORT_DESCRIPTION = "A groundbreaking Retina display. A new force-sensing trackpad. All-flash " \
                    "architecture. Powerful dual-core and quad-core Intel processors. Together, " \
                    "these features take the notebook to a new level of performance. And they will do " \
                    "the same for you in everything you create."
LONG_DESCRIPTION = "With fifth-generation Intel Core processors, the latest graphics, and faster " \
                   "flash storage, the incredibly advanced MacBook Pro with Retina display moves even " \
                   "further ahead in performance and battery life.* *Compared with the previous " \
                   "generation." + "\nRetina display with 2560-by-1600 resolution" \
                   + "\nFifth-generation dual-core Intel Core i5 processor" + "\nIntel Iris Graphics" \
                   + "\nUp to 9 hours of battery life1" + "\nFaster flash storage2" + "\n802.11ac Wi-Fi" \
                   + "\nTwo Thunderbolt 2 ports for connecting high-performance devices and transferring data at " \
                     "lightning speed" + "\nTwo USB 3 ports (compatible with USB 2 devices) and HDMI" \
                   + "\nFaceTime HD camera" + "\nPages, Numbers, Keynote, iPhoto, iMovie, GarageBand included" \
                   + "\nOS X, the world's most advanced desktop operating system"


