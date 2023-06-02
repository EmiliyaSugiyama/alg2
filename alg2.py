#Задание 2
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

import random

def generate_random_array(n):
    arr = [random.randint(1, 10**6) for _ in range(n)]
    return arr

n = 10  # количество элементов в массиве
arr = generate_random_array(n)
sorted_arr = quicksort(arr)

# Проверка правильности сортировки
expected_sorted_arr = sorted(arr)
assert sorted_arr == expected_sorted_arr, "Ошибка: Массивы не совпадают"

print("Исходный массив:", arr)
print("Отсортированный массив (собственный алгоритм):", sorted_arr)
print("Отсортированный массив (встроенный метод):", expected_sorted_arr)

# мы генерируем массив из 10 случайных целых чисел в диапазоне от 1 до 10^6, сортируем его с помощью нашего алгоритма быстрой сортировки и сравниваем результат с ожидаемым отсортированным массивом, полученным с помощью встроенного метода sorted. Если массивы совпадают, выводятся исходный и отсортированный массивы.

#Задание 3

films = [
    {"title": "Film A", "rating": 8.5, "genre": "Drama", "year": 2010},
    {"title": "Film B", "rating": 7.9, "genre": "Comedy", "year": 2015},
    {"title": "Film C", "rating": 8.2, "genre": "Action", "year": 2012},
    {"title": "Film D", "rating": 7.6, "genre": "Drama", "year": 2008},
    {"title": "Film E", "rating": 8.1, "genre": "Comedy", "year": 2019}
]

sorted_films = sorted(films, key=lambda x: (x["rating"], x["genre"], x["year"]), reverse=True)

for film in sorted_films:
    print(film["title"], film["rating"], film["genre"], film["year"])

#список films содержит словари с информацией о фильмах. Мы используем функцию sorted и передаем ей список фильмов и ключ сортировки, который представляет собой лямбда-функцию. Лямбда-функция возвращает кортеж из значений рейтинга, жанра и года выпуска для каждого фильма.

#Задание 4

messages = [
    {"employee": "John", "time": "12:30", "content": "Hello"},
    {"employee": "Alice", "time": "09:45", "content": "Good morning"},
    {"employee": "John", "time": "15:20", "content": "How are you?"},
    {"employee": "Bob", "time": "11:10", "content": "Meeting at 2 PM"},
    {"employee": "Alice", "time": "14:05", "content": "Can we talk?"},
    {"employee": "John", "time": "17:50", "content": "See you tomorrow"}
]

employee_stats = {}

for message in messages:
    employee = message["employee"]
    time = message["time"]

    if employee in employee_stats:
        employee_stats[employee]["count"] += 1
        employee_stats[employee]["last_time"] = time
    else:
        employee_stats[employee] = {"count": 1, "last_time": time}

# Находим сотрудника с наибольшим количеством сообщений
max_messages = max(employee_stats.values(), key=lambda x: x["count"])
max_employee = max_messages["count"]
max_time = max_messages["last_time"]

print("Сотрудник с наибольшим количеством сообщений:")
print("Имя:", max_employee)
print("Количество сообщений:", max_employee["count"])
print("Время последнего сообщения:", max_time)

#Задание 5

products = {
    "Electronics": [
        {"name": "TV", "sales": 100},
        {"name": "Laptop", "sales": 200},
        {"name": "Phone", "sales": 150}
    ],
    "Clothing": [
        {"name": "Shirt", "sales": 50},
        {"name": "Jeans", "sales": 80},
        {"name": "Dress", "sales": 120}
    ],
    "Books": [
        {"name": "Novel", "sales": 70},
        {"name": "Textbook", "sales": 90},
        {"name": "Magazine", "sales": 60}
    ]
}

# Сортируем товары в каждой категории по продажам
for category, products_list in products.items():
    sorted_products = sorted(products_list, key=lambda x: x["sales"])
    products[category] = sorted_products

# Выводим отсортированные товары в каждой категории
for category, products_list in products.items():
    print(category + ":")
    for product in products_list:
        print(product["name"], " - ", product["sales"])
    print()

