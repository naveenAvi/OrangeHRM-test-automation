import pytest
import time
import logging
import os
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage

log_folder = "Logs"
os.makedirs(log_folder, exist_ok=True)

log_file = os.path.join(log_folder, "test_log.log")

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

    def take_screenshot(self, driver, screenshot_name):
        """Capture and save screenshot to Screenshots folder"""
        screenshot_dir = "Screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{screenshot_name}.png")
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to {screenshot_path}")

    def test_login(self):
        logging.info("Test started: test_login")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logging.info("Browser launched and maximized")

        try:
            self.driver.get(self.base_url)
            logging.info(f"Navigated to: {self.base_url}")
            time.sleep(2)

            self.take_screenshot(self.driver, "login_page_loaded")
            
            login_page = Login(self.driver)
            login_page.setUsername(self.username)
            logging.info("Entered username")

            login_page.setPassword(self.password)
            logging.info("Entered password")

            login_page.clickLogin()
            logging.info("Login button clicked")
            time.sleep(3)

            self.take_screenshot(self.driver, "dashboard_page_loaded")

            expected_title = "OrangeHRM"
            actual_title = self.driver.title
            logging.info(f"Actual title: {actual_title}")
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
            logging.info("Login successful, title matched")

            dashboard_page = DashboardPage(self.driver)
            assert dashboard_page.verifyDashboard(), "Dashboard page not loaded"
            logging.info("Dashboard page verified successfully")

        except Exception as e:
            logging.error(f"Test failed due to: {str(e)}")

            self.take_screenshot(self.driver, "test_login_failure")

            raise

        finally:
            self.driver.quit()
            logging.info("Browser closed after test")
