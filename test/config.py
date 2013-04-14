from os import getcwd


driver = 'phantomjs'
# driver = 'firefox'
# driver = 'chrome'

test_directory = getcwd() + '/test' if not getcwd().endswith('test')  else getcwd()

html_fixture_url = 'file:///%s/fixtures/html-elements.html' % test_directory
