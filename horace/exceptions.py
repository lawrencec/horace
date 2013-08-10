class NotAtPageException(Exception):

    def __init__(self, expected_page_name, at_page_name):
        self.message = 'Not at correct page. Expected "%s" but found "%s"' %\
            (expected_page_name, at_page_name)

    def __str__(self):
        return repr(self.message)


class ElementNotFoundException(Exception):

    def __init__(self, selector):
        self.message = 'Element not found (%s)' % selector

    def __str__(self):
        return repr(self.message)


class JavascriptExecutionException(Exception):
    def __init__(self, message):
        self.message = 'Error executing javascript: %s' % message

    def __str__(self):
        return repr(self.message)