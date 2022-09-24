# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

print("Введите вещественное число")
number = input().split(".")
sum = 0
new_list= list(map(int, number[1]))
for i in range(len(new_list)):
    sum+= new_list[i]
print (sum)