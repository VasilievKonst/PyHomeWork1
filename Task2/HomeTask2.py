x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))

ls = not (x or y or z)
rs = not x and not y and not z
res = ls == rs
print("Утверждение является: ", res)