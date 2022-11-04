# # s = []

# # for i in s:
# #     s.append(0)
# # print(len(s))

# dict1 = {"name": "Mike", "salary": 80000}
# temp = dict1.pop("age")
# print(temp)

# a = []
# a += "Python"
# b = ["Python"]

# if a == b:
#     print(True)
# else:
#     print(False)


# x = [10, [3.141, 20, [30, 'qqz', 2.718]], 'foto']
# # x[1][2][3]
# x[1][2][1][2]

# a = ['foo', 'bar ', 'baz', 'qux', 'quux', 'corge']
# print(a[4::-2])

# f = 420
# f1 = 69
# f2 = 228
# f, f1, f2 = f2, f, f1
# print(f, f1, f2)

# nums = [1, 2, 3, 4]
# x = 1

# for i in range(len(nums)):

#     x *= i
# print(x)

# a = []
# a.append(a)
# print(a)

# lst = [14, 7, 2]
# string = "{2}{1}{2}{0}".format(lst[0], lst[1], lst[2])
# print(string)

# x = [1 ,2, 3]
# print(x in x)

# a = not bool("False")

# if not a:
#     a = a + 1
#     print(a)

# lst = [].append(5)
# print(lst)

# print(type(1/2))

# pi = 3.14
# print(f'{pi=}')

# x = True * 1
# if True + False:
#     False + True
#     print(x)
# else:
#     print(0)

# a = [1, 2, 3]
# b = a

# print(b[0], end='')
# a = [6, 7, 8]
# print(b[0], end= '')

# a = [0, 2, -4, -2, 1]

# for i in a:
#     if i < 0:
#         a.append(abs(i))
#         x = i
# print(x)

# a, b, *c = [i for i in range(0, 16, 4) if i % 4 == 0]
# print(len(c))

# lst = list ((1, 2, 3, 4, 5))

# if isinstance(lst, list):
#     print(lst[1:3] + lst[5:4])
#     print(str(8/1**2**2) == str(8/2**2**1))

# txt = 'AnyText'
# print(txt[-1::])

# lst = [1, 2, 3, 4]
# r= 1
# for i in range(len(lst)):
#     r*= i
# print(r)

# lst = [print(i) for i in range(100)]
# print(len(set(lst)))

# a = [2, 1, 2, 4]
# a[1:].remove(2)
# print(sum(a))

# a = [1,2,3,2]
# b = {1,2,3,2}

# print(set(a) == b)
# print(a == list (b))

# nums = ['one', 'two', 'three', 'four']
# num_dict = {x[0]: x for x in nums}
# print(num_dict['t'])
# nums = {1, 2, 3, 4, 5}
# nums = {0, 1, 2, 3} & nums
# nums = list(filter(lambda x: x > 1, nums))
# print(len(nums))

# a = [1, 2**2]
# b = [1, 2*2]

# x = 2*2
# y = 8/2

# if(x is y) | (a is b):
#     print(1)
# else:
#     print(0)
