# # Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу,
# #  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random
# number = int(input('введите размер массива '))
# listInt = []
# for i in range(number):
#     listInt.append(random.randint(0, 100))  #создали рандомный массив
# print(listInt)
# sum = 0
# for i in range(len(listInt)):
#     if i%2 != 0:
#         sum += listInt[i]
# print(f'Сумма элементов на нечетных позициях равна {sum}')

 

import random
listInt = [random.randint(0,100) for n in range(int(input('введите размер массива ')))]
print(listInt)
sum = 0
for index, value in enumerate(listInt):
    if index%2:
        sum += value
print(f'Сумма элементов на нечетных позициях равна {sum}')
