from horace.exceptions import NotAtPageException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Agent(object):

        def __init__(self, driver):
            self._driver = driver
            self._currentPage = None

        def __getattr__(self, name):
            if name == 'page':
                return self._currentPage
            else:
                return object.__getattribute__(self, name)

        def to(self, Page):
            self._driver.get(Page.url)

        def at(self, page):
            self._currentPage = page(self._driver)

            title = self._driver.title
            if page.wait == 0:
                if not self._currentPage.at(title):
                    raise NotAtPageException(self._currentPage.title, title)
            else:
                try:
                    self.waitUntil(
                        page.wait,
                        lambda driver: self._currentPage.at(driver.title)
                    )
                except TimeoutException:
                    raise NotAtPageException(self._currentPage.title, title)

        def to_at(self, Page):
            self.to(Page)
            self.at(Page)
            return self

        def do(self, action=None, *args):
            if action and callable(action):
                action(self._currentPage, *args)
            return self

        def waitUntil(self, delay, fn):
            WebDriverWait(self._driver, delay).until(lambda driver: fn(driver))

        def close(self):
            self._driver.close()