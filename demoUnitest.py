# 安装parameterized
from parameterized import parameterized, param
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问”Login“ 页面
        self.driver.get("http://150.109.156.47:8000/")

    """
    1.@parameterized.expand  ,括号中传递列表,列表中传递元组
    2.传递两个元组，代表两个case
    3.每个用例有三个参数

    (1)代表用户名取值
    （2）代表密码取值
    （3）代表登录成功与否：约定：0 为失败，1为成功
    """

    @parameterized.expand([("admin", "admin", "0"), ("admin", "admin123456", "1")])
    def test_001_login(self, username, password, status):
        """
        错误密码登录失败
        登录名
        """
        login_name = self.driver.find_element(By.ID, "inputUsername")
        login_name.clear()
        login_name.send_keys(username)
        # 登录密码
        login_pwd = self.driver.find_element(By.ID, "inputPassword")
        login_pwd.clear()
        login_pwd.send_keys(password)
        # 登录按钮
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div/form/button')
        login_btn.click()

        if status == "0":
            # 登录后失败信息
            ele = self.driver.find_element(By.XPATH, '/html/body/div/form/p')
            self.assertIn(ele.text, self.driver.page_source) # page_source表示页面源码
            # self.assertIn(预期结果，实际结果)  # 判断预期结果是否包含在实际结果中
        elif status == "1":
            print("登录成功！！")
        else:
            print("参数化状态只能为0和1")

    def tearDown(self) -> None:
        self.driver.quit()

        # @parameterized.expand表示调用
        # self表示什么意思
        # status是不是可以提前定义
添加里点击头像jenkins配置ssh 添加id_rsa 文件内容
 指定分支选择git里的分支
if __name__ == '__main__':
    unittest.main()
