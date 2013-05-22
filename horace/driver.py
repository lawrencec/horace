from selenium import webdriver
from horace.elements import Elements
from horace.element import Element

class Driver(object):
    def __new__(cls, *p, **k):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance

    def __init__(self, config=None):
        if config is None:
            config = {
                'driver': 'phantomjs'
            }

        drivers = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome
        }

        if config['driver'] in drivers:
            self._driver = drivers[config['driver']]()
        else:
            self._driver = webdriver.Remote(
                command_executor="http://localhost:8910/wd/hub",
                desired_capabilities={
                    'takesScreenshot': False,
                    'javascriptEnabled': True
                })

    def __getattr__(self, name):
        if name == '_driver':
            return self._driver
        elif name in webdriver.Remote.__dict__.keys():
            return webdriver.Remote.__dict__[name].__get__(self._driver)
        else:
            return object.__getattribute__(self, name)

    def first_element(self):
        first = self._driver.find_elements_by_css_selector('html')
        return Element(first[0]) if len(first) > 0 else None

    def last_element(self):
        last = self._driver.find_elements_by_css_selector('*')[-1]
        return Element(last)

    def all_elements(self):
        return Elements(self._driver.find_elements_by_css_selector('*'))

    def close(self):
        if len(self._driver.window_handles) > 0:
            self._driver.close()

