# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


n = (int(input("введите число n: ")))
list_1=[]
for i in range(n):
    element = int(input("введите элементы списка : "))  
    list_1.append(element)

m = (int(input("введите число m: ")))  
list_2 = []
for i in range(m):
    element = int(input("введите элементы списка: "))  
    list_2.append(element)

print(list_1)             
print(list_2)
list_3 = list_1 + list_2     

for i in set(list_3):              
    if list_3.count(i) > 1:         
        print(i, end=" ")