
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators

class TestSBurgersCabinet:
    def test_pass_cabinet_to_constructor(self,login_and_pass_to_cabinet):#Позитивный тест на  переход из Личного Кабинета в Конструктор
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/"]').click()#Переход в Конструктор
        text_in_constuctor = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Соберите бургер"]'))).text
        assert text_in_constuctor == "Соберите бургер"

    def test_pass_cabinet_exit_button(self,login_and_pass_to_cabinet):#Позитивный тест на  выход из личного кабинета
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в Личный Кабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//button[@class ="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]').click()#Переход в Конструктор
        text = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//main//h2'))).text# Текст на форме авторизации
        assert text == "Вход"


    def test_pass_cabinet_exit_logo(self,login_and_pass_to_cabinet):#Позитивный тест на  переход из Личного Кабинета по клику ЛОГО
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//li[1]/a[@class="AppHeader_header__link__3D_hX"]').click()#Переход по клику ЛОГО
        text_in_constuctor = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Соберите бургер"]'))).text
        assert text_in_constuctor == "Соберите бургер"