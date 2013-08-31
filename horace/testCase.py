from os import getenv
from unittest import TestCase
from horace.driver import Driver
from horace.agent import Agent


class TestCaseHorace(TestCase):

    def setUp(self):
        agentDriver = Driver({
            'driver': getenv('BROWSER', 'phantomjs'),
            'platform': getenv('PLATFORM', 'ANY')
        })
        self.agent = Agent(agentDriver)

    def tearDown(self):
        self.agent.close()

    def to(self, page, path=None, parameters=None):
        self.agent.to(page, path, parameters)

    def at(self, page):
        self.agent.at(page)

    def to_at(self, page, path=None, parameters=None):
        self.agent.to_at(page, path, parameters)

    def __getattr__(self, item):
        if item == 'page':
            return self.agent.page
        elif item == '_driver':
            return self.agent._driver
        else:
            return object.__getattribute__(self, item)