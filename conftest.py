import pytest
from selenium import webdriver
from constants import Constants
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():#запуск драйвера
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser

    browser.quit()

@pytest.fixture
def login_and_pass_to_cabinet(driver):#Авторизация и прохождение в Личный Кабинет
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//main//h2')))
    driver.find_element(*Locators.EMAIL).clear()
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)#Ввод почты
    driver.find_element(*Locators.PASSWORD).clear()
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)#Ввод пароля
    driver.find_element(*Locators.AUTH_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))#Обнаружение "Собери Бургер"
    driver.find_element(*Locators.CABINET_BUTTON).click()
    return driver


