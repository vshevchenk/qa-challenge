from typing import Optional

from selene.support import by
from selene.support.jquery_style_selectors import s, ss

from qa_challenge.components.board_card import BoardCard
from qa_challenge.pages.base_logged_in_page import BaseLoggedInPage


class BoardsPage(BaseLoggedInPage):
    def __init__(self):
        super().__init__()
        self.url = "https://sprintboards.io/boards"

        self.green_plus = s(by.css("button.text-success>svg[data-icon=plus-circle]"))
        self.red_plus = s(by.css("button.text-danger>svg[data-icon=plus-circle]"))

        self.add_card_modal = s(by.css("#add-card-modal"))
        self.add_card_title = s(by.xpath("//div[h5[text()=\"Title\"]]//input"))
        self.add_card_description = s(by.xpath("//div[h5[text()=\"Description\"]]//textarea"))
        self.add_card_button = s(by.css("div.modal-footer button"))

        self.red_cards = ss(by.css("div.card.border-danger"))
        self.green_cards = ss(by.css("div.card.border-success"))

        self.modal_title = s(by.css("div.modal-title"))
        self.modal_body = s(by.css("div.modal-body"))
        self.modal_confirm_button = s(by.css("div.modal-footer button.btn-danger"))

    def create_card(self, title: str, description: Optional[str] = None):
        self.add_card_title.set(title)
        if description:
            self.add_card_description.set(description)
        self.add_card_button.click()

    def get_last_green_card(self):
        return BoardCard(self.green_cards[-1])

    def get_last_red_card(self):
        return BoardCard(self.red_cards[-1])
