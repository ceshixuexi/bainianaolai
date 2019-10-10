from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegistrPage(BaseAction):
    register_button = By.XPATH,"//*[@text='已有账号，去登录']"
    def click_register_button(self):
        self.click(self.register_button)