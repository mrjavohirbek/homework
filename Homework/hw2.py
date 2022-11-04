name = input("What's your name? ")

print(f"Hello, my friend {name}\n" * 5)

name = input("What's your name? ")
age = int(input("How old are you? "))
job = input("What do you do? ")
it = input("What IT sphere do you like? ")
language = input("What programming language do you work on? ")

bio = """
Name: {0}
Age: {1}
Job: {2}
IT: {3}
Language: {4}
""".format(name, age, job, it, language)

print(bio)

word = input("Type your word: ")
print(f"{word} \n" * len(word))

palindrome = input("Type your word: ").lower()

reverse = palindrome[::-1]

if (palindrome == reverse):
    print("Your word is palindrome")
else:
    print("Your word is not palindrome")

word2 = input("Type your word: ")
print(word2[0], word2[-1])

number = "123456789"

print(number[slice(0, None, 2)], number[slice(1, None, 2)])
