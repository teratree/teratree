import json
import os
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExampleTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        cls.browser.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        # Comment this out if you don't want Chrome to quit
        cls.browser.quit()
        # Handy to use this line for debugging
        # import pdb; pdb.set_trace()
        super().tearDownClass()

    def test_01_get_debug_root(self):
        self.browser.get('http://web:8000/')
        heading = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1'))
        )
        self.assertEqual(heading.text, "Page not found (404)")
