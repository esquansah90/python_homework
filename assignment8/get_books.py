# Task 3
import pandas as pd
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

results = []

books = driver.find_elements(
    By.CSS_SELECTOR,
    "li.row.cp-search-result-item"
)
print(len(books))

for book in books:

    title_element = book.find_element(
        By.CSS_SELECTOR,
        "span.title-content"
    )

    title = title_element.text

    author_elements = book.find_elements(
        By.CSS_SELECTOR,
        "a.author-link"
    )

    author_names = []

    for author in author_elements:
        author_names.append(author.text)

    author_text = ";".join(author_names)

    format_year_element = book.find_element(
    By.CSS_SELECTOR,
    "span.display-info"
)

    format_year = format_year_element.text

    book_data = {
    "Title": title,
    "Author": author_text,
    "Format-Year": format_year
}

    results.append(book_data)

df = pd.DataFrame(results)

print(df)

# Task 4

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)
    
driver.quit()