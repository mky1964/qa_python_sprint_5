
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class TestSBurgerslogin:
    def test_login_in_accaunt(self, driver): #Позитивный тест на авторизацию через кнопку "Войти в Аккаунт" с переходом в Личный Кабинет по клику
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//main//h2')))#найти кнопку "Войти"
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == 'kirillmakshinskykag7123@yandex.ru' #Проверка Email в личном кабинете

    def test_login_via_cabinet(self,driver):#Позитивный тест на авторизацию через кнопку "Личный кабинет"
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//main//h2')))#найти кнопку "Войти"
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == 'kirillmakshinskykag7123@yandex.ru' #Проверка Email в личном кабинете

    def test_login_via_registr_form(self, driver):#Позитивный тест на авторизацию через кнопку Формы Регистрации
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//main//h2')))#найти кнопку "Войти"
        driver.find_element(By.XPATH, '//a[@href="/register"]').click()#Переход по кнопке "Зарегистрироваться"
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()#Переход по кнопке "Войти" в форму авторизации
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == 'kirillmakshinskykag7123@yandex.ru' #Проверка Email в личном кабинете

    def test_login_via_restore_button(self,driver):#Позитивный тест на авторизацию через кнопку Восстановления пароля
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//main//h2')))#найти кнопку "Войти"
        driver.find_element(By.XPATH, '//a[@href="/forgot-password"]').click()#Переход по кнопке "Восстановить пароль"
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()#Переход по кнопке "Войти" в форму авторизации
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == 'kirillmakshinskykag7123@yandex.ru' #Проверка Email в личном кабинете
