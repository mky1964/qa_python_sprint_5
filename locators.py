from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, "//input[@name='name']")#Поле   Email  формы авторизации
    PASSWORD = (By.XPATH, "//input[@type='password']") #Поле   PASSWORD  формы авторизации
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")# кнопка ввода при авторизации
    ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")#Кнопка аккаунта из главной страницы
    CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")#Кнопка личного кабинета из главной страницы

