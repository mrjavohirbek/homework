a = abs(float(input("Type a: ")))
b = abs(float(input("Type b: ")))

if (a > b):
    print(a)
elif (a < b):
    print(b)
else:
    print(f"{a} = {b}")

a2 = float(input("Type a2: "))
b2 = float(input("Type b2: "))

if (a2 != b2):
    print("Yes")
else:
    print("No")

a3 = float(input("Type a3: "))

if (a3 > 100 or a3 < -100):
    print("-")
else:
    print("+")

month = int(input("Type the number of the month: "))

if (month > 0 and month < 3 or month == 12):
    print("Winter")
elif (month >= 3 and month <= 5):
    print("Spring")
elif (month >= 6 and month <= 8):
    print("Summer")
elif (month >= 9 and month <= 11):
    print("Fall")
else:
    print("Error")

a4 = float(input("Type a4: "))
b4 = float(input("Type b4: "))
c4 = float(input("Type c4: "))

if (a4 > 10 and b4 > 10 and c4 > 10):
    print("Yes")
else:
    print("No")

a5 = float(input("Type a5: "))
b5 = float(input("Type b5: "))
c5 = float(input("Type c5: "))

ab = a5 + b5
bc = b5 + c5
ac = a5 + c5
abc = a5 + b5 + c5

if (a5 > 0 and b5 > 0 and c5 > 0):
    print(abc)
elif (a5 > 0 and b5 > 0):
    print(ab)
elif (b5 > 0 and c5 > 0):
    print(bc)
elif (a5 > 0 and c5 > 0):
    print(ac)
else:
    print("Error")

year_num = int(input("Type year number: "))
month_num = int(input("Type month number: "))

print(sum([(year_num * 12 * 29), (month_num * 29)]))

first_num = int(input("Type your first number: "))

if (first_num % 3 == 0 and first_num % 5 == 0):
    print("Wow, it is divisible by 3 and 5")
elif (first_num % 3 == 0 and first_num % 5 != 0):
    print("Arara")
elif (first_num % 3 != 0 and first_num % 5 == 0):
    print("Wow")
else:
    print("Error")

almaz = int(input("Type your age: "))

if (almaz > 0 and almaz <= 17):
    print("Too young")
elif (almaz >= 18 and almaz < 40):
    print("Let's go to the army")
elif (almaz >= 40):
    print("Too old")
else:
    print("Error")
