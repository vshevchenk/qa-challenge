from abc import ABC

from selene.browser import open_url, title, driver


class BasePage(ABC):

    def __init__(self):
        self.url = None

    def open(self):
        open_url(self.url)
        return self

    def get_tab_title(self):
        return title()

    def get_current_url(self):
        return driver().current_url
