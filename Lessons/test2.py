# list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# for i in list2:
#     print(i)

# almaz = int(input("Type your age: "))

# if (almaz > 0 and almaz <= 17):
#     print("Too young")
# elif (almaz >= 18 and almaz < 40):
#     print("Let's go to the army")
# elif (almaz >= 40):
#     print("Too old")
# else:
#     print("Error")

# print(int(673.3123))

# lst = [2, 'ase', 342]
# print(lst[0], lst[-1])

# car = ["BMW", "Mersedes", "Tesla", "Volvo", "Audi"]

# n = 0
# for i in car:
#     n += 1
#     print(i, n)

# a = "идёт снег"

# x = a.find(' ')
# print(a[x+1:] + a[x] + a[:x])

# def name():
#     name = input("Name: ")
#     surname = input("Surname: ")
#     print(name, surname)


# name()

# def time():
#     hour = int(input("Hour: "))
#     minute = int(input("Minute: "))
#     second = int(input("Second: "))
#     print(hour * 60 * 60 + minute * 60 + second)


# time()

# def bank():
#     deposit = int(input("Deposit: "))
#     years = int(input("Years: "))
#     print(deposit + (deposit * 10 * 365 / 365 / 100) * years)


# bank()

# def sum():
#     a = int(input("a: "))
#     b = int(input("b: "))
#     print(a + b)


# sum()

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[::-1])

# lst = []

# for i in range(0, 101):
#     lst.append(i)

# print(lst)

# friends = {}

# name = input("Name: ")
# surname = input("Surname: ")

# friends.setdefault(name, surname)
# print(friends)


# def ages():
#     age = int(input("Age: "))
#     if age < 14:
#         print("Kid")
#     elif age >= 14 and age <= 18:
#         print("Teenager")
#     elif age > 18 and age <= 30:
#         print("Young man")
#     elif age > 30 and age <= 50:
#         print("Independent person")
#     elif age > 50:
#         print("Respected person")


# ages()

# age = " "

# while True:
#     age = int(input('Age: '))
#     if age > 18 and age < 50:
#         print("Stop")
#         break

# a = int(input("a: "))
# b = int(input("b: "))
# oper = input("Operation: ")


# def calc(a, b, operation):

#     if oper == "+":
#         print(a + b)
#     elif oper == "-":
#         print(a - b)
#     elif oper == "/":
#         print(a / b)
#     elif oper == "*":
#         print(a * b)
#     else:
#         print("Operation is incorrect")


# calc(a, b, oper)

# lst = []
# for i in range(10):
#     if (i % 2 == 1):
#         lst.append(i)

# print(lst)
