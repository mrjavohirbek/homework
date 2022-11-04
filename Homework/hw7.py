fruits = ['apple', 'banana', 'grapes', 'dragonfruit',
          'orange', 'pear', 'strawberry', 'kiwi']

n = 0
for i in fruits:
    n += 1
    print(n, i)

lst1 = [1, 3, 5, 7, 9]
lst2 = [3, 8, 6, 5]

for i in lst2:
    if i in lst1:
        lst1.remove(i)
print(lst1)


lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
lst3 = []

for i in lst:
    if (i % 2 == 0):
        lst3.append(i / 4)
    else:
        lst3.append(i * 2)

print(lst3)

num = 3384456779

s = str(num)
print(max(s))

Days = {
    '01': 'first', '02': 'second', '03': 'third',
    '04': 'fourth', '05': 'fifth', '06': 'sixth',
    '07': 'seventh', '08': 'eighth', '09': 'ninth',
    '10': 'tenth', '11': 'eleventh', '12': 'twelfth',
    '13': 'thirteenth', '14': 'fourteenth', '15': 'fifteenth',
    '16': 'sicteenth', '17': 'seventeenth', '18': 'eighteenth',
    '19': 'nineteenth', '20': 'twentieth', '21': 'twenty first',
    '22': 'twenty second', '23': 'twenty third', '24': 'twenty fourth',
    '25': 'twenty fifth', '26': 'twenty sixth', '27': 'twenty seventh',
    '28': 'twenty eighth', '29': 'twenty ninth', '30': 'thirtieth',
    '31': 'thirty first'
}

Months = {
    '01': 'January', '02': 'February', '03': 'March',
    '04': 'April', '05': 'May', '06': 'June',
    '07': 'July', '08': 'August', '09': 'September',
    '10': 'October', '11': 'November', '12': 'December'
}

data = '01.01.2000'

DateInput = data.split('.')
print('Today is the ' + Days[DateInput[0]] + ' of ' + Months[DateInput[1]] +
      ' ' + DateInput[2])

my_list = [1, 2, 3, 4, 5, 5, 4, 5, 6, 7, 8, 10, 10, -1, -2, -1]

print(list(set(my_list)))

type = " "

while type != 'No':
    type = input('Shall we start? Yes/No : ')
    if type == 'Yes':
        date = input('Enter the date in the format dd.mm.yyyy: ')
        Date = date.split('.')

        if len(date) == 10:
            dd, mm, yyyy = date.split('.')
            if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
                if dd.isdigit() and mm.isdigit() and yyyy.isdigit():
                    if (1 <= int(dd) <= 31) and (1 <= int(mm) <= 12) and (1 <= int(yyyy) <= 9999):
                        if dd == '31' and (mm in ['01', '03', '05', '07', '08', '10', '12']):
                            print('Today is the ' + Days[Date[0]] + ' of ' + Months[Date[1]] +
                                  ' ' + Date[2])
                        elif int(dd) < 31:
                            print('Today is the ' + Days[Date[0]] + ' of ' + Months[Date[1]] +
                                  ' ' + Date[2])
                        else:
                            print('Wrong format')
                            continue

                    else:
                        print('Wrong format')
                        continue
                else:
                    print('Format is incorrect: ')
                    continue
            else:
                print('Format is incorrect: ')
                continue
        elif len(date) < 10:
            print('Digits are not sufficient')
        elif len(date) > 10:
            print('Too many numbers')
print('Bye')
