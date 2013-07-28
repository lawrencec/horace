from horace.contentNode import element
from horace.page import Page
from test.config import html_fixture_url


class CSSTestPageWithMissingRequiredElements(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'hardbreaks': element(selector='br', required=True)
    }