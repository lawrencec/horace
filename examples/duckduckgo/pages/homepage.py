from horace.page import Page
from horace.contentNode import element, content_module
from examples.duckduckgo.modules.form import DuckDuckGoFormModule
from examples.duckduckgo.modules.footer import DuckDuckGoFooterModule


class DuckDuckGoHomePage(Page):
    url = 'https://www.duckduckgo.com'
    title = 'Search DuckDuckGo'

    _content = {
        'logo': element(selector='#logo_homepage_link'),
        'form': content_module(module=DuckDuckGoFormModule),
        'footer': content_module(module=DuckDuckGoFooterModule)
    }