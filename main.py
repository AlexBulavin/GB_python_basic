'''
Урок 1. Ввод-Вывод, операторы ветвления

БАЗОВЫЕ:

Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
''' 
print("Задание 1")
n = 1
m1 = 'ello'
m2 = 'world'
print(f"n = {n}")
print(f'H{m1} {m2}!')

'''
Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
'''

user_name = user_password = user_age = None

user_name = input('Введите имя пользователя: ')
user_password = input(f'{user_name}, введите пароль: ')
print(f'Ваши данные для входа в аккаунт: '
    f'имя - {user_name}, '
    f'пароль - {user_password}, '
    f'возраст - {user_age}' 
    if (user_age := input(f'{user_name}, \
        введите возраст (полных лет): ')).isnumeric()
    else 'Введено не число, пользователь не создан, повторите регистрацию')

'''
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
'''
print('\nЗадание 2')
print(f'{round(int(n)/3600, 1)}:{round(int(n)/60, 1)}:{int(n)}' 
    if (n := input('Введите целое число секунд: ')).isnumeric() 
    else "Введено не число")
'''
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
'''
print('\nЗадание 3')

n = input('Введите целое положительное число: ')
if (n.isnumeric() and (int(n) > 0)) :
    n = int(n)
    nn = n*n
    nnn = nn*n
    print(f'n + n*n + n*n*n = {n + nn + nnn}') 
else : 
    print(f"Ошибка, ввода!")

'''
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
'''
print('\nЗадание 4')
sales = loses = profit = stuff_num = None

print(int(sales) 
    if (sales := input('Введите выручку фирмы (целое число): ')).isnumeric()
    else "Введено не число")
sales = int(sales)

print(int(loses) 
    if (loses := input('Введите издержки фирмы (целое число): ')).isnumeric()
    else "Введено не число")
loses = int(loses) 

profit = sales - loses
print(f'Финансовый результат - прибыль. Ее величина: {profit}\n' 
    f'Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)' 
    f'\nРентабельность выручки = {round(profit/sales, 1)}' 
    if profit > 0 else f'Убыток {profit}')

print(f'Прибыль фирмы в расчете на одного сотрудника = '
    f'{round(profit/int(stuff_num), 1)}' 
    if (stuff_num := input(f'Введите количество сотрудников '
    f'(целое число): ')).isnumeric() and profit > 0
    else "Введено не число")

'''
ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
print('\nЗадача 2 дополнительная')
while  not (number := input('Введите целое число: ')).isnumeric():
    "Введено не число"
sum = 0
for i in number:
    sum += int(i)
print(f'Сумма цифр числа {number} = {sum}')

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10

'''
print('\nЗадача 4 дополнительная')
while  not (total_amount := input('Введите количество сделанных журавликов'
    f' (оно должно быть кратно 6): ')).isnumeric() and (int(total_amount) % 6 != 0):
    "Введено не число или оно не кратно 6, повторите ввод"
single_boy_amount = int(total_amount) // 6
print(f'Петя и Сережа сделали по {single_boy_amount}, '
    f'а Катя - {single_boy_amount * 4}')

'''

Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
print('\nЗадача 6 дополнительная')
while  not (ticket_number := input('Введите номер билета (он должен быть '
    f'шестизначным числом): ')).isnumeric() and (len(ticket_number) != 6):
    "Введено не число или оно не шестизначное, повторите ввод"

print(f'Ура, билетик счастливый!' 
    if (int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2]) ==\
        int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5]))
    else f'Ничего страшного, не повезло в этот раз')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между 
дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no

'''
print('\nЗадача 8 дополнительная')
while  not (chocolate_length := input('Введите ширину шоколадки в дольках' 
    f'(она должна быть натуральным числом): ')).isnumeric()\
    and (int(chocolate_length) > 0):
    "Введено не число или оно меньше или равно нолю, повторите ввод"
while  not (chocolate_width := input('Введите длину шоколадки в дольках '
    f'(она должна быть натуральным числом): ')).isnumeric()\
    and (int(chocolate_width) > 0):
    "Введено не число или оно меньше или равно нолю, повторите ввод"
pieces_amount = input(f'Шоколадка {chocolate_length}X'
    f'{chocolate_width}'
    f'На какое количество будем делить?')
if (pieces_amount.isnumeric()\
    and (int(pieces_amount) > 0)\
    and (int(pieces_amount) >= int(chocolate_length)\
    or  int(pieces_amount) >= int(chocolate_width))\
    and(int(chocolate_length) % int(pieces_amount) == 0\
    or int(chocolate_width) % int(pieces_amount) == 0)):
    print(f'Шоколадка делится на {pieces_amount}!')

else: 
    print(f'Не делится.')   
 
