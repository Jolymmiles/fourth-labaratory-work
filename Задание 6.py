b = int(input('Введите двухзнанчое число:'))
a = int(input('Введите однозначное число:'))
z = a + b
b2 = z % 10
b1 = z // 10
print('Сумма заданых чисел:', z)
print('Число едениц:', b2)
print('Число десятков:', b1)
