from horace.exceptions import NotAtPageException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib import urlencode


class Agent(object):

        def __init__(self, driver):
            self._driver = driver
            self._currentPage = None

        def __getattr__(self, name):
            if name == 'page':
                return self._currentPage
            else:
                return object.__getattribute__(self, name)

        def to(self, page, parameters=None):
            url = page.url
            if parameters is not None:
                url = '%s?%s' % (url, urlencode(parameters))
            self._driver.get(url)

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

            return self

        def to_at(self, page, parameters=None):
            self.to(page, parameters)
            self.at(page)

            return self

        def then(self, action=None, *args):
            if action and callable(action):
                action(self._currentPage, *args)
            return self

        def waitUntil(self, delay, fn):
            WebDriverWait(self._driver, delay).until(lambda driver: fn(driver))

        def close(self):
            self._driver.close()