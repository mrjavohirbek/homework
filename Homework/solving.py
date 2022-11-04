# 1. Вам дается текст:

stribg = """Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."""
# print(stribg.count('s'))
# print(stribg.count('t'))
# - Посчитайте количество букв  `s`  и  `t` .
# - Найдите все слова, которые начинаются с корня  `advert (регистр не должен учитываться) и превратите их все в верхний регистр

# print(stribg.lower().replace("advert", 'ADVERT'))
# 2. Дана строка нечетной длины больше 7 символов, вернуть строку, состоящую из трех средних символов данной строки

# Пример:

some_string = "Adverts"

# Output: "ver"

# 3. Дается 2 строки "Aidana" и  "Adilet" .  Вам нужно в результате получить смешанную строку из двух имен, буква за буквой.
a = 'adileta'
b = 'aidana'
#  Результат: "AAiddialneat"
# print(a[0]+ b[0]+ a[1])
# res = ''
# if len(a) != len(b):
#     res = 'кпц'
# else:
#     for i in range(len(a)):
#         res += a[i] +b[i]
# print(res)

# 4. Используйте текст с первого задания. Отделите каждое слово в отдельный элемент списка. Уберите точки, запятые, тире и кавычки. Удалите похожие слова (регистр не учитывается) и отсортируйте по алфавиту.
text_new = (
    stribg.replace(',', '')
    .replace('-', '')
    .replace('"', '')
    .replace("'", '')
    .replace('.', '')
)
res = sorted(list(set(text_new.lower().split())))
print(res)
#  Получите из кортежа число 20 и запишите в отдельную переменную
# 5.  aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
aTuple = (
    "Orange", [10, ('Aidana', [1, 2, {2: 3, "1": 'хомяк'}]), 20, 30], (5, 15, 25))
res = aTuple[1][1][1][2]
# print(res.get('1'))
# print(res.values())

# aa2 = [2,3,4,6]
# num = 0
# for i in aa2:
#     num += i
# print(num)
# print(sum(aa2))
# 6.  Найдите сумму цифр четырехзначного числа 3456 ( int )
x = 3456
x1 = []
x1 += str(x)
res = 0
for i in x1:
    res += int(i)
# print(res)
# 7 . Напишите программу, которая проверяет текст с первого задания и выводит два слова: наиболее часто встречающееся и самое длинное.


############################################################################################
############################################################################################
############################################################################################
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ РАУНД 2 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
############################################################################################
############################################################################################
############################################################################################

# У вас есть словарь студентов  IT Academy:
students = [
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
all_gender = []
for i in students:
    all_gender.append(i['gender'])
count_male = all_gender.count('Male')
count_female = all_gender.count('Female')
p_male = round(float(count_male / (count_female+count_male) * 100))
p_female = round(float(count_female / (count_female+count_male) * 100))
# 1) высните процентное соотношение мужского пола и женского.
# print(p_male)
# print(p_female)

# 2) выведите всех студентов с курса python
py_course = []
for i in students:
    if i['course'] == 'python':
        py_course.append(i['name'])
print(py_course)
# 3) уберите дубликаты курсов

# 4) выведите студентов, которые старше 30 и найдите процент их количества относительно других
students_age = []
for i in students:
    if i['age'] > 30:
        students_age.append(i['name'])
print(students_age)

# 5) отсортируйте студентов по:
# имени
# курсу
# полу
# возрасту

# 6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ?
# Напишите код

# 7) Добавьте по 5 новых студентов на курсы  java  и  python

# 8) Отчислите всех студентов младше 15 лет

# 9) Написать программу, которая проверяет пароль. До тех пор пока пароль не совпадет,
# программа должна спрашивать пароль. Причем, пароли могут быть равны одному из
# элементов списка `password_list = [‘password’, ‘12 3456’, ‘12345678’, ‘qwerty’, ‘abc123’, ‘monkey’, ‘1234567’]`. Нужно использовать бесконечный цикл, а также операторы break и continue

# 10) Распечатать числа от 23 до 87 включительно с шагом итерации 8, используя цикл for и функцию range

# #2) Необходимо удалить пустые строки из списка строк.
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
