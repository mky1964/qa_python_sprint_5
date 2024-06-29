

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators

class TestSBurgersConstructor:
    def test_pass_to_sauce_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Соусы
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/"]').click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//main/section[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[2]/span[@class="text text_type_main-default"]'))).click()#Клик "Соусы"
        sauce_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//p[text()="Соус фирменный Space Sauce" and @class="BurgerIngredient_ingredient__text__yp3dH"]'))).text
        assert sauce_name == 'Соус фирменный Space Sauce'


    def test_pass_to_fillings_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Начинки
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/"]').click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//main/section[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[3]/span[@class="text text_type_main-default"]'))).click()#Клик "Начинки"
        filling_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//p[text()="Говяжий метеорит (отбивная)"]'))).text
        assert filling_name == "Говяжий метеорит (отбивная)"

    def test_pass_to_bread_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Булки
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')))
        driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/"]').click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//main/section[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[3]/span[@class="text text_type_main-default"]'))).click()#Клик "Начинки"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//main/section[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[1]/span[@class="text text_type_main-default"]'))).click()#Клик "Булки"
        filling_name = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Флюоресцентная булка R2-D3"]'))).text
        assert filling_name == "Флюоресцентная булка R2-D3"