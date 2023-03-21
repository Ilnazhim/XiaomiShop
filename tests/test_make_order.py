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


@allure.description("Test pre-order_from_product_page")
def test_pre_order_from_product_page(browser):

    """Ссылка на тестовый"""
    link = "https://grechka:digital@xiaomi-shop.grechka.digital/catalog/nosimye-ustroystva/fitnes-braslety/xiaomi-smart-band-7?_token=jQ0uy2ebZrARtSE8U1jZnGLiGYpOVFyX31n7gH8n&order_type=presale&customer_name=%D0%A2%D0%B5%D1%81%D1%82&customer_phone=8+919+111+11+11&customer_email=nazhimov%40grechka.digital&products=6934177783517&shop_id=MIRUP02870&customer_acceptance=1#"
    """Ссылка на боевой"""
    #link = "https://xiaomi-stores.ru/catalog/smartfony-i-planshety/redmi/redmi-10c-3-64-gb-mint-green"
    print("\nStart Pre-order Test")
    browser.maximize_window()
    pp = ProductPage(browser, link)
    pp.open()
    pp.make_the_pre_order()

    print("Finish Tests")
    time.sleep(1)