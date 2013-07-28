from examples.angular.modules.filters import TodoMVCFilters
from examples.angular.modules.list import TodoMVCList
from horace.contentNode import element, content_module
from horace.module import Module


class TodoMVC(Module):
    baseSelector = '#main'

    _content = {
        'toggleAllButton': element('input#toggle-all'),
        'toggleAllButtonLabel': element('label[for="toggle-all"]'),
        'list': content_module(module=TodoMVCList),
        'filters': content_module(module=TodoMVCFilters)
    }