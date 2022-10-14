# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input("введите число n "))
# m = -n
# while m<0:
#     print(f"{m}")
#     m = m+1
# while m<n+1:
#     print(f"{m}")
#     m = m+1

 

n = int(input("введите число n "))
print([n for n in range(-n, n+1)])