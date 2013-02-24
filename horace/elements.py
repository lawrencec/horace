from horace.element import Element


class Elements(object):

    def __init__(self, elements):
        self._elements = []
        for elem in elements:
            self._elements.append(Element(elem))
        #((list(Element(elem))) for elem in elements)

    def __getitem__(self, key):
        return self._elements[key]

    def __len__(self):
        return len(self._elements)

    def __getattr__(self, item):
        valid_keys = Element.__dict__.keys()
        valid_keys.append('_element')
        if item in valid_keys:
            return Element.__dict__[item].__get__(self._elements[0])
        else:
            object.__getattribute__(self, item)