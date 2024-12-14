import allure
from selene import by, be, browser
from selene.support.shared.jquery_style import s
from confest import browser_management

REPO_NAME = "eroshenkoam/allure-example"


def test_steps(browser_management):
    expected_result = "Тестируем тест"

    with allure.step("Клик на инпут ввода"):
        s('[class="search-input"]').click()

    with allure.step("Поиск репозитория"):
        s('[id="query-builder-test"]').send_keys(REPO_NAME).submit()

    with allure.step("Клик на найденный репозиторий"):
        s(by.link_text(REPO_NAME)).click()

    with allure.step("Клик на таб issues"):
        s("#issues-tab").click()

    with allure.step(f"Проверка отображения {expected_result} на странице"):
        s(by.partial_text(expected_result)).should(be.visible)
