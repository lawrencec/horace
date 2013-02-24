from unittest import TestCase
from selenium import webdriver
from horace.page import Page
from horace.module import Module
from config import html_fixture_url

import config


drivers = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome
}


class TestObject(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = {
            'takeScreenshot': False,
            'javascriptEnabled': True
        }
        if config.driver in drivers:
            cls.driver = drivers[config.driver]()
        else:
            cls.driver = webdriver.Remote(
                command_executor="http://localhost:8910/wd/hub",
                desired_capabilities=caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver = None

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(config.html_fixture_url)

    def tearDown(self):
        self.driver = None

    def _findBySelector(self, selector, parent=None):
        if parent is None:
            result = self.driver.find_element_by_css_selector(selector)
        else:
            result = parent.find_element_by_css_selector(selector)
        return result


class ParagraphSectionModule(Module):
    base = '#paragraphsSection'
    required = True

    _content = {
        'paragraphs': {
            'selector': 'p',
            'required': False
        }
    }

    def __init__(self, driver, config=None):
        super(ParagraphSectionModule, self).__init__(driver, config)


class CSSTestPage(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'paragraphSection': {
            'base': ParagraphSectionModule,
            'required': True
        },
        'headingTwos': {'selector': 'h2'}
    }

    def __init__(self, driver):
        super(CSSTestPage, self).__init__(driver)

    # Setting properties via the @property decorator is purely optional but it
    # helps in providing code assistance in IDES or python console
    # @property
    # def paragraphSection(self):
    #     return self._getContent('paragraphSection')


class CSSTestPageWithMissingRequiredElements(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'hardbreaks': {
            'selector': 'br',
            'required': True
        }
    }

    def __init__(self, driver):
        super(CSSTestPageWithMissingRequiredElements, self).__init__(driver)


class UnknownTestPage(Page):
    url = 'must404.html'
    title = 'unknown'

    def __init__(self, driver):
        super(UnknownTestPage, self).__init__(driver)


class DuckDuckGoPage(Page):
    url = 'http://duckduckgo.com/'
    title = 'DuckDuckGo'

    def __init__(self, driver):
        super(DuckDuckGoPage, self).__init__(driver)