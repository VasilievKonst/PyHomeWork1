x = int(input("Введите номер четверти координат: "))
if (x == 1):
    print("Диапазоном для 1 четверти координат является X > 0 и Y > 0")
elif (x == 2):
    print("Диапазоном для 2 четверти координат является X < 0 и Y > 0")
elif (x == 3):
    print("Диапазоном для 3 четверти координат является X < 0 и Y < 0")
elif (x == 4):
    print("Диапазоном для 4 четверти координат является X > 0 и Y < 0")
else:
    print("Такой четверти не существует! \nВведите корректное значение.")
