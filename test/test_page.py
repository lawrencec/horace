import os
from utils import HoraceTestObject
from test.CSSTest.pages.testpage import CSSTestPage
from test.CSSTest.pages.testpage_missing_elements import CSSTestPageWithMissingRequiredElements
from test.CSSTest.modules.paragraph import ParagraphSectionModule

from horace.contentNode import element, content_module, content_module_list
from horace.exceptions import ElementNotFoundException


class TestPageObject(HoraceTestObject):
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
            page = CSSTestPageWithMissingRequiredElements(self.driver)
            len(page.hardbreaks)
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

    def test_refresh_content(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.headingTwos)
        self.assertEquals(len(webPage.paragraphSection.paragraphs), 2)
        webPage.refresh_content('paragraphSection')
        self.assertEquals(len(webPage.paragraphSection.paragraphs), 2)

    def test_iframe_with_elements(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.anIFrame)
        # self.assertEqual(len(webPage.anIFrame.get_elements_by_selector('h2')), 1)
        self.assertEqual(len(webPage.anIFrame.headingTwoForIframe), 1)
        self.assertEqual(len(webPage.headingTwos), 9)

    def test_iframe_with_modules(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.anIFrame)
        self.assertIsNotNone(webPage.headingTwos)
        self.assertEqual(len(webPage.anIFrame.headingTwoForIframe), 1)
        self.assertEqual(len(webPage.headingTwos), 9)

        self.assertIsNotNone(webPage.anIFrame.table)
        webPage.anIFrame.activate()
        self.assertEqual(len(webPage.anIFrame.table.rows), 2)
        self.assertEqual(len(webPage.anIFrame.rows), 2)

    def test_elements_helper(self):
        element_definition = element('foo', False)
        self.assertEquals(element_definition, {'selector': 'foo', 'required': False})
        try:
            element(None, False)
        except Exception, e:
            self.assertEquals(
                "selector required",
                e.message
            )

    def test_module_helper(self):
        module_definition = content_module(ParagraphSectionModule, 'foo', False)
        self.assertEquals(module_definition, {'module': ParagraphSectionModule, 'selector': 'foo', 'required': False})
        try:
            content_module(None, None, False)
        except Exception, e:
            self.assertEquals(
                "selector or module required",
                e.message
            )

    def test_module_list_helper(self):
        module_list_definition = content_module_list(ParagraphSectionModule, 'foo', False)
        self.assertEquals(module_list_definition,
                          {'module': ParagraphSectionModule, 'selector': 'foo', 'required': False, 'isList': True})
        try:
            content_module_list(None, 'foo', False)
        except Exception, e:
            self.assertEquals(
                "selector or module required",
                e.message
            )

    def test_take_screenshot(self):
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.headingTwos)
        base64EncodedImage = webPage.take_screenshot()
        self.assertEquals(base64EncodedImage[:10], 'iVBORw0KGg')

    def test_take_screenshot_as_filename(self):
        screenshotFilename = '/tmp/testScreenshot.png'
        webPage = CSSTestPage(self.driver)
        self.assertIsNotNone(webPage.headingTwos)

        self.assertFalse(os.path.exists(screenshotFilename))
        self.assertTrue(webPage.take_screenshot(screenshotFilename))
        assert os.path.exists(screenshotFilename)
        os.remove(screenshotFilename)
        self.assertFalse(os.path.exists(screenshotFilename))