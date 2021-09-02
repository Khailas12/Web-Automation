import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"


class Main(webdriver.Chrome):
    def __init__(self, path=r"C:\SeleniumDriver", teardown=False):
        self.path = path
        self.teardown = teardown
        os.environ["PATH"] += self.path
        super(Main, self).__init__()    # super() method lets you access methods in a parent class

    def first_page(self):
        self.maximize_window()
        self.get(URL)
        self.implicitly_wait(2)
        print("Site opened")

    def popup_skip(self):
        try:
            button = self.find_element_by_class_name("at-cm-no-button")
            button.click()
            print("Popup skipped")
        except:
            print("\n No element with this class name. Skipping the process")


class Secondary(Main):   # Using call parent method
        def message(self):
            msg = self.find_element_by_id("user-message")
            msg.send_keys("Hello World")

        def text_btn(self):
            btn = self.find_element_by_css_selector(
                "button[onclick='showInput();']")
            btn.click()
            print("text button clicked")

        def sum(self):
            sum1 = self.find_element_by_id("sum1")
            sum2 = self.find_element_by_id("sum2")

            sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD4)
            sum2.send_keys(Keys.NUMPAD6, Keys.NUMPAD8)

        def sum_button(self):
            btn = self.find_element_by_css_selector(
                "button[onclick='return total()']")
            btn.click()
            print("Sum button clicked")




