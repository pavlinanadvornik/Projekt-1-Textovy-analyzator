import string

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user_name = input("username: ")
password = input("password: ")
registered = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}
line = 35 * "-"
number_of_texts = len(TEXTS)

print(line)

if user_name in registered and password == str(registered[user_name]):
    print(f"Welcome to the app, {user_name}! \nWe have {number_of_texts} texts to be analyzed.")
else:
    print(f"Nejsi registrovaný.")
    exit()
print(line)

text_number = input(f"Enter a number btw. 1 and {number_of_texts} to select: ")
text_number_int = int(text_number)

if text_number.isdigit():
    if text_number_int not in range(1,number_of_texts+1):
        print("Takové číslo textů nemáme.")
        exit()
else:
    print("Tohle není číslo")
    exit()

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
count = 0
word_lengths_dict = {}
words = TEXTS[text_number_int-1].split()

print("There are", len(words), "words in the selected text.")

for word in words:
    clean_word = word.strip(string.punctuation)
    if clean_word.istitle():
        titlecase += 1
    elif clean_word.isupper():
        uppercase += 1
    elif clean_word.islower():
        lowercase += 1
    elif clean_word.isdigit():
        numeric += 1
        count += int(clean_word)
    word_length = len(clean_word)
    word_lengths_dict[word_length] = word_lengths_dict.get(word_length, 0) + 1
print("There are", titlecase, "titlecase words.")
print("There are", uppercase, "uppercase words.")
print("There are", lowercase, "lowercase words.")
print("There are", numeric, "numeric strings.")
print("The sum of all the numbers: ", count)
print(line)
print(f"{'LEN':<3} | {"OCCURRENCES":<19} | {"NR.":>3}")
print(line)

sorted_word_lengths_dict = dict(sorted(word_lengths_dict.items()))

for key, value in sorted_word_lengths_dict.items():
    print(f"{key:<3} | {'*'*value:<19} | {value:>3}")
