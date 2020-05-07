from abc import ABC

from selene.browser import open_url, title, driver


class BasePage(ABC):

    def __init__(self):
        self.url = None

    def open(self):
        open_url(self.url)
        return self

    @staticmethod
    def get_tab_title():
        return title()

    @staticmethod
    def get_current_url():
        return driver().current_url
