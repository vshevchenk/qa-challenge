from typing import Optional

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from qa_challenge.components.header_menu import HeaderMenu
from qa_challenge.pages.base_page import BasePage
from qa_challenge.pages.login_page import LoginPage


class BaseLoggedInPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header_menu = HeaderMenu()

    def open(self, email: Optional[str] = None, password: Optional[str] = None):
        if self.get_current_url() != self.url:
            super().open()
        if email is not None and password is not None:
            try:
                self.header_menu.account_dropdown.is_displayed()
            except (NoSuchElementException, TimeoutException):
                LoginPage().open().login(email, password)
                self.header_menu.account_dropdown.is_displayed()
                if self.get_current_url() != self.url:
                    super().open()
