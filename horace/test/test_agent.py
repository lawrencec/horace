from horace.agent import Agent
from horace.exceptions import NotAtPageException
from utils import TestObject, CSSTestPage, DuckDuckGoPage, UnknownTestPage


class TestAgent(TestObject):

    def test_to(self):
        agent = Agent(self.driver)
        agent.to(DuckDuckGoPage)
        self.assertNotEqual(self.driver.current_url, CSSTestPage.url)
        agent.to(CSSTestPage)
        self.assertTrue(self.driver.current_url.endswith(CSSTestPage.url))

    def test_at(self):
        agent = Agent(self.driver)
        agent.to(DuckDuckGoPage)
        agent.at(DuckDuckGoPage)
        self.assertEquals(DuckDuckGoPage.title, self.driver.title)

    def test_at_raises_exception_if_not_at_correct_page(self):
        agent = Agent(self.driver)
        agent.to(DuckDuckGoPage)
        try:
            agent.at(UnknownTestPage)
            self.fail("Didn't raise Exception")
        except NotAtPageException, e:
            self.assertEquals(
                'Not at correct page. Expected "unknown" but found "DuckDuckGo"',
                e.message
            )
        self.assertRaises(Exception, agent.at, UnknownTestPage)

    def test_toAt(self):
        agent = Agent(self.driver)
        agent.toAt(DuckDuckGoPage)
        self.assertTrue(DuckDuckGoPage.title, self.driver.title)

    def test_currentPage(self):
        agent = Agent(self.driver)
        agent.toAt(DuckDuckGoPage)
        self.assertIsInstance(agent.page, DuckDuckGoPage)

    def test_close(self):
        agent = Agent(self.driver)
        agent.close()
        self.assertEqual(len(agent._driver.window_handles), 0)

    def test_get_attribute(self):
        agent = Agent(self.driver)
        try:
            agent.foo
        except AttributeError, e:
            self.assertEquals(
                "'Agent' object has no attribute 'foo'",
                e.message
            )



