# Задайте последовательность цифр. Напишите программу, которая выведет 
#   список неповторяющихся элементов исходной последовательности.
# spisok = [1,2,3,4,1,5,4,8,7]
# print(spisok)
# for i in spisok:
#     if spisok.count(i) == 1:
#         print(i)

import random
spisok = [random.randint(0,10) for n in range(int(input('введите размер списка ')))]
print(spisok)
spisok_count= list(zip(list(spisok.count(i) for i in spisok), spisok))
for count, num in spisok_count:
    if count == 1:
        print(num)
           