from selenium.webdriver.common.keys import Keys

from horace.driver import Driver
from horace.agent import Agent

from examples.angular.pages.todo import TodoMVCPage

class TodoMVCAgent(Agent):

    def presentAndCorrect(self):
        page = self.page
        print 'Title:\n%s\n' % page.header.title.text
        print 'Title is displayed:\n%s\n' % page.header.title.displayed
        print 'Footer is displayed:\n%s\n' % page.footer.p.displayed
        print 'Footer text\n%s\n' % page.footer.text
        self._driver.delete_all_cookies()
        print 'Filters is displayed:\n%s\n' % page.todo.filters.all.displayed
        return self

    def clearAll(self):
        self._driver.execute_script('localStorage.clear()')
        return self

    def addTodo(self, item):
        page = self.page
        page.new.double_click(self._driver)
        page.new.value(item)
        print 'Entered todo is:\n%s\n' % page.new.value()
        page.new.value(Keys.RETURN)
        print 'Filters is displayed:\n%s\n' % page.todo.filters.all.displayed
        return self

    def filterBy(self, filterType):
        pass

    def printNumberOfTodos(self):
        page = self.page
        page.refresh_content('todo')

        print '\nYou have %s todo item(s)\n' % len(page.todo.list.items)
        return self

    def drive(self):
        self.to_at(TodoMVCPage)

        (self.presentAndCorrect()
            .addTodo('food')
            .printNumberOfTodos()
            .addTodo('moar food')
            .printNumberOfTodos())

        self.clearAll()
        self.close()

driver = Driver({
    'driver': 'phantomjs'
})

if __name__ == '__main__':
    TodoMVC = TodoMVCAgent(driver)
    TodoMVC.drive()