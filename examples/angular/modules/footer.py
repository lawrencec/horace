from horace.contentNode import element
from horace.module import Module


class TodoMVCFooter(Module):
    baseSelector = '#info'

    _content = {
        'p': element(selector='p')
    }