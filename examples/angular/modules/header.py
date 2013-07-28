from horace.module import Module
from horace.contentNode import element


class TodoMVCHeader(Module):
    baseSelector = '#header'

    _content = {
        'title': element(selector='h1')
    }
