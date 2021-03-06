from horace.agent import Agent
from horace.exceptions import NotAtPageException
from utils import HoraceTestObject
from DDG.pages.homepage import DuckDuckGoPage
from CSSTest.pages.testpage import CSSTestPage
from CSSTest.pages.unknownpage import UnknownTestPage


class TestAgent(HoraceTestObject):

    def test_to(self):
        agent = Agent(self.driver)
        agent.to(DuckDuckGoPage)
        self.assertNotEqual(self.driver.current_url, CSSTestPage.url)
        agent.to(CSSTestPage)
        # have to split on final directory as chrome has file:/// instead of file://// (like firefox and phantomjs)
        self.assertTrue(self.driver.current_url.split('fixtures/')[1].endswith(CSSTestPage.url.split('fixtures/')[1]))

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
                'Not at correct page. Expected "unknown" but found "Search DuckDuckGo"',
                e.message
            )
        self.assertRaises(Exception, agent.at, UnknownTestPage)

    def test_toAt(self):
        agent = Agent(self.driver)
        agent.to_at(DuckDuckGoPage)
        self.assertTrue(DuckDuckGoPage.title, self.driver.title)

    def test_currentPage(self):
        agent = Agent(self.driver)
        agent.to_at(DuckDuckGoPage)
        self.assertIsInstance(agent.page, DuckDuckGoPage)

    def test_get_attribute(self):
        agent = Agent(self.driver)
        try:
            agent.foo
        except AttributeError, e:
            self.assertEquals(
                "'Agent' object has no attribute 'foo'",
                e.message
            )

    def test_wait_timeout(self):
        agent = Agent(self.driver)
        DuckDuckGoPage.wait = 1
        DuckDuckGoPage.title = "Incorrect title to trigger exception"
        agent.to(DuckDuckGoPage)
        try:
            agent.at(DuckDuckGoPage)
            self.fail("Didn't raise Exception")
        except NotAtPageException, e:
            pass
        self.assertRaises(Exception, agent.at, DuckDuckGoPage)

    def test_do_calls_callable_correctly(self):
        agent = Agent(self.driver)
        agent.foo = 0

        def my_func(page):
            agent.foo = 1
        CSSTestPage.wait = 5
        agent.to_at(CSSTestPage)
        agent.then(my_func)
        self.assertEquals(agent.foo, 1)

    def test_do_does_not_call_an_uncallable(self):
        agent = Agent(self.driver)
        agent.foo = 0
        agent.to_at(CSSTestPage)
        agent.then(1)
        self.assertEquals(agent.foo, 0)
