import string
import pytest
import random


from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import name, email_reg, password_reg, reg_button


def random_str(lenght):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(lenght))


@pytest.fixture
def driver():
    return webdriver.Chrome()


@pytest.fixture()
def new_user(driver):
    def create():
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, name).send_keys(random_str(9))
        email = f'{random_str(9)}@narod.ru'
        driver.find_element(By.XPATH, email_reg).send_keys(email)
        password = random_str(9)
        driver.find_element(By.XPATH, password_reg).send_keys(password)
        driver.find_element(By.XPATH, reg_button).click()
        return email, password
    return create


