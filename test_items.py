import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_find_button(browser):
    browser.get(link)
    time.sleep(20)
    button = browser.find_element_by_css_selector("#add_to_basket_form :nth-child(3)")
    assert button.get_attribute("disable") is None, "Кнопка должна сущестовать и не быть заблокированной"

