# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

def NumbersSum(numA, numB): 
    if (numA == 0):                   
        return numB                  
    if (numB == 0):                   
        return numA                   
    if (numA != 0 and numB != 0):                               
        return NumbersSum(numA-1, numB+1)
    
    
numA = int(input("Введите число A: "))
numB = int(input("Введите число B: "))
result = NumbersSum(numA, numB) 
print(f"Сумма чиcел {numA} и {numB} равна: {result}")