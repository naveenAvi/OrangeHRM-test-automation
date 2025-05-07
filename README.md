# OrangeHRM Test Automation

This is a Python Selenium automation project to test the OrangeHRM demo site.  
It uses PyTest and follows the Page Object Model (POM) design pattern.

## ✅ Features

- Automated Login
- Dashboard page verification
- Leave functionality via Quick Launch
- Logout functionality
- HTML test report generation
- One-click test run using `.bat` file

## 🔧 Tech Stack

- Python 3.12
- Selenium
- PyTest
- chromedriver-autoinstaller
- pytest-html

## 📁 Folder Structure

orangehrm_automation/

├── PageObjects/ # Page classes (LoginPage, DashboardPage, LeavePage)

├── testCases/ # Pytest test cases

├── Reports/ # Generated HTML test report

├── Screenshots/  # Screenshots

├── RunTests.bat # One-click test runner

├── requirements.txt # All dependencies

├── README.md # Project overview






## ▶️ How to Run

1. Install Python
2. Create a virtual environment:
    ```
    python -m venv .venv
    ```
3. Activate the environment and install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the tests:
    
    ```
    RunTests.bat
    ```

## 🔗 Demo Site Used

[https://opensource-demo.orangehrmlive.com](https://opensource-demo.orangehrmlive.com)
