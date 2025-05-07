import pytest
import time
import logging
import os
from selenium import webdriver
import chromedriver_autoinstaller

from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

log_dir = "Logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "test_login_leave_logout.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

chromedriver_autoinstaller.install()

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def take_screenshot(self, driver, name):
        screenshot_dir = "Screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        path = os.path.join(screenshot_dir, f"{name}.png")
        driver.save_screenshot(path)
        logging.info(f"Screenshot saved: {path}")

    def test_login_leave_logout(self):
        logging.info("===== Starting test_login_leave_logout =====")

        driver = webdriver.Chrome()
        driver.maximize_window()
        logging.info("Chrome browser launched and maximized")

        try:
            driver.get(self.base_url)
            logging.info(f"Navigated to {self.base_url}")
            time.sleep(2)
            self.take_screenshot(driver, "01_login_page")

            login_page = Login(driver)
            login_page.setUsername(self.username)
            logging.info("Username entered")
            login_page.setPassword(self.password)
            logging.info("Password entered")
            login_page.clickLogin()
            logging.info("Login button clicked")
            time.sleep(3)

            self.take_screenshot(driver, "02_dashboard_loaded")
            dashboard_page = DashboardPage(driver)
            assert dashboard_page.verifyDashboard(), "Dashboard page not loaded"
            logging.info("Dashboard verified successfully")

            dashboard_page.clickLeave()
            logging.info("Leave option clicked")
            time.sleep(2)

            self.take_screenshot(driver, "03_leave_page")
            leave_page = LeavePage(driver)
            assert leave_page.verifyLeavePage(), "Leave page not loaded"
            logging.info("Leave page verified successfully")

            dashboard_page.logout()
            logging.info("Logout clicked")
            time.sleep(2)

            actual_title = driver.title
            expected_title = "OrangeHRM"
            assert actual_title == expected_title, "Logout failed or did not return to login page"
            logging.info("Successfully logged out and returned to login page")
            self.take_screenshot(driver, "04_after_logout")

        except Exception as e:
            self.take_screenshot(driver, "99_test_failure")
            raise

        finally:
            driver.quit()
            logging.info("Browser closed")
            logging.info("===== Test completed: test_login_leave_logout =====")
