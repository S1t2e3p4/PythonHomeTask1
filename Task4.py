# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))
print('')

if quarter == 1:
    print('К первой четверти относятся точки у которых диапазон возможных координат удовлетворяет условию: x > 0 и y > 0')
elif quarter == 2:
    print('Ко второй четверти относятся точки у которых диапазон возможных координат удовлетворяет условию: x < 0 и y > 0')
elif quarter == 3:
    print('К третьей четверти относятся точки у которых диапазон возможных координат удовлетворяет условию: x < 0 and y < 0')
elif quarter == 4:
    print('К четвёртой четверти относятся точки у которых диапазон возможных координат удовлетворяет условию: x > 0 and y < 0')
else:
    print('ERROR!')