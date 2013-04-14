# Horace

A page object based interface around webdriver to help with automating of browser
navigation, screen scraping and testing. Inspired by [Geb](http://gebish.org).
A simple example usage can be seen below:

    # Go to www.duckduckgo.com
    ddgPage = DuckDuckGoPage(driver)

    # Enter a query into the search box
    ddgPage.searchModule.searchInput.value('my search query')

## Pages and Modules

Page content is specified using lists. The keys in that list can then be directly
used as attributes for the page objects.

    class DuckDuckGoPage(Page):
        url = 'http://duckduckgo.com/'
        title = 'DuckDuckGo'

        content = {
            'searchModule' : {
                'base': searchModule, #module
                'required': False
            }
        }

    class SearchModule(Module):
        base = '#search_wrapper_homepage'
        required = True

        content = {
            'searchInput': {'selector': '#search_form_input_homepage'}
        }

Usage of the above Page and Module:

    # Go to www.duckduckgo.com
    ddgPage = DuckDuckGoPage(driver)

    # Enter a query into the search box
    ddgPage.searchModule.searchInput.value('my search query')

Optionally, you can explicitly define a property using the @property decorator
in order to help with code completion tools in python consoles and IDE's:

    @property
    def searchModule(self):
        return self._getContent('searchModule')

## Examples

See the DuckDuckGo and Angular examples in the test directory. You'll probably need to install Horace first via python
setup.py or pip.

The DDG example performs a search query on the DDG home page and then shows how many search results were found.

The Angular example loads up the ToDoMVC angular page and adds two todo items to the todo list.

Both examples only tested and phantomjs and Firefox so far (Mac).

## Tests

The tests require an install of firefox or phantomjs. The test/config.py file
by default states phantomjs as the default browser to use. Change it to firefox
if you don't have phantomjs installed.

If you have phantomjs installed, first run it in webdriver mode:

    phantomjs --webdriver=8910
    
Tests can be run using nose like so:

    cd tests
    nosetests

with coverage if you have [coverage.py](http://nedbatchelder.com/code/coverage/) installed

    nosetests --with-coverage --cover-package=horace

or if you want a html coverage report:

    nosetests --with-coverage --cover-html --cover-html-dir=./coverage --cover-erase --cover-package=horace

## Why Horace?

As this project is inspired by [Geb](http://gebish.org) and as Geb is apparently
named after an Egytpian god, I thought it would be nice if I named this project in
a similar vein. A god-based name is out of the question so I thought
I'd name it after my favourite god-based quote. The quote,
['Deus ex machina'](http://en.wikipedia.org/wiki/Deus_ex_machina) comes from the
Roman poet [Horace's](http://en.wikipedia.org/wiki/Horace) book about writing poetry
where he instructs poets to not invoke an outside plot device or
'god from the machine' to solve insoluble plot problems. As this project
is about control and automation, I thought it was an apt name (despite the
tenuous link).

The fact that one of my favourite games happens to be called 'Deus Ex' (the original!)
is purely coincidental.
