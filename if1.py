"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
 * Вывести содержимое переменной на экран
"""
age = int(input('введите возраст'))
if age <= 7:
    print('ты ходишь в детский сад')
elif age <= 18:
    print('ты ходишь в школу')
elif age <= 24:
    print('ты ходишь в ВУЗ')
else:
    print('ты ходишь на работу')