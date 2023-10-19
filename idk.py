# долги
# n = int(input('Введите число: '))
# print((n-1) * (n+1))

# a = int(input('A:'))
# b = int(input('B:'))

# print(a ** b )

# a = int(input('A:'))
# b = int(input('B:'))
# c = int(input('C:'))
# print(a*b , b*c)

# k = int(input('конфеты: '))
# n = int(input('дети: '))
# print(k // n , k % n)

# a = int(input('A: '))
# b = int(input('B: '))
# print(max(a,b))

# print(len(input('A: ')))

# a = int(input('A: '))

# if a in range(3,6):
#     print('Весна')
# elif a in range(6,9):
#     print('Осень')

# if a in [12,1,2]:
#     print('Зима')

# x = int(input('число: '))
# s = ''
# while x != 0:
#     s += str(x %5)
#     x //= 5 
# print(s[::-1])

# x = int(input('число: '))
# s = ''

# while x != 0:
#     s += str(x % 3)
#     x // 3
# print(s[::-1] , s.count('2'))

# print('число кратное трём' if int(int('число: ')) % 3 == 0 else 'число не кратное трём')

# a = int(input('A: '))
# b = int(input('B: '))
# while a + b > 100:
#     a -= 4
#     b += 2
# print(a,b)

# a = int(input('A: '))
# while a % 2 != 0 or a > 100: a -= 7
# print(a)

# s = 0 
# n = int(input('N: '))
# for i in range(n): s += int(input(f'число {i+1}:'))
# print(s if s % 2 == 0 else 2* s)

# sp = 0
# sm = 0
# n = int(input('N: '))
# for i in range(n):
#     a = int(input(f'число {i + 1 }: '))
#     if a > 0:
#         sp += a
#     else:
#         sm += a
# print(sp , sm)

# count = 0
# for i in range(10000 , 100001): count += 1 if i % 3 == 0 and i % 9 == 0 else 0
# print(count)

# a = 15
# b = 19
# c = max(a + 10, b) - min(a, b - 10)
# print(c)

# a = int(input('A: '))
# b = int(input('B: '))
# c = int(input('C: '))

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)


# a = int(input('A: '))
# b = int(input('B: '))
# c = int(input('C: '))

# print(max(a,b,c) - min(a,b,c))

# arr = []
# n = int(input('N: '))
# for i in range(n): arr.append(int(input(f'число {i + 1}:')))
# print(min(arr))

# arr = []
# n = int(input('N: '))
# for i in range(n):
#     a = int(input(f'число {i + 1}:'))
#     if a % 3 == 0: arr.append(a)
# print(max(arr) if len(arr) != 0 else -1)

# arr = []
# n = int(input('N: '))
# for i in range(n):
#     a = int(input(f'число {i + 1}:'))
#     if a % 5 == 0 and a % 10 != 0: arr.append(a)
# print(max(arr) if len(arr) != 0 else -1)

# n = int(input('N: '))
# s = 0 
# ch = []
# nch = []
# for i in range(n):
#     a = int(input(f'число: {i + 1}:'))
#     s += a 
#     ch.append(a) if a % 2 == 0 else nch.append(a)
# print('повезло' if s == max(ch) * min(nch) else 'в следующий раз')

import os
import random
import time

clear = lambda: os.system('cls')

print('hello, I guessed one word. Your task guess this word use letters!')
input('click Enter for continue')
clear()
time.sleep(1)
print('lets go')
time.sleep(1)

words = ['calm', 'table' , 'cinema' , 'window' , 'floor' , 'light' , 'cat' , 'bottle' , 'glass']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    
    for symb in word:
        if symb in letters:
            print(symb , end = ' ')
        else:
            print('*' , end = ' ')
            isWin = False
    print()

    if isWin:
        print('well done! you are guessed')
        break
    letter = input('write letters: ')
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
        print(f'you have: {hp}')

if hp == 0:
    print('you are lost! you havent more attempts...')




















