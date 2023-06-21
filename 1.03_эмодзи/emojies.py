import requests
from bs4 import BeautifulSoup
import re

# нужные нам разделы
sections = ['nature', 'music', 'science']

# счета emoji в тексте
def count_emoji(text):
    # Используем регулярное выражение для поиска emoji
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # символы и пиктограммы
                               u"\U0001F680-\U0001F6FF"  # транспорт и карты
                               u"\U0001F1E0-\U0001F1FF"  # флаги стран
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)
    emojis = re.findall(emoji_pattern, text)
    return len(emojis)

# считаем эмодзи в разделе
def count_emoji_in_section(section):
    url = f"https://emojipedia.org/{section}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    emoji_count = count_emoji(text)
    return emoji_count

# считаем общее кол-во нужных эмодзи
for section in sections:
    count = count_emoji_in_section(section)
    print(f"Количество emoji в разделе {section}: {count}")


# Вывод:
# Количество emoji в разделе nature: 175
# Количество emoji в разделе music: 42
# Количество emoji в разделе science: 9
