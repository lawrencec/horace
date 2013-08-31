from os import getcwd, getenv


# driver = getenv('BROWSER', 'phantomjs')

test_directory = getcwd() + '/test' if not getcwd().endswith('test') else getcwd()

html_fixture_url = 'file:///%s/fixtures/html-elements.html' % test_directory
js_fixture_url = 'file:///%s/fixtures/js-test.html' % test_directory
