from horace.exceptions import JavascriptExecutionException
from utils import HoraceTestObject
from test.JSTest.pages.jstestpage import JSTestPage
from config import js_fixture_url


class TestJavascript(HoraceTestObject):
    driver = None

    def _get_default_fixture_url(self):
        return js_fixture_url

    def test_page_javascript_returns_document_variable(self):
        webPage = JSTestPage(self.driver)
        title = webPage.execute_script('return document.title')
        self.assertEquals('JS Test Page', title)

    def test_page_javascript_returns_variable(self):
        webPage = JSTestPage(self.driver)
        jsArray = webPage.execute_script('return testArray')
        self.assertEquals(len(jsArray), 2)
        self.assertEquals(jsArray, [100, 200])

    def test_page_javascript_return_element(self):
        webPage = JSTestPage(self.driver)
        bodyEl = webPage.execute_script('return document.getElementsByTagName("body")[0]')
        self.assertEquals(bodyEl.get_attribute('id'), 'jsTestPage')

    def test_page_javascript_raises_javascript_execution_exception(self):
        webPage = JSTestPage(self.driver)
        try:
            webPage.execute_script('return testArrrr')
        except JavascriptExecutionException, e:
            pass
        self.assertRaises(Exception, webPage.execute_script, JavascriptExecutionException)
