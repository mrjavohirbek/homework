a = int(673.3123)
b = float(512)
c = int(float(str(192)))
d = float(173) + 5
e = str(193.000000000001)

print(a)
print(b)
print(c)
print(d)
print(e)

f = 'Calling ' + str(911)
g = 'abc' + 'xyz'

print(f)
print(g)

a2 = 589
b2 = 932.901

c2 = 'Hello world'
d2 = '892.01'

print(a2 + b2)
print(c2 + d2)

# Hello world589 892.01 932.901589 1481.01

a2, b2, c2, d2 = c2 + str(a2), d2, str(b2) + str(a2), 1481.01
print(a2, b2, c2, d2)
