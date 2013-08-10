from horace.contentNode import element
from horace.page import Page
from test.config import js_fixture_url


class JSTestPage(Page):
    url = js_fixture_url
    title = 'JS Test Page'

    _content = {
        'body': element('#jsTestPage')
    }
