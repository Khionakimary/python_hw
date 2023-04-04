# Задача 10: 
# 2) Пользователь вводит число n. На следующих строках нужно вводить 1 или 0, 
# в ответе вывести количество наименее встречающихся из них 
# (т.е либо количество 0 либо 1, в зависимости от того, кого меньше)

from random import randint

n = int(input("Введите число N: "))
counter_0 = 0
counter_1 = 0
for i in range(n):
    temp = randint(0, 1) 
    print(temp, end=" ")   
    if temp == 0:
        counter_0 += 1
    else:
        counter_1 += 1
if counter_0 < counter_1:
    print(f"\nНаименее встречающимся числом являестя: 0, количество {counter_0}")
else:
    print(f"\nНаименее встречающимся числом являестя: 1, количество {counter_1}")