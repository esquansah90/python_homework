# Task 6

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(
    "https://owasp.org/Top10/2025/"
)

results = []

vulnerabilities = driver.find_elements(
    By.XPATH,
    "/html/body/div[3]/main/div/div[3]/article/ol/li"
)

print(len(vulnerabilities))

for vulnerability in vulnerabilities:

    link_element = vulnerability.find_element(
        By.TAG_NAME,
        "a"
    )

    title = link_element.text

    link = link_element.get_attribute("href")


    vulnerability_data = {
        "Title": title,
        "Link": link
    }

    results.append(vulnerability_data)

print(results)

df = pd.DataFrame(results)

print(df)

df.to_csv(
    "owasp_top_10.csv",
    index=False
)

driver.quit()
