import urllib.request   # Подключаем нужный модуль, что бы радотать с интернет-запросоми
"""
opener = urllib.request.build_opener()  # Создаем объект, который будет делать запрос
response = opener.open("https://httpbin.org/get")  # Открываем нужный сайт с помощью GET
print(response.read())  # Печатаем ответ от сайта
"""


import requests     # pip install requests
"""
# GET
response = requests.get("https://coinmarketcap.com/")  # Запрашиваем сайт
print(response.text)  # Выводим весь текст страницы
"""


"""
# POST
response = requests.post("https://httpbin.org/post", data={"key": "value"})
print(response.text)
"""



from bs4 import BeautifulSoup   # pip install beautifulsoup4

"""
response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr", {"style": "cursor:pointer"})  # Find rows with the specified style (if unique)

for row in rows:
    price_cell = row.find("td", {"style": "text-align:end"})
    if price_cell:
        price_div = price_cell.find("div", {"class": "sc-b3fc6b7-0 dzgUIj"})
        if price_div:
            price_span = price_div.find("span")
            if price_span:
                price = price_span.text.strip()
                print(price)
"""




"""
url = 'http://quotes.toscrape.com'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    quotes = soup.find_all("span", class_="text")
    for quote in quotes:
        print(quote.text)  # Виводимо всі цитати
"""








import requests                 # pip install requests
from bs4 import BeautifulSoup   # pip install beautifulsoup4

class HeroParser:
    def __init__(self, url):
        # Инициализация класса с адресом сайта
        self.url = url

    def fetch_page(self):
        # Загружаем страницу сайта
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Не удалось загрузить страницу, код ошибки: {response.status_code}")

    def parse_heroes(self, html):
        # Извлекаем имена супергероев из HTML страницы
        soup = BeautifulSoup(html, 'html.parser')
        hero_elements = soup.find_all('p', class_='card-body__headline')  # Находим теги <p> с именами
        heroes = [hero.text.strip() for hero in hero_elements]  # Извлекаем текст из каждого тега
        return heroes


# Создаем объект парсера
url = "https://www.marvel.com/characters"
parser = HeroParser(url)

# Загружаем страницу
html_content = parser.fetch_page()

# Парсим героев
heroes = parser.parse_heroes(html_content)

# Выводим список героев
print("Список супергероев Marvel:")
for hero in heroes:
    print(hero)
