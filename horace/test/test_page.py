from utils import TestObject
from utils import CSSTestPage, CSSTestPageWithMissingRequiredElements
from horace.exceptions import ElementNotFoundException


class TestPageObject(TestObject):
    driver = None

    def test_page_modules(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.paragraphSection)
        self.assertEquals(len(webPage.paragraphSection.paragraphs), 2)
        self.assertIsNotNone(webPage.table)
        self.assertIsNotNone(webPage.table.rows)
        self.assertEquals(len(webPage.table.rows), 4)
        self.assertEquals(webPage.table.rows[1].data.text, 'Division 1')
        self.assertFalse('paragraphs' in webPage._content_instances)
        self.assertEquals(len(webPage._content_instances), 4)


    def test_page_title(self):
        webPage = CSSTestPage(self.driver)
        self.assertEquals(webPage.title, 'Horace Test Page')

    def test_page_with_required_elements_throws_exception(self):
        try:
            CSSTestPageWithMissingRequiredElements(self.driver)
            self.fail("Didn't raise Exception")
        except ElementNotFoundException, e:
            self.assertEquals(
                'Element not found (br)',
                e.message
            )

    def test_page_elements(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.headingTwos)
        self.assertEqual(len(webPage.headingTwos), 9)

    def test_get_attribute(self):
        webPage = CSSTestPage(self.driver)
        try:
            webPage.foo
        except AttributeError, e:
            self.assertEquals(
                "'CSSTestPage' object has no attribute 'foo'",
                e.message
            )

    def test_iframe_element(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.anIFrame)
        self.assertEqual(len(webPage.anIFrame.get_elements_by_selector('h2')), 1)
        self.assertEqual(len(webPage.anIFrame.headingTwos), 1)
        self.assertEqual(len(webPage.headingTwos), 9)