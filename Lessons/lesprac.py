# Есть программа, которая запрашивает ваши любимые песни(бесконечно)
# И выводит список любимых песен

# Вам необходимо вывести только уникальные значения из списка(список прошлого задания) в независимости от их регистра(Большие или маленькие буквы)
# Сохранять все песни в словарь(первое задание). Ключом будут числа от 1 и по возрастанию. {1: “Название песни”, 2: “Название песни”} и тд.

songs = []
songs2 = {}

while True:
    a = input("Your favorite song: ")
    songs.append(a)
    set_res = set(songs)
    print("Unique songs: ")
    songs_res = (list(set_res))
    for i in songs_res:
        print(i)
    n = 0
    for i in songs:
        n += 1
        songs2[n] = i
    print(songs2)

# Мне нужна функция, которая принимает числа и возвращает строку из этого числа. Если же пользователь отправил аргумент не интежер вернуть строку “Принимаю только числа”

nums = []


def numbers():
    try:
        a = float(input("Type your number: "))
    except:
        print("Only numbers")
    else:
        nums.append(a)


while True:
    numbers()
    print(nums)


# вывести только уникальные значения из списка
# ["a", "b", "a", "c", "c"]

lists = ["a", "b", "a", "c", "c"]
unique_lists = list(set(lists))
print(unique_lists)


# Создать lambda функцию, которая возвращает квадрат числа

def square(n): return n * n


print(square(4))

# Создать  lambda функцию, которая принимает два аргумента и возвращает произведение этих чисел.


def mult(a, b): return a * b


print(mult(3, 4))

# написать функцию, которая находит факториал числа


def fact():
    n = int(input("Enter your number: "))
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print(factorial)


fact()

# Напишите функцию с именем show_stars (rows). Если аргумет rows
# равен 5 то выдов должен быть таким :
# Пример:
# *
# **
# ***
# ****
# *****


def show_stars(rows):
    if rows == 5:
        print('\n'.join('*' * i for i in range(1, rows + 1)))


show_stars(5)


# Напишите функцию с именем fizz_buzz, которая принимает число.
# ● Если число делится на 3, оно должно вернуть «Fizz».
# ● Если он делится на 5, он должен вернуть «Buzz».
# ● Если он делится как на 3, так и на 5, он должен вернуть «FizzBuzz»
# ● В противном случае он должен вернуть то же число.


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 != 0:
        print("fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("buzz")
    elif n % 3 == 0 and n % 5 == 0:
        print("fizz_buzz")
    else:
        print(n)


fizz_buzz(15)


# Hаписать функцию is_prime, принимающую 1 аргумент — число от 0 до
# 1000, и возвращающую True, если оно простое, и False - иначе.


def is_prime(n):

    if n < 2:

        return False

    if n == 2:

        return True

    limit = n**(1/2)

    i = 2

    while i <= limit:

        if n % i == 0:

            return False

        i += 1

    return True


print(is_prime(int(input("Enter: "))))


# Является ли число палиндромом. Если да, то должен напечатать True иначе false


def palindrom(n):
    n = str(n)
    if n == n[::-1]:
        print("True")
    else:
        print("False")


palindrom(344)
