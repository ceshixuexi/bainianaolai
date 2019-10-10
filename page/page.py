from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegistrPage


class Page:
    def __init__(self,driver):
        self.driver = driver
    def home(self):
        return HomePage(self.driver)
    def register(self):
        return RegistrPage(self.driver)
    def login(self):
        return LoginPage(self.driver)
    def me(self):
        return MePage(self.driver)
