"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv

subjects = [
    ['Английский язык', 'Гаранян А. В.', 8],
    ['Алгебра', 'Гомзяков Б. И.', 10],
    ['Информатика', 'Наумова О. В.', 9]
]
with open('Ibraev.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Препод', 'Любовь к предмету (от 0 до 10)'])
    for subject in subjects:
        writer.writerow(subject)