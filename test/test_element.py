from utils import TestObject
from horace.element import Element
from horace.exceptions import ElementNotFoundException


class TestElement(TestObject):

    def test_tag_name(self):
        webElement = self._findBySelector('link[title="A CSS stylesheet"]')
        element = Element(webElement)
        self.assertEqual(element.tag_name, 'link')

    def test_id(self):
        webElement = self._findBySelector('#headings')
        element = Element(webElement)
        self.assertEqual(element.id, 'headings')

    def test_selected(self):
        webElement = self._findBySelector('#checkbox1')
        webElement.click()  # select
        element = Element(webElement)
        self.assertTrue(element.selected)

    def test_displayed(self):
        webElement = self._findBySelector('#hiddenElement')
        element = Element(webElement)
        self.assertFalse(element.displayed)

    def test_parent(self):
        webElement = self._findBySelector('blockquote')
        element = Element(webElement)
        self.assertEqual(element.parent.tag_name, 'body')

    def test_text(self):
        webElement = self._findBySelector('#headings')
        element = Element(webElement)
        self.assertEqual(element.text, 'Headings')

    def test_value(self):
        webElement = self._findBySelector('#text_field')
        element = Element(webElement)
        element.value('Text in a field')
        self.assertEqual(element.value(), 'Text in a field')

    def test_click(self):
        webElement = self._findBySelector('#text_field')
        element = Element(webElement)
        element.click()  # ensure focus
        self.assertEqual(Element(self.driver.switch_to_active_element()).id, element.id)

    def test_size(self):
        webElement = self._findBySelector('img')
        element = Element(webElement)
        self.assertEqual(element.size(), {'width': 250, 'height': 125})

    def test_style(self):
        webElement = self._findBySelector('#hiddenElement')
        element = Element(webElement)
        self.assertTrue(element.style('display') in [None, 'none'])

    def test_location(self):
        webElement = self._findBySelector('#headings')
        element = Element(webElement)
        element_location = element.location()
        self.assertTrue('x' in element_location)
        self.assertTrue('y' in element_location)

    def test_attribute(self):
        webElement = self._findBySelector('link[title="Another CSS stylesheet"]')
        element = Element(webElement)
        self.assertIn('css/style2.css', element.attribute('href'))

    def test_exception_when_parent_not_found(self):
        webElement = self._findBySelector('html')
        element = Element(webElement)
        self.assertEqual(element.tag_name, 'html')
        try:
            element.parent()
        except ElementNotFoundException, e:
            self.assertEquals(e.message, 'Element not found (..)')

    def test_find_by_css_selector(self):
        webElement = self._findBySelector('html')
        element = Element(webElement)
        bodyElement = element.find('body')
        self.assertEqual(len(bodyElement), 1)
        self.assertEqual(bodyElement[0].tag_name, 'body')
