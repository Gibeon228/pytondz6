# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# print ("Введите число к")
# k = int(input())
# list = []
# sum = 0
# for i in range(1, k):
#     list.append((1+1/i) ** i)
#     sum += list[i]
# print (list)
# print (sum)


from functools import reduce
print ("Введите число к")
k = int(input())
list1 = ([((1+1/x) ** x) for x in range (1, k)])
sum = reduce((lambda x, y: x + y), list1)
print (list1)
print (sum)