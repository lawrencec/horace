from horace.contentNode import content_module_list, element
from horace.module import Module


class TableRowModule(Module):
    _content = {
        'data': element(selector='td', required=False)
    }


class TableModule(Module):
    baseSelector = 'table'
    required = True

    _content = {
        'rows': content_module_list(module=TableRowModule, selector='tr')
    }