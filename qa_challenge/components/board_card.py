from selene.elements import SeleneElement
from selene.support import by
from selene.support.conditions import be


class BoardCard:

    def __init__(self, element: SeleneElement):
        self.element = element
        self.title = element.s(by.css("h6"))
        self.description = element.s(by.css("div.card-body p"))
        self.like_button = \
            element.s(by.xpath(".//button[*[name()='svg' and contains(@class,'fa-thumbs-up')]]"))
        self.delete_button = \
            element.s(by.xpath(".//button[*[name()='svg' and contains(@class,'fa-times-circle')]]"))
        self.loading_circle = element.s(by.css("svg.fa-circle-notch"))

    def get_title_text(self):
        return self.title.text

    def get_description_text(self):
        return self.description.text

    def get_like_count(self):
        return int(self.like_button.text)

    def like(self):
        self.like_button.click()
        self.loading_circle.should_not_be(be.in_dom)
