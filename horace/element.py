from selenium.common.exceptions import InvalidSelectorException
from horace.exceptions import ElementNotFoundException

from selenium.webdriver.remote.command import Command

class Element(object):
    def __init__(self, element):
        self._element = element

    @property
    def tag_name(self):
        return self._element.tag_name

    @property
    def id(self):
        return self._element.get_attribute('id')

    @property
    def selected(self):
        return self._element.is_selected()

    @property
    def displayed(self):
        return self._element.is_displayed()

    @property
    def parent(self):
        result = None
        try:
            result = self._element.find_elements_by_xpath('..')
        except InvalidSelectorException:
            raise ElementNotFoundException('..')
        return Element(result[0])

    @property
    def text(self):
        return self._element.text

    def value(self, value=None, doReturn=False):
        if not value:
            return self._element.get_attribute('value')
        else:
            return self._element.send_keys(value)

    def click(self):
        return self._element.click()

    def size(self):
        return self._element.size

    def style(self, property_name):
        return self._element.value_of_css_property(property_name)

    def location(self):
        return self._element.location

    def attribute(self, name):
        return self._element.get_attribute(name)

    def find(self, selector):
        return self._element.find_elements_by_css_selector(selector)

    def double_click(self, driver):
        driver.execute(Command.MOVE_TO, {'element': self._element.id})
        driver.execute(Command.DOUBLE_CLICK, {})
        return self

