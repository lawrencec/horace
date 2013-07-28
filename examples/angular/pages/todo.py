from horace.page import Page
from horace.contentNode import content_module, element
from examples.angular.modules.todo import TodoMVC
from examples.angular.modules.footer import TodoMVCFooter
from examples.angular.modules.header import TodoMVCHeader


class TodoMVCPage(Page):
    url = 'http://todomvc.com/architecture-examples/angularjs-perf/'
    title = u'AngularJS \u2022 TodoMVC'

    _content = {
        'header': content_module(module=TodoMVCHeader),
        'footer': content_module(module=TodoMVCFooter),
        'new': element(selector='#new-todo'),
        'todo': content_module(module=TodoMVC)
    }
