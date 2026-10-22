from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ---------------------------------------------------------
# 1. BROWSER CONFIGURATION
# ---------------------------------------------------------

# Configure Microsoft Edge to remain open after execution
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# Initialise the browser
driver = webdriver.Edge(options=options)

# Open the Python website
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# ---------------------------------------------------------
# 2. EXTRACT EVENT INFORMATION
# ---------------------------------------------------------

print("Starting events extraction...")

number_articles = driver.find_element(By.XPATH, '//*[@id="mwDw"]')

# ---------------------------------------------------------
# 3. DISPLAY RESULTS
# ---------------------------------------------------------

print(f'Current Number of Articles: {number_articles.text}')


community_portal = driver.find_element(By.LINK_TEXT, value='Community portal')

# community_portal.click()

search = driver.find_element(By.NAME, value="search")

# Send Keyboard
search.send_keys("Python", Keys.ENTER)
