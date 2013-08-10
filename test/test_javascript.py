from horace.exceptions import JavascriptExecutionException
from utils import TestObject
from test.JSTest.pages.jstestpage import JSTestPage
from config import js_fixture_url


class TestJavascript(TestObject):
    driver = None
    fixture_url = js_fixture_url

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
            self.assertTrue(e.message.startswith(
                'Error executing javascript: Error Message => \'Can\'t find variable: testArrrr')
            )
        self.assertRaises(Exception, webPage.execute_script, JavascriptExecutionException)
