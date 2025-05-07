from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_heading_xpath = "//h6[text()='Dashboard']"
        self.leave_menu_xpath = "//span[text()='Leave']"
        self.user_menu_xpath = "//p[@class='oxd-userdropdown-name']"
        self.logout_link_xpath = "//a[text()='Logout']"

    def verifyDashboard(self):
        return self.driver.find_element(By.XPATH, self.dashboard_heading_xpath).is_displayed()

    def clickLeave(self):
        self.driver.find_element(By.XPATH, self.leave_menu_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.user_menu_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()
