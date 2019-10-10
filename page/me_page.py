from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    nickname_text = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    def get_nickname(self):
        return self.get_text(self.nickname_text)