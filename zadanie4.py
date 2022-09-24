# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 5, 6]
if (len(list1) % 2 == 1):
    new_list = list((list1[i] * list1[-1*(i+1)]) for i in range (int(len(list1) /2 +1)))
else:
    new_list = list((list1[i] * list1[-1*(i+1)]) for i in range (int(len(list1) /2)))
print (new_list)