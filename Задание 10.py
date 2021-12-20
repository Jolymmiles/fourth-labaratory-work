n = int(input('Введите n:'))
if n <= 100:
    print('Введите n>999:')
    n = int(input('n='))
z = (n % 1000) // 100
x = n // 1000
print('Число сотен:', z)
print('Число тысяч:', x)
