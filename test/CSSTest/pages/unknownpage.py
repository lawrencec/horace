from horace.page import Page


class UnknownTestPage(Page):
    url = 'must404.html'
    title = 'unknown'

    def at(self, title):
        return None
