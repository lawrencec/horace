from unittest import TestCase
from selenium import webdriver
import config
from horace.agent import Agent

drivers = dict(firefox=webdriver.Firefox, chrome=webdriver.Chrome)


class HoraceTestCase(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = {
            'takeScreenshot': False,
            'javascriptEnabled': True
        }
        if config.driver in drivers:
            cls.driver = drivers[config.driver]()
        else:
            cls.driver = webdriver.Remote(
                command_executor="http://localhost:8910/wd/hub",
                desired_capabilities=caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver = None

    def setUp(self):
        self.driver = self.__class__.driver
        self.agent = Agent(self.driver)

    def tearDown(self):
        self.driver = None

    def to(self, page, **kwargs):
        self.agent.to(page, kwargs)

    def at(self, page, **kwargs):
        self.agent.at(page, kwargs)

    def to_at(self, page, **kwargs):
        self.agent.to_at(page, kwargs)

    def __getattr__(self, item):
        if item == 'page':
            return self.agent.page
        elif item == '_driver':
            return self.agent._driver
        else:
            return object.__getattribute__(self, item)