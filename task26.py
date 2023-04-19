# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def raiseNumberToPower(numA, numB): 
    if (numB == 1):                  
        return numA                   
    if (numB != 1):                   
        return (numA * raiseNumberToPower(numA, numB - 1)) 
    
numA = int(input("Введите число A: "))
numB = int(input("Введите число B: "))
result = raiseNumberToPower(numA, numB)
print(f"Результат возведения чила {numA} в степень {numB} равен: {result}")