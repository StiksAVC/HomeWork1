"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_scores = [
    {'school_class': '5a', 'scores': [2, 4, 5, 3, 2, 4, 5, 5]},
    {'school_class': '6б', 'scores': [3, 3, 2, 4, 5, 4, 5, 3]},
    {'school_class': '9в', 'scores': [2, 4, 5, 3, 2, 1, 2, 4]}
]
for marks in school_scores:
    average_score = 0
    class_name = 0
    average_score = float(sum(marks.get("scores"))/len(marks.get("scores")))
    class_name = (marks.get("school_class"))
    print("Класс:", (class_name), "Средний балл:", (average_score))
    break                                                                     # не выходит завершить цикл
average_school_score = 0
average_school_score = float(sum(marks.get("scores"))/len(marks.get("scores")))
print("Средний балл по школе:", (average_school_score))


#import random                                                               пробовал рандомно выставить оценки, про имена переменных знаю((((
#n = random.randint(1,6)
#s = 5
#for n in range (s):
 # print(n)