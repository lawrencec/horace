from horace.module import Module
from horace.contentNode import element


class DuckDuckGoFooterModule(Module):
    baseSelector = '#footer_homepage'

    _content = {
        'title': element(selector='#footer_homepage_left')
    }