from horace.contentNode import content_module, content_module_list, element
from horace.module import IFrameModule
from test.CSSTest.modules.table import TableModule, TableRowModule


class IFrame(IFrameModule):
    baseSelector = '#anIFrame'

    _content = {
        'headingTwoForIframe': element(selector='h2'),
        'table': content_module(module=TableModule),
        'rows': content_module_list(module=TableRowModule, selector='tr')
    }