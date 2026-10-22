from selenium import webdriver
from selenium.webdriver.common.by import By


# ---------------------------------------------------------
# 1. BROWSER CONFIGURATION
# ---------------------------------------------------------

# Configure Microsoft Edge to remain open after execution
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# Initialise the browser
driver = webdriver.Edge(options=options)

# Open the newsletter signup page
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")


# ---------------------------------------------------------
# 2. LOCATE FORM ELEMENTS
# ---------------------------------------------------------

# Find the input fields
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Find the signup button
sign_up = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit']"
)


# ---------------------------------------------------------
# 3. FILL IN THE FORM
# ---------------------------------------------------------

# Enter personal information
first_name.send_keys("Diogo")
last_name.send_keys("Braga")
email.send_keys("diogo.braga@gmail.com")


# ---------------------------------------------------------
# 4. SUBMIT THE FORM
# ---------------------------------------------------------

# Click the signup button
sign_up.click()

print("Signup form submitted successfully!")