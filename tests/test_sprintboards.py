from selene.support.conditions import be

from qa_challenge.model.credentials import Credentials
from qa_challenge.pages.boards_page import BoardsPage
from qa_challenge.pages.create_board_page import CreateBoardPage
from qa_challenge.pages.home_page import HomePage
from qa_challenge.pages.login_page import LoginPage

login_page = LoginPage()
home_page = HomePage()
create_board_page = CreateBoardPage()
boards_page = BoardsPage()


def test_login(credentials: Credentials):
    login_page.open()
    login_page.login(credentials.email, credentials.password)
    assert home_page.header_menu.account_dropdown.is_displayed()


def test_navigate_to_create_board(credentials: Credentials):
    home_page.open(credentials.email, credentials.password)
    home_page.header_menu.create_board.click()
    assert create_board_page.get_title_text() == "Create a Board"
    assert create_board_page.get_current_url() == create_board_page.url


def test_create_board(credentials: Credentials):
    create_board_page.open(credentials.email, credentials.password)
    create_board_page.create_board("My first board", "Sennder")
    assert create_board_page.get_popup_text() == "Created"
    assert boards_page.green_plus.is_displayed()
    assert boards_page.url in boards_page.get_current_url()


def test_board_cards_crud(credentials: Credentials):
    create_board_page.open(credentials.email, credentials.password)
    create_board_page.create_board("My first board", "Sennder")
    boards_page.green_plus.is_displayed()

    boards_page.green_plus.click()
    boards_page.add_card_modal.is_displayed()
    boards_page.create_card("Goal was achieved", "Sprint was well planned")
    boards_page.add_card_modal.should_not_be(be.visible)
    last_green_card = boards_page.get_last_green_card()
    assert last_green_card.get_title_text() == "Goal was achieved"
    assert last_green_card.get_description_text() == "Sprint was well planned"

    boards_page.red_plus.click()
    boards_page.create_card("Goal was not achieved")
    boards_page.add_card_modal.should_not_be(be.visible)
    last_red_card = boards_page.get_last_red_card()
    assert last_red_card.get_title_text() == "Goal was not achieved"
    assert last_red_card.get_description_text() == "No description provided."

    original_likes = last_green_card.get_like_count()
    last_green_card.like()
    assert last_green_card.get_like_count() - original_likes == 1

    last_red_card.delete_button.click()
    assert boards_page.modal_title.text == "Delete Card"
    assert boards_page.modal_body.text == "Are you sure you want to continue?"
    boards_page.modal_confirm_button.click()
    assert last_red_card.element.should_not_be(be.in_dom)
