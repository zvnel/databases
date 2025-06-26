import psycopg2 #для подключения к бд
import matplotlib.pyplot as plt #для визуализации
import matplotlib.colors as mcolors #для цветов

#подключаемся к базе данных
conn = psycopg2.connect(user = '*********',
                          password = '*******',
                          host = '*******',
                          port = '*******',
                          database = '******')
cursor = conn.cursor() #курсор для запроса

#запрос
cursor.execute("""
    SELECT book_genre, COUNT(*) AS count
    FROM BOOKS_INFO
    GROUP BY book_genre
""")

genres_count = cursor.fetchall()
conn.close()

colors = list(mcolors.TABLEAU_COLORS) #цвета
plt.figure(figsize=(10, 6)) #создаем фигуру
plt.pie([count for _, count in genres_count], labels=[genre for genre, _ in genres_count], colors=colors[:len(genres_count)], autopct='%1.1f%%') #заполняем диаграмму
plt.title('genres of books')
plt.axis('equal')
plt.show()

***

import psycopg2 #для подключения к бд
import matplotlib.pyplot as plt
from datetime import datetime


#подключаемся к базе данных
conn = psycopg2.connect(user = 'itmo408653_2024',
                          password = 'itmo408653',
                          host = '146.185.211.205',
                          port = '5432',
                          database = 'dbstud')

c = conn.cursor()

# Запрос
c.execute("""
    SELECT TO_CHAR(publication_date, 'MM') AS month, COUNT(*) AS count
    FROM PUBLICATION
    WHERE TO_CHAR(publication_date, 'MM') BETWEEN '01' AND '06'
    GROUP BY month
    ORDER BY month
""")
publication_data = c.fetchall()

# Получение списка первых 6 месяцев
months = ['01', '02', '03', '04', '05', '06']

# Заполнение пропущенных месяцев нулями
book_counts = [0] * 6
for month, count in publication_data:
    book_counts[int(month) - 1] = count

# Создание списка цветов
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Построение диаграммы
plt.figure(figsize=(12, 6))
plt.bar(months, book_counts, color=colors)
plt.xticks(range(len(months)), [datetime.strptime(m, '%m').strftime('%b') for m in months])
plt.xlabel('Month')
plt.ylabel('Number of Books')
plt.title('Books published in the first half of 2023')
plt.show()

# Закрытие соединения с базой данных
conn.close()
