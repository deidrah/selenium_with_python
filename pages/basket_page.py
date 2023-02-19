import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Constant:
    MOST_WANTED_BUTTON = (By.XPATH, "//*[@id='menu-item-128']/a")
    AD_MAGNOLIA_BUTTON = (By.XPATH, "//*[@id='page']/div/div/div[2]/div/ul/li[2]/a[2]")
    MY_CARD_BUTTON = (By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    INITIAL_VALUE = (By.XPATH, "//div[@class='quantity']//input[@type='number']")
    PLUS_BUTTON = (By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[5]/div/div/a[2]')
    UPDATE_BUTTON = (By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[2]/td/input[1]')
    FINAL_VALUE = (By.XPATH, "//div[@class='quantity']//input[@type='number']")


def add_to_basket(web_driver):
    web_driver.find_element(*Constant.MOST_WANTED_BUTTON).click()
    time.sleep(2)
    web_driver.find_element(*Constant.AD_MAGNOLIA_BUTTON).click()
    time.sleep(2)
    web_driver.find_element(*Constant.MY_CARD_BUTTON).click()
    time.sleep(2)
    initial_value = web_driver.find_element(*Constant.INITIAL_VALUE).get_attribute('value')
    initial_value_value_int = int(initial_value)
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constant.PLUS_BUTTON))
    plus_button = web_driver.find_element(*Constant.PLUS_BUTTON)
    plus_button.click()
    time.sleep(1)
    plus_button.click()
    time.sleep(1)
    web_driver.find_element(*Constant.UPDATE_BUTTON).click()
    time.sleep(1)
    final_value = int(web_driver.find_element(*Constant.FINAL_VALUE).get_attribute('value'))
    time.sleep(1)
    return [initial_value_value_int, final_value]