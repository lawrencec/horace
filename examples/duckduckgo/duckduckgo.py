from horace.driver import Driver
from horace.agent import Agent
from examples.duckduckgo.pages.homepage import DuckDuckGoHomePage
from examples.duckduckgo.pages.searchpage import DuckDuckGoSearchPage


class DuckDuckGoAgent(Agent):

    def drive(self):
        searchTerm = 'deus ex machina'
        self.to_at(DuckDuckGoHomePage)
        self.page.form.input.value(searchTerm)
        self.page.form.submit.click()
        self.at(DuckDuckGoSearchPage)
        print 'Found %s links for "%s"' % (len(self.page.links), searchTerm)
        self.close()

driver = Driver({
    'driver': 'phantomjs',
    'platform': 'MAC'
})

if __name__ == '__main__':
    DDG = DuckDuckGoAgent(driver)
    DDG.drive()
