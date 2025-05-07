import pytest
import time
import logging
from selenium import webdriver

from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login_leave(self):
        logging.info("Starting test_login_leave")

        driver = webdriver.Chrome()
        driver.maximize_window()
        logging.info("Browser launched and maximized")

        driver.get(self.base_url)
        logging.info(f"Navigated to {self.base_url}")
        time.sleep(2)

        login_page = Login(driver)
        login_page.setUsername(self.username)
        logging.info("Username entered")

        login_page.setPassword(self.password)
        logging.info("Password entered")

        login_page.clickLogin()
        logging.info("Login button clicked")
        time.sleep(3)

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.verifyDashboard(), "Dashboard page not loaded"
        logging.info("Dashboard page loaded successfully")

        dashboard_page.clickLeave()
        logging.info("Navigated to Leave section")
        time.sleep(2)

        leave_page = LeavePage(driver)
        assert leave_page.verifyLeavePage(), "Leave page not loaded"
        logging.info("Leave page loaded successfully")

        
