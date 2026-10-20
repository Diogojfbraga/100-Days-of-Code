from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get("https://www.amazon.co.uk/Wantek-Conduction-Headphones-Headphone-Waterproof-red/dp/B0DLK37D3B/ref=sr_1_1_sspa?crid=12JSRZXBFI5ZY&dib=eyJ2IjoiMSJ9.bKjSStRlbrH9XDP2RQh3fYbbEqo2kBU6MFsOkJ_FWC3F7gciuy1dU5W96lnnJOzArRWSQPJv5lkQ-7gdKi8SP4F2J6os52DeFv7-IG7AFyjbyJU8LejUEa881-0Uow9cIIo-5UlDziRN-dZ3eD2fTiwpIRworDrlVzXRraSOAbqa4_s1Gz628cx2UrEUkJPUaHN9QD2xN7qcJmwTdcje257D1fhBp3Jovv8hgYuP0PI.sMOr-mlhMwNFji1IzJ8ppiAUNlU2LG8QRXB-YXNZCKg&dib_tag=se&keywords=swimming+earphones+waterproof&qid=1792510546&sprefix=swiming+earph%2Caps%2C118&sr=8-1-spons&aref=tyi0TJOo3g&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")


price_pound = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
price_pennies = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text

print(f'The price is {price_pound}.{price_pennies}')

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

driver.find_element(By.XPATH, value="")

driver.quit()