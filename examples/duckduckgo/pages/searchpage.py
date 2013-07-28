from horace.page import Page
from horace.contentNode import element
import re


class DuckDuckGoSearchPage(Page):
    url = '^https://www.duckduckgo.com?q='
    title = 'DuckDuckGo'

    _content = {
        'logo': element(selector='#logo_homepage_link', required=False),
        'links': element(
            selector='div[class="results_links_deep highlight_d2"]'
        )
    }

    def at(self, title):
        return re.search('at DuckDuckGo$', title)
