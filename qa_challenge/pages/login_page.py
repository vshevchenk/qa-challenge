from selene.support import by
from selene.support.jquery_style_selectors import s

from qa_challenge.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url = "https://sprintboards.io/auth/login"

        self.email = s(by.css("[type=email]"))
        self.password = s(by.css("[type=password]"))
        self.login_button = s(by.css("[type=submit]"))

    def login(self, email: str, password: str):
        self.email.set(email)
        self.password.set(password)
        self.login_button.click()
