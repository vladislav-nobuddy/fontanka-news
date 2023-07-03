import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.fontanka.ru/24hours.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


response = requests.get(url, headers=headers)
soup = bs(response.text, 'lxml')
# print(soup)
news = soup.find_all('li', class_='J1amh')
num = 1
for new in news:
    print(f'Новость номер: {num}')
    title = new.find('div', class_='J1amv').find('a', class_='J1fb')
    link = new.find('div', class_='J1amv').find('a', class_='J1fb').get('href')

    if 'http' in link:
        pass
    else:
        link = 'https://www.fontanka.ru' + link

    print(f'{title.text}\n ссылка: {link}')
    num = num + 1
