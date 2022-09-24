# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
print("Введите число N")
N = int (input())
list1 = []
mult = 1
for i in range(N):
    list1.append(random.randint(-N, N))
print(list1)
list2 = list(map(int,input().split()))
print (list2)
for i in range(len(list2)):
    mult*= list1[list2[i]]
print (mult)