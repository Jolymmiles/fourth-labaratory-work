n = int(input())
b = int(input('6 система : '))
n1 = ''
while n > 0:
    n1 = str(n % b) + n1
    n //= b
if ((n1 % 100000 <= 55555) and
        (n1 % 100 == 13) or (n1 % 100 == 14)):
    print('True')
else:
    print('False')
