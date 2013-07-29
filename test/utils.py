from unittest import TestCase
from selenium import webdriver
from config import driver, platform, html_fixture_url


class TestObject(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = {
            'takeScreenshot': False,
            'javascriptEnabled': True,
            'browserName': driver,
            'platform': platform
        }
        cls.driver = webdriver.Remote(
            command_executor="http://localhost:5556/wd/hub",
            desired_capabilities=caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver = None

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(html_fixture_url)

    def tearDown(self):
        self.driver = None

    def _findBySelector(self, selector, parent=None):
        if parent is None:
            result = self.driver.find_element_by_css_selector(selector)
        else:
            result = parent.find_element_by_css_selector(selector)
        return result
