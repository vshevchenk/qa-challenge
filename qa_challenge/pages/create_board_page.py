from selene.support import by
from selene.support.jquery_style_selectors import s
from selenium.webdriver.support.select import Select

from qa_challenge.pages.base_logged_in_page import BaseLoggedInPage


class CreateBoardPage(BaseLoggedInPage):
    def __init__(self):
        super().__init__()
        self.url = "https://sprintboards.io/boards/create"

        self.title = s(by.css("h1"))
        self.session_name = s(by.css("[placeholder=\"Session Name\"]"))
        self.owner = s(by.css(".custom-select"))
        self.create_board_button = s(by.css("[type=submit]"))
        self.popup_title = s(by.css(".swal-title"))

    def get_title_text(self):
        return self.title.text

    def create_board(self, session_name: str, owner: str):
        self.session_name.set(session_name)
        self.select_owner(owner)
        self.create_board_button.click()

    def select_owner(self, owner: str):
        Select(self.owner).select_by_visible_text(owner)

    def get_popup_text(self):
        return self.popup_title.text
