from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import random_str
from locators import name, email_reg, password_reg, reg_button, incorrect_pass_error
from selenium.webdriver.support import expected_conditions as ec


def testing_sign_in_home_page_button_successful_login(driver, new_user):
    new_user()
    WebDriverWait(driver, 7).until(ec.url_matches('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def testing_registration_incorrect_password_reg_error():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, name).send_keys(random_str(6))
    driver.find_element(By.XPATH, email_reg).send_keys(f'{random_str(6)}@narod.ru')
    driver.find_element(By.XPATH, password_reg).send_keys(random_str(4))
    driver.find_element(By.XPATH, reg_button).click()
    assert driver.find_element(By.XPATH, incorrect_pass_error).is_displayed()


    driver.quit()
