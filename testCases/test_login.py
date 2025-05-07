import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import time
import logging

from PageObjects.LoginPage import Login

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chromedriver_autoinstaller.install()

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self):
        logging.info("Starting test_login")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logging.info("Browser launched and maximized")

        self.driver.get(self.base_url)
        logging.info(f"Navigated to URL: {self.base_url}")
        time.sleep(5)

        login_page = Login(self.driver)
        login_page.setUsername(self.username)
        logging.info(f"Entered username: {self.username}")

        login_page.setPassword(self.password)
        logging.info(f"Entered password")

        login_page.clickLogin()
        logging.info("Clicked login button")
        time.sleep(5)

        expected_title = "OrangeHRM"
        actual_title = self.driver.title
        logging.info(f"Page title after login: {actual_title}")

        assert actual_title == expected_title, f"Expected title '{expected_title}', got '{actual_title}'"
        logging.info("Login test passed")

        self.driver.close()
        logging.info("Browser closed")
