from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Constant:
    PAGE_TITLE = (By.XPATH, "//h1[@class='page-title']/span")
    SEARCH_BOX_INPUT = (By.ID, "search-field-top-bar")


def check_page_title(web_driver):
    search_box = web_driver.find_element(*Constant.SEARCH_BOX_INPUT)
    search_box.send_keys('Black top')
    search_box.submit()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.PAGE_TITLE))
    page_title = web_driver.find_element(*Constant.PAGE_TITLE).text
    return page_title
