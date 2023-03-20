import time
import allure
from pages.product_page import ProductPage


@allure.description("Test order_from_product_page")
def test_order_from_product_page(browser):

    """Ссылка на тестовый"""
    link = "https://grechka:digital@xiaomi-shop.grechka.digital/catalog/smartfony-i-planshety/redmi/redmi-10c-3-64-gb-mint-green"
    """Ссылка на боевой"""
    #link = "https://xiaomi-stores.ru/catalog/smartfony-i-planshety/redmi/redmi-10c-3-64-gb-mint-green"
    print("\nStart Order Test")
    browser.maximize_window()
    pp = ProductPage(browser, link)
    pp.open()
    pp.make_the_order()

    print("Finish Tests")
    time.sleep(1)
