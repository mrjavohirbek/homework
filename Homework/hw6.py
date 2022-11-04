for i in range(5):
    print(i, 0)

sum = 0

for i in range(101):
    sum += i
    print(sum)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = [a, b, c]

if len(set(d)) == len(d):

    print("Error")

else:

    print("Yes")

a2 = int(input("a2: "))
b2 = int(input("b2: "))
c2 = int(input("c2: "))

if a2 + b2 == c2 or b2 + c2 == a2 or a2 + c2 == b2:

    print("Yes")
else:
    print("Error")

a3 = int(input("a3: "))
b3 = int(input("b3: "))
c3 = int(input("c3: "))
print((a3 > 0) + (b3 > 0) + (c3 > 0))

for i in range(1, 497):
    if (i % 2 == 0):
        print(i)

sum2 = 0

for i in range(0, 15):
    sum2 += i
    print(sum2)

i = 1

for i in range(1, 9435, 2):
    i *= i
print(i)

mass = []

for i in range(54, 9185):

    if i % 5 == 0:

        mass.append(i)

print(mass)

A = int(input("A: "))
B = int(input("B: "))

if A < B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)

n = int(input("n: "))

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)
