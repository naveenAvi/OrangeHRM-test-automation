import pytest
import time
import logging
import os
from selenium import webdriver

from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

log_dir = "Logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "test_login_leave.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

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

    def test_login_leave(self):
        logging.info("===== Starting test_login_leave =====")

        driver = webdriver.Chrome()
        driver.maximize_window()
        logging.info("Browser launched and maximized")

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
            logging.info("Dashboard page loaded successfully")

            dashboard_page.clickLeave()
            logging.info("Navigated to Leave section")
            time.sleep(2)

            leave_page = LeavePage(driver)
            assert leave_page.verifyLeavePage(), "Leave page not loaded"
            logging.info("Leave page loaded successfully")
            self.take_screenshot(driver, "03_leave_page")

        except Exception as e:
            logging.error(f"Test failed: {str(e)}")
            self.take_screenshot(driver, "99_test_login_leave_failure")
            raise

        finally:
            driver.quit()
            logging.info("Browser closed")
            logging.info("===== Finished test_login_leave =====")
