from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()
#from constants import Constants
#from locators import Locators


class TestSBurgersRegPositive:
    def test_reg_positive(self, driver): #Позитивный тест на регистрацию
        email = faker.email()
        print(email)
        password = '123456'
        name = 'Петя'
        driver.find_element(By.XPATH, '//p[text() = "Личный Кабинет"]').click()#Клик "Личный Кабинет"
        driver.find_element(By.XPATH, '//a[@href="/register"]').click()#Клик "Зарегистрироваться"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//label[text()="Имя"]')))
        driver.find_element(By.XPATH, '//fieldset[1]//input').clear()
        driver.find_element(By.XPATH, '//fieldset[1]//input').send_keys(name)#Ввод Имя
        driver.find_element(By.XPATH, '//fieldset[2]//input').clear()
        driver.find_element(By.XPATH, '//fieldset[2]//input').send_keys(email)
        driver.find_element(By.XPATH, './/input[@name="Пароль"]').clear()#Ввод Пароль
        driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(password)
        driver.find_element(By.XPATH, '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()#Клик на Зарегистрироваться

        form_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//h2[text() = "Вход"]'))).text
        assert  form_name == 'Вход' #Проверка заголовка в форме

class TestSBurgersRegNegativePass:
    def test_reg_negative_password(self,driver):# Негативный тест на ввод пароля (вводиться 4 символа
        email = faker.email()
        name ='Вася'
        print(email)
        password = '1234'# 4 символа в password
        driver.find_element(By.XPATH, '//p[text() = "Личный Кабинет"]').click()  # Кликаем "Личный Кабинет"
        driver.find_element(By.XPATH, '//a[@href="/register"]').click()  # Кликаем "Зарегистрироваться"
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//label[text()="Имя"]')))
        driver.find_element(By.XPATH, '//fieldset[1]//input').clear()
        driver.find_element(By.XPATH, '//fieldset[1]//input').send_keys(name)  # Ввод Имя
        driver.find_element(By.XPATH, '//fieldset[2]//input').clear()
        driver.find_element(By.XPATH, '//fieldset[2]//input').send_keys(email)
        driver.find_element(By.XPATH, './/input[@name="Пароль"]').clear()
        driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(password) #ввод Пароль
        driver.find_element(By.XPATH,
                            '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()  # Клик на Зарегистрироваться

        alert_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))).text

        assert alert_text == 'Некорректный пароль'  # Проверка сообщения




