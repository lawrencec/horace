from horace.page import Page


class TodoMVCPage(Page):
    url = 'http://todomvc.com'
    title = 'TodoMVC'

    def get_applist(self):
        appList = []
        applistLinks = self.get_elements_by_selector('.applist li a')
        for app in applistLinks:
            appList.append(app.get_attribute('href'))
        return appList
