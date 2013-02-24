from unittest import TestCase
from selenium.webdriver import Remote
from horace.driver import Driver
from config import html_fixture_url


class TestDriver(TestCase):

    def test_default_config(self):
        d = Driver()
        self.assertTrue(d._driver)
        self.assertIsInstance(d._driver, Remote)

    # def test_with_config(self):
    #     d = Driver({'driver':'firefox'})
    #     self.assertTrue(d._driver)
    #     self.assertIsInstance(d._driver, Firefox)
    #     d.close()

    def test_passthrough(self):
        d = Driver()
        self.assertIsInstance(d._driver, Remote)
        html = d.find_elements_by_css_selector('html')
        self.assertEquals(len(html), 1)

    def test_title(self):
        d = Driver()
        d.get(html_fixture_url)
        self.assertEquals(d.title, 'Horace Test Page')

    def test_firstElement(self):
        d = Driver()
        first = d.firstElement()
        self.assertEquals(first.tag_name, 'html')

    def test_lastElement(self):
        d = Driver()
        first = d.lastElement()
        self.assertEquals(first.tag_name, 'body')

    def test_allElements(self):
        d = Driver()
        allElems = d.allElements()
        self.assertEquals(len(allElems), 3)