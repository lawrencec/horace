from horace.contentNode import element
from horace.module import Module


class ParagraphSectionModule(Module):
    baseSelector = '#paragraphsSection'
    required = True

    _content = {
        'paragraphs': element(selector='p', required=False)
    }