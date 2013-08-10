from selenium.common.exceptions import WebDriverException
from horace.contentNode import ContentNode
from horace.exceptions import JavascriptExecutionException


class Page(ContentNode):
    url = None
    title = None
    _content = {}
    wait = 0

    def at(self, title):
        return unicode(title) == unicode(self.title)

    def at(self, title):
        return unicode(title) == unicode(self.title)

    def initialize_content(self, item):
        self.to_default_content()
        super(Page, self).initialize_content()

    def take_screenshot(self, filename=None):
        if filename is None:
            return self._driver.get_screenshot_as_base64()
        else:
            return self._driver.get_screenshot_as_file(filename)

    def execute_script(self, script):
        try:
            return self._driver.execute_script(script)
        except WebDriverException, e:
            raise JavascriptExecutionException(e.msg)

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


