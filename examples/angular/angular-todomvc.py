from horace.driver import Driver
from horace.agent import Agent
from horace.page import Page
from horace.module import Module
from horace.contentNode import element, content_module, content_module_list
from selenium.webdriver.common.keys import Keys


class TodoMVCFooter(Module):
    baseSelector = '#info'

    _content = {
        'p': element(selector='p')
    }


class TodoMVCHeader(Module):
    baseSelector = '#header'

    _content = {
        'title': element(selector='h1')
    }


class TodoMVCItem(Module):
    _content = {
        'label': element(selector='li label'),
        'destroyButton': element(selector='li button.destroy'),
    }


class TodoMVCList(Module):
    baseSelector = '#todo-list'

    _content = {
        'items': content_module_list(module=TodoMVCItem, selector='li', required=False)
    }


class TodoMVCFilters(Module):
    baseSelector = '#filters'

    _content = {
        'all': element(selector='li:nth-child(1)'),
        'active': element(selector='li:nth-child(2)'),
        'completed': element(selector='li:nth-child(3)'),
    }


class TodoMVC(Module):
    baseSelector = '#main'

    _content = {
        'toggleAllButton': element('input#toggle-all'),
        'toggleAllButtonLabel': element('label[for="toggle-all"]'),
        'list': content_module(module=TodoMVCList),
        'filters': content_module(module=TodoMVCFilters)
    }

class TodoMVCPage(Page):
    url = 'http://todomvc.com/architecture-examples/angularjs-perf/'
    title = u'AngularJS \u2022 TodoMVC'

    _content = {
        'header': content_module(module=TodoMVCHeader),
        'footer': content_module(module=TodoMVCFooter),
        'new': element(selector='#new-todo'),
        'todo': content_module(module=TodoMVC)
    }


class TodoMVCAgent(Agent):

    def presentAndCorrect(self, page):
        if not page:
            page = self.page
        print 'Title:\n%s\n' % page.header.title.text
        print 'Title is displayed:\n%s\n' % page.header.title.displayed
        print 'Footer is displayed:\n%s\n' % page.footer.p.displayed
        print 'Footer text\n%s\n' % page.footer.text
        # self._driver.delete_all_cookies()
        print 'Filters is displayed:\n%s\n' % page.todo.filters.all.displayed

    def clearAll(self):
        self._driver.execute_script('return localStorage.clear()')

    def addTodo(self, page, item):
        if not page:
            page = self.page
        page.new.double_click(self._driver)
        page.new.value(item)
        print 'Entered todo is:\n%s\n' % page.new.value()
        page.new.value(Keys.RETURN)
        print 'Filters is displayed:\n%s\n' % page.todo.filters.all.displayed

    def filterBy(self, filterType):
        pass

    def printNumberOfTodos(self, page):
        page.refresh_content('todo')
        if not page:
            page = self.page
        print '\nYou have %s todo item(s)\n' % len(page.todo.list.items)

    def drive(self):
        self.to_at(TodoMVCPage).do(
            self.presentAndCorrect)\
            .do(self.addTodo, 'food')\
            .do(self.printNumberOfTodos)\
            .do(self.addTodo, 'moar food')\
            .do(self.printNumberOfTodos)

        self.clearAll()
        self.close()

driver = Driver({
    'driver': 'phantomjs'
})

if __name__ == '__main__':
    TodoMVC = TodoMVCAgent(driver)
    TodoMVC.drive()