from unittest import TestCase
from selenium.webdriver import Remote
from horace.driver import Driver
from config import html_fixture_url, driver


class TestDriver(TestCase):
    config = {'driver': driver}

    def test_default_config(self):
        d = Driver(TestDriver.config)
        self.assertTrue(d._driver)
        self.assertIsInstance(d._driver, Remote)

    def test_with_config(self):
        d = Driver(TestDriver.config)
        self.assertTrue(d._driver)
        self.assertEquals(d._driver.name, driver)
        d.close()

    def test_capabilities(self):
        d = Driver(TestDriver.config)
        self.assertTrue(d._driver)
        capabilities = d._driver.capabilities
        self.assertTrue(capabilities['javascriptEnabled'])

    def test_passthrough(self):
        d = Driver(TestDriver.config)
        self.assertIsInstance(d._driver, Remote)
        html = d.find_elements_by_css_selector('html')
        self.assertEquals(len(html), 1)

    def test_title(self):
        d = Driver(TestDriver.config)
        d.get(html_fixture_url)
        self.assertEquals(d.title, 'Horace Test Page')

    def test_firstElement(self):
        d = Driver(TestDriver.config)
        first = d.first_element()
        self.assertEquals(first.tag_name, 'html')

    def test_lastElement(self):
        d = Driver(TestDriver.config)
        first = d.last_element()
        self.assertEquals(first.tag_name, 'body')

    def test_allElements(self):
        d = Driver(TestDriver.config)
        allElems = d.all_elements()
        self.assertEquals(len(allElems), 3)