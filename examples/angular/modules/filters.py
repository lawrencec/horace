from horace.module import Module
from horace.contentNode import element


class TodoMVCFilters(Module):
    baseSelector = '#filters'

    _content = {
        'all': element(selector='li:nth-child(1)'),
        'active': element(selector='li:nth-child(2)'),
        'completed': element(selector='li:nth-child(3)'),
    }