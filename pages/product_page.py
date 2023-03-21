import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.data import DataPage
from utilities.logger import Logger

import allure
from base.base_class import BaseClass


class ProductPage(BaseClass):

    # Locators
    button_town = "//div[@class='notification__city js-popup-city-tgl js-notification-city-confirm']"
    input_town = "//input[@placeholder='Ваш город']"
    choose_town = "//li[@class='popup-city__item js-city-item'][1]"
    accept_cookie = "//div[@class='policy-banner__close js-coockie-banner-button']"
    button_reserve = "//button[@class='btn btn_small map-item__btn map-item__choose js-select-shop js-reserve-shop']"
    button_pre_reserve = "//button[@class='btn btn_small map-item__btn map-item__choose js-select-shop js-presale-button js-popup-presale-tgl']"
    button_cart = "//a[@class='header-cart']"
    button_make_reserve = "//button[@class='btn p-basket-item__btn js-popup-reserve-tgl js-reserve-send']"
    input_name = "//input[@placeholder='Ваше имя']"
    input_phone = "//input[@name='customer_phone']"
    input_mail = "//input[@name='customer_email']"
    checkbox = "//label[@class='small checkbox__label']"
    button_make_order = "//input[@class='btn popup-form__submit']"
    button_ok = "//button[@class='btn popup__btn js-popup-reserve-tgl']"


    # Getters
    def get_button_town(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_town)))

    def get_input_town(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_town)))

    def get_choose_town(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_town)))

    def get_accept_cookie(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie)))

    def get_button_reserve(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_reserve)))

    def get_button_pre_reserve(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pre_reserve)))

    def get_button_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_button_make_reserve(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_reserve)))

    def get_input_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_mail(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_mail)))

    def get_checkbox(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_button_make_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))

    def get_button_ok(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_ok)))

    # Actions
    def click_button_town(self):
        self.get_button_town().click()
        print("Click button_town")

    def input_input_town(self):
        self.get_input_town().send_keys(*DataPage.town)
        print("Input town")

    def input_input_pre_order_town(self):
        self.get_input_town().send_keys(*DataPage.pre_order_town)
        print("Input town")

    def click_choose_town(self):
        self.get_choose_town().click()
        print("Click choose_town")

    def click_accept_cookie(self):
        self.get_accept_cookie().click()
        print("Click accept_cookie")

    def click_button_reserve(self):
        self.get_button_reserve().click()
        print("Click_button_reserve")

    def click_button_pre_reserve(self):
        self.get_button_pre_reserve().click()
        print("Click_button_pre_reserve")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("Click_button_cart")

    def click_button_make_reserve(self):
        self.get_button_make_reserve().click()
        print("button_make_reserve")

    def input_input_name(self):
        self.get_input_name().send_keys(*DataPage.name)
        print("input_name")

    def input_input_name_pre_order(self):
        self.get_input_name().send_keys(*DataPage.name_pre_order)
        print("input_name_pre_order")

    def input_input_phone(self):
        self.get_input_phone().send_keys(*DataPage.phone)
        print("input_phone")

    def input_input_mail(self):
        self.get_input_mail().send_keys(*DataPage.email)
        print("input_mail")

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Click checkbox")

    def click_button_make_order(self):
        self.get_button_make_order().click()
        print("Click button_make_order")


    def click_button_ok(self):
        self.get_button_ok().click()
        print("Click button_ok")


    # Metods
    def make_the_order(self):
        """make_the_order"""
        with allure.step("make_the_order from product page"):
            Logger.add_start_step(method="make_the_order")

            self.get_current_url()
            self.click_button_town()
            self.input_input_town()
            time.sleep(3)
            self.click_choose_town()
            self.click_accept_cookie()
            self.click_button_reserve()
            self.click_button_cart()
            self.click_button_make_reserve()
            self.input_input_name()
            self.input_input_phone()
            self.input_input_mail()
            self.click_checkbox()
            self.click_button_make_order()
            self.click_button_ok()
            Logger.add_end_step(url=self.browser.current_url, method="make_the_order")

    def make_the_pre_order(self):
        """make_pre_order"""
        with allure.step("make_the_pre_order from product page"):
            Logger.add_start_step(method="make_the_pre_order")

            self.click_button_town()
            self.input_input_pre_order_town()
            time.sleep(3)
            self.click_choose_town()
            self.click_accept_cookie()
            self.click_button_pre_reserve()
            self.input_input_name_pre_order()
            self.input_input_phone()
            self.input_input_mail()
            self.click_checkbox()
            self.click_button_make_order()
            self.click_button_ok()
            Logger.add_end_step(url=self.browser.current_url, method="make_the_pre_order")

