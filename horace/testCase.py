from unittest import TestCase
from selenium import webdriver
from test.config import driver, platform
from horace.agent import Agent


class TestCaseHorace(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = {
            'takeScreenshot': False,
            'javascriptEnabled': True,
            'browserName': driver,
            'platform': platform
        }
        cls.driver = webdriver.Remote(
            command_executor="http://localhost:5556/wd/hub",
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