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
