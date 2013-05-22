from unittest import TestCase
from selenium import webdriver
from horace.contentNode import content_module, content_module_list, element
from horace.page import Page
from horace.module import Module, IFrameModule
import config
from config import html_fixture_url
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

    def _findAllBySelector(self, selector, parent=None):
        if parent is None:
            result = self.driver.find_elements_by_css_selector(selector)
        else:
            result = parent.find_elements_by_css_selector(selector)
        return result


class ParagraphSectionModule(Module):
    baseSelector = '#paragraphsSection'
    required = True

    _content = {
        'paragraphs': element(selector='p', required=False)
    }


class TableRowModule(Module):
    _content = {
        'data': element(selector='td', required=False)
    }


class TableModule(Module):
    baseSelector = 'table'
    required = True

    _content = {
        'rows': content_module_list(module=TableRowModule, selector='tr')
    }


class IFrame(IFrameModule):
    baseSelector = '#anIFrame'

    _content = {
        'headingTwoForIframe': element(selector='h2'),
        'table': content_module(module=TableModule),
        'rows': content_module_list(module=TableRowModule, selector='tr')
    }


class CSSTestPage(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'paragraphSection': content_module(
            module=ParagraphSectionModule,
            required=True
        ),
        'headingTwos': element(selector='h2'),
        'anIFrame': content_module(module=IFrame),
        'table': content_module(module=TableModule)
    }

    # Setting properties via the @property decorator is purely optional but it
    # helps in providing code assistance in IDES or python console
    # @property
    # def paragraphSection(self):
    #     return self._getContent('paragraphSection')


class CSSTestPageWithMissingRequiredElements(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'hardbreaks': element(selector='br', required=True)
    }


class UnknownTestPage(Page):
    url = 'must404.html'
    title = 'unknown'

    def at(self, title):
        return None


class DuckDuckGoPage(Page):
    url = 'http://duckduckgo.com/'
    title = 'Search DuckDuckGo'