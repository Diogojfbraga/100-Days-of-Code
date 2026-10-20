from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.python.org/")

print("Starting events extraction")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
   

for event in events:
    print((event.get_attribute('datetime'))[:10])
#     print(f"Processing event {i}")
#     events_time = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')



    # test = events_time.get_attribute("datetime")
    # print(events_time.get_attribute("outerHTML"))
    
    # events_year = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time/span').text
    
    # print(f"Event {i}: {events_time.tag_name}")
    # print(f"Date: {test!r}")
    # print(i)


# for time in events_time:
    # print(events_time)

# price_pound = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# price_pennies = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text

# # print(f'The price is {price_pound}.{price_pennies}')

# # documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# # print(documentation_link.text)

# driver.find_element(By.XPATH, value="")

# driver.quit()