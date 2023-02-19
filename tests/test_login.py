from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import login_button, email_reg, password_reg, sign_in_button, main_page_title, pa_button, button_reg_form, button_rec_password


def testing_main_psge_sign_in_button_successful_login(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_sign_in_pa_button_successful_login(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, pa_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_sign_in_button_reg_form_successful_login(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, button_reg_form).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_sign_in_from_password_recovery_form(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, button_rec_password).click()
    driver.find_element(By.XPATH, button_reg_form).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    driver.quit()
