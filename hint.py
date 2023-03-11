'''
value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)

name = "Hi there"
print(type(name)) # функция, которая указывает на тип данных
\'''
Здесь расположен коммент в Python

Как сделать комментарий?
Если Вы хотите закомментировать 1 строку достаточно применить специальный
символ “#”, если Вам нужно закомментировать сразу несколько строк выделите их
и нажмите ctrl (cmd) + / или же используйте тройные кавычки "’’’"
\'''
s = 'hello,' # создание 1-ой строки
w = "sun" # создание 2-ой строки
print(s, w)

s = 'hello "world"'
print(s)
s = "hello 'world'"
print(s)
s = 'hello \"world'
print(s)

# Делаем ввод с одновременной проверкой и выводом

print(int(n) if (n := input('Введите целое число: ')).isnumeric() else "Введено не число")

#----------------------- int() -------------------------------
n = 1.345
print("print(int(n))", int(n)) # Отбрасывается дробная часть вне зависимости больше 0.5 или меньше

m = '345'
print("print(m * 2) ", m * 2) # При умножении строки на число, она повторяется столько раз на какое была умножена
print("print(int(m)*2)", int(m)*2)

#----------------------- str() -------------------------------
n = 1.345
print("print(str(n) * 2)", str(n) * 2)

#----------------------- float() -----------------------------
print("print(float(n) * 2)", float(n) * 2)

m = 2
print("print(float(m))", float(m))

#----------------------- round() -----------------------------
a = 1.43425
b = 2.2983
c = round(a * b, 5) #Указали до какого знака после запятой нужно округлить

#--------------- Сокращенные операции присваивания -----------
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

#--------------- is, is not, in, not in -----------------------
a = 1 > 4 # Присваиваем результат сравнения 1 > 4
print(a) # False

a = 1 < 4 and 5 > 2
print(a) # True

a = 1 == 2
print(a) # False

a = 1 != 2
print(a) # True

#--- Можно сравнивать не только числовые значения, но и строки: ---
a = 'qwe'
b = 'qwe'
print(a == b) # True

#--- В Python можно использовать тройные и даже четверные неравенства ---

a = 1 < 3 < 5 < 10
print (a) # True
'''

n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
else:
    print('Пожалуй')
    print('хватит )')
print(summa)
# Пожалуй
# хватит
# 0

#----- for, range ---
'''
for i in enumeration:
# operator 1
# operator 2
# ...
# operator n
'''

for i in 1, -2, 3, 14, 5:
    print(i)
# 1 -2 3 15 5

'''
Range
● Range выдает значения из диапазона с шагом 1.
● Если указано только одно число — от 0 до заданного числа.
● Если нужен другой шаг, третьим аргументов можно задать приращение.
'''
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20

for i in range(5):
    print(i)
# 0 1 2 3 4

for i in 'qwerty':
    print(i)

text = "СъЕШЬ ещё этих МяГкИх французских булок"
print(len(text)) # 39

print('ещё' in text) # True

print(text.lower()) # съешь ещё этих мягких французских булок

print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК

print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

#-------Срезы---
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2]