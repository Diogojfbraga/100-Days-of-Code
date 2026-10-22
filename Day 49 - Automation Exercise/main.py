from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------------------------------------------------------
# 1. BROWSER CONFIGURATION
# ---------------------------------------------------------

# Configure Microsoft Edge to remain open after execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialise the browser
driver = webdriver.Chrome(options=options)

# Open the Python website
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Navigation_button__uyKX2"))).click()

# Login
email = driver.find_element(By.CLASS_NAME, "Login_input__RLJo3")

email.send_keys("student@test.com")

password = driver.find_element(By.ID, "password-input")

password.send_keys("password123")

login_button = driver.find_element(By.CLASS_NAME, "Login_submitButton__tJFna")

login_button.click()