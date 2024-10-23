# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#    for browser_type in [p.chromium, p.firefox, p.webkit]:
#        browser = browser_type.launch()
#        page = browser.new_page()
#        page.goto("http://playwright.dev")
#        page.screenshot(path=f"example-{browser_type.name}.png")
#        browser.close()
#
import logging
from datetime import date
import getpass
from fints.client import FinTS3PinTanClient

logging.basicConfig(level=logging.DEBUG)
f = FinTS3PinTanClient(
    "123456789",  # Your bank's BLZ
    "myusername",  # Your login name
    getpass.getpass("PIN:"),  # Your banking PIN
    "https://hbci-pintan.gad.de/cgi-bin/hbciservlet",
    product_id="Your product ID",  # see above
)
