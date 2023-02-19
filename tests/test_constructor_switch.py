from selenium.webdriver.common.by import By
from locators import bread_section, sauces_section, topping_section, current_tab


def testing_bread_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, sauces_section).click()
    bread_element = driver.find_element(By.XPATH, bread_section)
    bread_element.click()
    current_element = driver.find_element(By.XPATH, current_tab)
    assert bread_element.text == current_element.text


def testing_sauces_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    sauce_element = driver.find_element(By.XPATH, sauces_section)
    sauce_element.click()
    current_element = driver.find_element(By.XPATH, current_tab)
    assert sauce_element.text == current_element.text


def testing_topping_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    filling_element = driver.find_element(By.XPATH, topping_section)
    filling_element.click()
    current_element = driver.find_element(By.XPATH, current_tab)
    assert filling_element.text == current_element.text


    driver.quit()