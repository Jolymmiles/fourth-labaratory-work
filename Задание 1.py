# Задание 1
a = int(input('Введите число:'))
b = a // 10
c = a % 10
x = b + c
z = b * c
if b == 1:
    chislo = 0 + b
if c == 1:
    chislo = chislo + c
print('Десятков=', b)
print('Число единиц в нем', chislo)
print('сумму его цифр', x)
print('произведение его цифр', z)

# Задание 2


a = int(input('Введите трехзначное число:'))
b = int(input('Введите трехзначное число:'))
c = a // 100
b = a % 10
v = (a % 100 - b) // 10
n = a // 100
x = a % 10
m = (a % 100 - x) // 10
f = c + v + b + n + m + x
g = c - v - b - n - m - x
h = c * v * b * n * m * x
j = (c + v + b) / (n + m + x)
print('Общая сумма', f)
print('Разность', g)
print('Произведение', h)
print('Частное от деления сумм', j)

# Задание 3
a = int(input('Введите трехзначное число:'))

z = a // 10
x = z // 10
c = a % 10
v = z % 10
b = c * 100 + v * 10 + x * 1
print('Ответ', b)

# Задание 4
a = int(input('Введите трехзначное число:'))
z = a // 100
x = a % 100
print('Ответ:', x * 10 + z)

# Задание 5
chislo = int(input('Введите число:'))
z = chislo % 10
x = (chislo // 10) % 10
c = chislo // 100
print(z, x, c)
print(x, z, c)
print(c, x, z)
print(c, z, x)
print(z, c, x)
print(x, c, z)

# Задание 6
b = int(input('Введите двухзнанчое число:'))
a = int(input('Введите однозначное число:'))
z = a + b
b2 = z % 10
b1 = z // 10
print('Сумма заданых чисел:', z)
print('Число едениц:', b2)
print('Число десятков:', b1)

# Задание 8
c = int(input('Введите трехзначное число:'))
z = c % 10
v = c // 100
b = (c // 10) % 10
x = v * 100 + z * 10 + b
print(x)

# Задание 9
x = int(input('Введите трехзначное число x:'))
z = x % 10
c = x - z
v = c // 10
r = z * 100 + v
print('Ответ n:', r)
n = int(input('Введите n:'))
f = n // 100
g = n - f * 100
h = g * 10 + f
print('Ответ x:', h)

# Задание 10
n = int(input('Введите n:'))
if n <= 100:
    print('Введите n>999:')
    n = int(input('n='))
z = (n % 1000) // 100
x = n // 1000
print('Число сотен:', z)
print('Число тысяч:', x)
