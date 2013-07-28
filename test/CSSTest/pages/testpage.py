from horace.contentNode import content_module, element
from horace.page import Page
from test.config import html_fixture_url
from test.CSSTest.modules.iframe import IFrame
from test.CSSTest.modules.table import TableModule
from test.CSSTest.modules.paragraph import ParagraphSectionModule


class CSSTestPage(Page):
    url = html_fixture_url
    title = 'Horace Test Page'

    _content = {
        'paragraphSection': content_module(
            module=ParagraphSectionModule,
            required=True
        ),
        'headingTwos': element(selector='h2'),
        'anIFrame': content_module(module=IFrame),
        'table': content_module(module=TableModule)
    }

    # Setting properties via the @property decorator is purely optional but it
    # helps in providing code assistance in IDES or python console
    # @property
    # def paragraphSection(self):
    #     return self._getContent('paragraphSection')
