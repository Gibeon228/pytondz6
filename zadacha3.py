# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce
list1 = [2, 3, 5, 9, 3]
new_list = [list1[x] for x in range (len(list1)) if x % 2 !=0]
print (new_list)
sum = reduce((lambda x, y: x + y), new_list)
print (sum)
