import pytest
import time
import logging
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self):
        logging.info("Test started: test_login")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logging.info("Browser launched and maximized")

        self.driver.get(self.base_url)
        logging.info(f"Navigated to: {self.base_url}")
        time.sleep(2)

        login_page = Login(self.driver)
        login_page.setUsername(self.username)
        logging.info("Entered username")

        login_page.setPassword(self.password)
        logging.info("Entered password")

        login_page.clickLogin()
        logging.info("Clicked login")
        time.sleep(3)

        # Assertion: Verify title
        expected_title = "OrangeHRM"
        actual_title = self.driver.title
        logging.info(f"Actual title: {actual_title}")
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
        logging.info("Login successful, title matched")

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.verifyDashboard(), "Dashboard page not loaded"
        logging.info("Dashboard page verified successfully")


