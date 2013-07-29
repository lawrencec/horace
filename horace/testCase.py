from unittest import TestCase
from horace.driver import Driver
from test.config import driver, platform
from horace.agent import Agent


class TestCaseHorace(TestCase):

    def setUp(self):
        agentDriver = Driver({
            'driver': driver,
            'platform': platform
        })
        self.agent = Agent(agentDriver)

    def tearDown(self):
        self.agent.close()

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