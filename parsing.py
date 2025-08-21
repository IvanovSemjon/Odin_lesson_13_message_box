import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def parse_drom_premium_cars():
    # URL целевой страницы
    url = "https://auto.drom.ru/region77/premium/"
    
    # Заголовки для имитации браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Отправляем GET-запрос
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем статус ответа
        
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим блок со всеми объявлениями
        ads_block = soup.find('div', class_='css-12lf65q e3qgya0')
        
        if not ads_block:
            print("Не удалось найти блок с объявлениями")
            return pd.DataFrame()
        
        # Находим все объявления
        ads = ads_block.find_all('a', class_='css-b5o66h e18mkgj90')
        
        cars_data = []
        
        for ad in ads:
            try:
                # Извлекаем название автомобиля
                name_tag = ad.find('span', class_='css-1t71ine e16zdi0i0')
                car_name = name_tag.text.strip() if name_tag else "Название не найдено"
                
                # Ищем блок с ценой - он находится прямо в блоке объявления
                price_block = ad.find('div', class_='css-luilqb egua2dj0')
                
                if price_block:
                    # Получаем весь текст из блока цены
                    price_text = price_block.get_text(strip=True)
                    # Очищаем цену от лишних символов (оставляем только цифры)
                    car_price = re.sub(r'[^\d]', '', price_text)
                    car_price = int(car_price) if car_price.isdigit() else None
                else:
                    car_price = None
                
                # Добавляем данные в список
                cars_data.append({
                    'Марка_модель': car_name,
                    'Цена_руб': car_price
                })
                
                print(f"Найдено: {car_name} - {car_price} руб.")
                
            except Exception as e:
                print(f"Ошибка при парсинге объявления: {e}")
                continue
        
        # Создаем DataFrame
        df = pd.DataFrame(cars_data)
        
        return df
        
    except requests.RequestException as e:
        print(f"Ошибка при подключении к сайту: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return pd.DataFrame()


def save_df_to_notebook(df, filename='cars_data.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Данные об автомобилях из спецразмещения\n")
        f.write("=" * 50 + "\n\n")
        f.write(df.to_string(index=False))
        f.write("\n\nВсего найдено автомобилей: " + str(len(df)))
    print(f"Данные сохранены в файл {filename}")

df = parse_drom_premium_cars()
if not df.empty:
    save_df_to_notebook(df)
else:
    print("Нет данных для сохранения")

