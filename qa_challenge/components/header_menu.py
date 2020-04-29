from selene.support import by
from selene.support.jquery_style_selectors import s


class HeaderMenu():
    def __init__(self):
        self.text_center = s(by.css(".text-center"))
        self.account_dropdown = s(by.css("#account-dropdown"))
        self.create_board = s(by.xpath("//li[a/text()=\"Create Board\"]"))
