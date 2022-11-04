music_list = ['Popstar', 'Woman', 'Saxobeat', 'Hola', 'Stay',
              'Dance Monkey', 'Psy', 'Juicy', 'Pure love', 'Bad guy']

music_list[3], music_list[7] = music_list[7], music_list[3]

print(music_list)

fruits = ['apple', 'banana', 'grapes', 'dragonfruit',
          'orange', 'pear', 'strawberry', 'kiwi']

fav_fruits = ['banana', 'orange', 'strawberry']

for i in fruits:
    if i in fav_fruits:
        print("I like " + i)
    else:
        print("I don't like " + i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(numbers[2:8])
print(numbers[::-1])

list = []

for i in range(0, 11):
    list.append(i)

print(list)

a = [1, 3, 4, 5]
b = [4, 5, 6, 7]

for i in a:
    if (i in b):
        b.remove(i)
print(b)

print(min(list))

print(list.clear())

sum = 0

for i in list:
    sum += i
print(sum)

print(sum / len(list))

list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for i in list2:
    print(i)
