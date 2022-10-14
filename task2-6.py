# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число  '))
# listN = [1]
# for i in range (1, n):
#     listN.append((i+1)*listN[i-1])   # 1  1*2  1*2*3  1*2*3*4   1*2*3*4*5    1*2*3*4*5*6
# print(listN)

n = int(input('Введите число  '))
listN = [n for n in range(1, n+1)]
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
listN = list((map(fact, listN)))
print(listN)

 