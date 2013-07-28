from horace.module import Module
from horace.contentNode import element


class TodoMVCItem(Module):
    _content = {
        'label': element(selector='li label'),
        'destroyButton': element(selector='li button.destroy'),
    }