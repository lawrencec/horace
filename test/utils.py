from os import getenv
from unittest import TestCase
from selenium import webdriver
from config import html_fixture_url


class TestObject(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = {
            'takeScreenshot': False,
            'javascriptEnabled': True,
            'browserName': cls._get_driver(),
            'platform': cls._get_platform()
        }
        cls.driver = webdriver.Remote(
            command_executor="http://localhost:4445/wd/hub",
            desired_capabilities=caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver = None

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(self._get_default_fixture_url())

    def tearDown(self):
        self.driver = None

    def _findBySelector(self, selector, parent=None):
        if parent is None:
            result = self.driver.find_element_by_css_selector(selector)
        else:
            result = parent.find_element_by_css_selector(selector)
        return result

    @classmethod
    def _get_driver(cls):
        return getenv('BROWSER', 'phantomjs')

    @classmethod
    def _get_platform(cls):
        return 'ANY'

    def _get_default_fixture_url(cls):
        return None


class HoraceTestObject(TestObject):

    def _get_default_fixture_url(self):
        return html_fixture_url