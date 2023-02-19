from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import login_button, email_reg, password_reg, sign_in_button, pa_button, button_profile, button_constructor, logo, button_log_out, button_for_placing_an_order


def testing_click_through_to_your_pa(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_from_pa_to_constructor(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, pa_button)))
    driver.find_element(By.XPATH, pa_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, button_constructor)))
    driver.find_element(By.XPATH, button_constructor).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_from_pa_to_logo(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, pa_button)))
    driver.find_element(By.XPATH, pa_button).click()
    driver.find_element(By.XPATH, logo).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def testing_logout_of_pa_successful_logout(driver, new_user):
    email, password = new_user()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_reg).send_keys(email)
    driver.find_element(By.XPATH, password_reg).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, pa_button)))
    driver.find_element(By.XPATH, pa_button).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, button_profile)))
    driver.find_element(By.XPATH, button_log_out).click()
    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, sign_in_button)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    driver.quit()