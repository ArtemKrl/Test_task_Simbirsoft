import time
import pytest
from pywinauto_recorder.player import *
from selenium import webdriver


def test_main():
    driver = webdriver.Chrome()
    driver.get("https:www.google.com/")
    driver.find_element_by_css_selector("div.a4bIc > input").send_keys("Калькулятор")
    time.sleep(1)
    driver.find_element_by_css_selector("div.aajZCb > div.lJ9FBc > center > input.gNO89b").click()
    time.sleep(1)
    with Window(u"Калькулятор - Поиск в Google - Google Chrome||Pane"):
        with Region(u"Калькулятор - Поиск в Google||Document->||Group->||Table->||Table->||Custom"):
            left_click(u"1||DataItem->1||Button")
            left_click(u"умножение||DataItem")
            left_click(u"2||DataItem->2||Button")
            left_click(u"вычитание||DataItem->вычитание||Button")
            left_click(u"3||DataItem->3||Button")
            left_click(u"сложение||DataItem->сложение||Button")
            left_click(u"1||DataItem->1||Button")
        with Region(u"Калькулятор - Поиск в Google||Document->||Group->||Table->||Table->||Custom->равно||DataItem"):
            left_click(u"равно||Button")

    check_one = driver.find_element_by_css_selector("div.xwgN1d.XSNERd > div > span").text
    check_two = driver.find_element_by_css_selector("#cwos").text
    expected_result_one = "1 × 2 - 3 + 1 ="
    expected_result_two = "0"
    assert check_one == expected_result_one
    assert check_two == expected_result_two


if __name__ == "__main__":
    test_main()
