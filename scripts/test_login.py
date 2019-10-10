import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        self.page.home().click_me()
        self.page.register().click_register_button()
        self.page.login().input_username('itheima_test')
        self.page.login().input_password('itheima')
        self.page.login().click_login_button()
        text = self.page.me().get_nickname()
        assert text == 'itheima_test','用户名与预期不一致'
