from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_input = By.ID,"com.yunmall.lc:id/logon_account_textview"
    password_input = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button = By.ID, "com.yunmall.lc:id/logon_button"
    def input_username(self,text):
        self.input(self.username_input,text)
    def input_password(self,text):
        self.input(self.password_input,text)

    def click_login_button(self):
        self.click(self.login_button)