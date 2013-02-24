class NotAtPageException(Exception):

    def __init__(self, expected_page_name, at_page_name):
        self.message = 'Not at correct page. Expected "%s" but found "%s"' %\
            (expected_page_name, at_page_name)


class ElementNotFoundException(Exception):

    def __init__(self):
        self.message = 'Element not found'

    def __str__(self):
        return repr(self.message)