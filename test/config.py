from os import getcwd, getenv


driver = getenv('BROWSER', 'phantomjs')
platform = getenv('PLATFORM', 'MAC')

test_directory = getcwd() + '/test' if not getcwd().endswith('test') else getcwd()

html_fixture_url = 'file:///%s/fixtures/html-elements.html' % test_directory
