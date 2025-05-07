from selenium.webdriver.common.by import By

class LeavePage:
    leave_heading_xpath = "//h6[text()='Leave']"

    def __init__(self, driver):
        self.driver = driver

    def verifyLeavePage(self):
        return self.driver.find_element(By.XPATH, self.leave_heading_xpath).is_displayed()
