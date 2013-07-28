from horace.module import Module
from horace.contentNode import element


class DuckDuckGoFormModule(Module):
    baseSelector = '#search_form_homepage'

    _content = {
        'input': element(selector='#search_form_input_homepage'),
        'select': element(selector='#bang'),
        'submit': element(selector='#search_button_homepage')
    }