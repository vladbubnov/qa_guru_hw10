from selene import by, be, browser
from selene.support.shared.jquery_style import s
from confest import browser_management

REPO_NAME = "eroshenkoam/allure-example"


def test_selene(browser_management):
    s('[class="search-input"]').click()
    s('[id="query-builder-test"]').send_keys(REPO_NAME).submit()
    s(by.link_text(REPO_NAME)).click()
    s("#issues-tab").click()
    s(by.partial_text("Тестируем тест")).should(be.visible)
