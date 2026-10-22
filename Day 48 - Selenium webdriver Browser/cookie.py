from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 20)

# Select English
wait.until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
).click()

# Wait for the cookie button
cookie = wait.until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Click continuously
while True:
    cookie.click()