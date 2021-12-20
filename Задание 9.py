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
