from examples.angular.modules.todoitem import TodoMVCItem
from horace.contentNode import content_module_list
from horace.module import Module


class TodoMVCList(Module):
    baseSelector = '#todo-list'

    _content = {
        'items': content_module_list(module=TodoMVCItem, selector='li', required=False)
    }
