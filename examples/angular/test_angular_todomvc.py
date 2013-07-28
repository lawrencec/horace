from selenium.webdriver.common.keys import Keys

from examples.angular.pages.todo import TodoMVCPage
from horace.testCase import TestCaseHorace


class TestFoo(TestCaseHorace):

    def test_add_multiple_todos(self):

        self.to_at(TodoMVCPage)
        (self.presentAndCorrect()
            .addTodo('food')
            .addTodo('moar food')
            .assertTodosArePersistedAfterReload())

        self.clearAll()

    def presentAndCorrect(self):
        page = self.page

        self.assertEquals(page.header.title.text, 'todos')
        self.assertTrue(page.header.title.displayed)
        self.assertTrue(page.footer.p.displayed)
        self._driver.delete_all_cookies()
        self.assertFalse(page.todo.filters.all.displayed)
        self.assertEquals(page.footer.text, 'Double-click to edit a todo\nCredits: Christoph Burgdorf, Eric Bidelman, Jacob Mumm and Igor Minar\nPart of TodoMVC')

        return self

    def clearAll(self):
        self._driver.execute_script('return localStorage.clear()')
        return self

    def addTodo(self, item):
        page = self.page
        page.new.double_click(self._driver)
        page.new.value(item)
        self.assertEquals(page.new.value(), item)
        page.new.value(Keys.RETURN)
        self.assertTrue(page.todo.filters.all.displayed)
        return self

    def assertTodosArePersistedAfterReload(self):
        page = self.page
        page.refresh_content('todo')
        self.assertEquals(len(page.todo.list.items), 2)
        return self