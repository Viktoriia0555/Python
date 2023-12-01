
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
import matplotlib.pyplot as plt

# Список новинних сайтів для аналізу
websites = ['https://www.bbc.com/news/world', 'https://edition.cnn.com/world']

# Ініціалізація WebDriver
driver = webdriver.Chrome()

# Функція для отримання тексту статті за URL
def get_article_text(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    article = soup.find('article')
    if article:
        text = article.get_text(separator=' ')
        return text
    return ''

# Функція для очищення тексту від знаків пунктуації та нормалізації
def clean_text(text):
    text = text.lower()  # Перетворення тексту на нижній регістр
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)  # Видалення пунктуації
    text = re.sub(r'\s+', ' ', text).strip()  # Видалення зайвих пробілів
    return text

# Функція для підрахунку кількості слів
def count_words(text):
    words = text.split()
    return Counter(words)

# Створення словника для зберігання текстів статей за різні періоди
article_texts = {}
for website in websites:
    article_texts[website] = {}
    for year in range(2022, 2024):  # Перебір років
        for month in range(1, 13):  # Перебір місяців
            archive_url = f'{website}/archive/{year}/{month}'  # Формування URL для архівного перегляду за місяць та рік
            text = get_article_text(archive_url)  # Отримання тексту статті за URL
            if text:
                cleaned_text = clean_text(text)  # Очищення та нормалізація тексту
                word_count = count_words(cleaned_text)  # Підрахунок слів та їх кількості
                article_texts[website][f'{year}-{month:02d}'] = word_count  # Зберігання кількості слів для кожного періоду

# Виведення результатів підрахунку кількості слів для конкретного сайту за різні періоди
selected_website = 'https://www.bbc.com/news/world'
for period, word_count in article_texts[selected_website].items():
    print(f'Period: {period}')
    print(word_count.most_common(10))  # Виведення 10 найбільш часто зустрічаючихся слів за період
    print('\n')

# Візуалізація результатів у вигляді графіка
df = pd.DataFrame(article_texts[selected_website])  # Створення DataFrame з результатами
df = df.transpose()  # Транспонування DataFrame для зручності

# Формування списку найбільш часто зустрічаючихся слів для кожного періоду
top_10_words = []
for column in df.columns:
    top_10_words.extend(df[column].apply(lambda x: x.most_common(10)).tolist())

# Побудова графіку частоти слів за період
plt.figure(figsize=(12, 6))
for i, word_count in enumerate(top_10_words):
    words = [word[0] for word in word_count]
    counts = [count[1] for count in word_count]
    plt.plot(df.index, counts, marker='o', label=f'Top {i+1} words: {words}')

plt.xlabel('Period')
plt.ylabel('Word Frequency')
plt.title('Top 10 Words Frequency Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

# Закриття браузера
driver.quit()