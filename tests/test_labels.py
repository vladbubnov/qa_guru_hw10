import allure
from selene import by, be, browser
from selene.support.shared.jquery_style import s
from confest import browser_management

REPO_NAME = "eroshenkoam/allure-example"


@allure.tag('web')
@allure.feature("Задачи в репозитории")
@allure.story("Проверка Issue")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест для проверки поиска текста на странице")
@allure.link("https://github.com", name="Testing")
def test_labels(browser_management):
    expected_result = "Тестируем тест"

    @allure.step("Поиск репозитория")
    def search_for_repository(repo):
        s('[class="search-input"]').click()

        s('[id="query-builder-test"]').send_keys(repo).submit()

    @allure.step("Клик на найденный репозиторий")
    def open_repository(repo):
        s(by.link_text(repo)).click()

    @allure.step("Клик на таб issues")
    def open_issue_tab():
        s("#issues-tab").click()

    @allure.step(f"Проверка отображения {expected_result} на странице")
    def should_displayed_text(name):
        s(by.partial_text(name)).should(be.visible)

    search_for_repository(REPO_NAME)
    open_repository(REPO_NAME)
    open_issue_tab()
    should_displayed_text(expected_result)