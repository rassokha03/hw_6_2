from selene import browser
from selene import be, have


def test_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print("По запросу найдена ссылка")


def test_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dwadwaodj313').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("По запросу ничего не найдено")