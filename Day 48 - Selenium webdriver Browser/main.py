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

# Open the Python website
driver.get("https://www.python.org/")


# ---------------------------------------------------------
# 2. EXTRACT EVENT INFORMATION
# ---------------------------------------------------------

print("Starting events extraction...")

# Find all upcoming event dates
events = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget time"
)

# Find all upcoming event names
names = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget li a"
)


# ---------------------------------------------------------
# 3. STORE EVENTS IN A DICTIONARY
# ---------------------------------------------------------

events_dict = {}

# Pair each event date with its corresponding name
for i, (event, name) in enumerate(zip(events, names)):

    events_dict[i] = {
        "time": event.get_attribute("datetime")[:10],
        "name": name.text
    }


# ---------------------------------------------------------
# 4. DISPLAY RESULTS
# ---------------------------------------------------------

print(events_dict)