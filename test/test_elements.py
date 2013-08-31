from horace.elements import Elements
from utils import HoraceTestObject


class TestElements(HoraceTestObject):

    def _findBySelector(self, selector, parent=None):
        if parent is None:
            result = self.driver.find_elements_by_css_selector(selector)
        else:
            result = parent.find_elements_by_css_selector(selector)
        return result

    def getElements(self, selector):
        webElements = self._findBySelector(selector)
        element = Elements(webElements)
        return element

    def test_property_name_resolves_to_first_item(self):
        elements = self.getElements('link')
        self.assertEqual(
            elements.attribute('title'),
            'A CSS stylesheet'
        )

    def test_property_name_can_be_found_via_indexed_element(self):
        elements = self.getElements('link')
        self.assertEqual(
            elements[1].attribute('title'),
            'Another CSS stylesheet'
        )

    def test_exception_incorrect_attribute_is_accessed(self):
        elements = self.getElements('link')
        try:
            self.assertRaises(AttributeError, elements.incorrect)
        except AttributeError:
            pass