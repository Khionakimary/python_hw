# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def count_vowels_letters(text):
    counter = 0
    for x in text:
        if x in vowel_letters:
            counter += 1
    return counter

vowel_letters = 'уеыаоэяию'        
poems = input("Введите текст: ").lower().split()   

print(poems)    
count_vowels = [count_vowels_letters(text) for text in poems] 
if len(set(count_vowels)) == 1:
    print('Парам пам-пам')       
else:
     print('Пам парам')