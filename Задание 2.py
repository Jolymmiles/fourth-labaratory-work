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
