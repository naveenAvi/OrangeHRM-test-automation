import pytest
import time
import logging
from selenium import webdriver
import chromedriver_autoinstaller

from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chromedriver_autoinstaller.install()

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login_leave_logout(self):
        logging.info("Starting test_login_leave_logout")

        driver = webdriver.Chrome()
        driver.maximize_window()
        logging.info("Browser launched and window maximized")

        driver.get(self.base_url)
        logging.info(f"Navigated to {self.base_url}")
        time.sleep(2)

        login_page = Login(driver)
        login_page.setUsername(self.username)
        logging.info("Entered username")

        login_page.setPassword(self.password)
        logging.info("Entered password")

        login_page.clickLogin()
        logging.info("Clicked login")
        time.sleep(3)

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.verifyDashboard(), "Dashboard page not loaded"
        logging.info("Dashboard page verified")

        dashboard_page.clickLeave()
        logging.info("Clicked Leave on dashboard")
        time.sleep(2)

        leave_page = LeavePage(driver)
        assert leave_page.verifyLeavePage(), "Leave page not loaded"
        logging.info("Leave page verified")

        dashboard_page.logout()
        logging.info("Clicked logout")
        time.sleep(2)

        expected_title = "OrangeHRM"
        actual_title = driver.title
        assert actual_title == expected_title, "Logout failed or not returned to login page"
        logging.info("Logout successful, login page reloaded")

