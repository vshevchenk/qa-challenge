from qa_challenge.pages.base_logged_in_page import BaseLoggedInPage


class HomePage(BaseLoggedInPage):
    def __init__(self):
        super().__init__()
        self.url = "https://sprintboards.io/"
