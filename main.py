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

print(30 * "-")

registered = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}


if user_name in registered and str(password) == str(registered[user_name]):
    print(f"Welcome to the app, {user_name}! \nWe have {len(TEXTS)} texts to be analyzed.")
else:
    print(f"Nejsi registrovaný.")
    exit()

print(30 * "-")

text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if text_number.isdigit():
    if int(text_number) not in range(1,len(TEXTS)+1):
        print("Takové číslo textů nemáme.")
        exit()
else:
    print("Tohle není číslo")
    exit()


cislo_textu = int(text_number)

print("There are", len(TEXTS[cislo_textu-1].split()), "words in the selected text.")

words = TEXTS[cislo_textu-1].split()
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
count = 0

for x in range(len(words)):
    if words[x][0].isupper() and words[x][1:].islower():
        titlecase += 1
    if words[x][0:].isupper():
        uppercase += 1
    if words[x][0:].islower():
        lowercase += 1
    if words[x][0:].isdigit():
        numeric += 1
        count += int(words[x])

print("There are", titlecase, "titlecase words.")
print("There are", uppercase, "uppercase words.")
print("There are", lowercase, "lowercase words.")
print("There are", numeric, "numeric strings.")
print("The sum of all the numbers: ", count)

delka_slov = {}

for xy in range(len(words)):
    ciste_slovo = words[xy].strip(",.:!")
    delka_slova = len(ciste_slovo)
    
    if delka_slova in delka_slov:
        delka_slov[delka_slova] += 1
    else:
        delka_slov[delka_slova] = 1
    

print(35 * "-")
print(f"{"LEN":<3} | {"OCCURRENCES":<19} | {"NR.":>3}")
print(35 * "-")
sorted_delka_slov = dict(sorted(delka_slov.items()))

for klic, hodnota in sorted_delka_slov.items():
    print(f"{klic:<3} | {"*"*hodnota:<19} | {hodnota:>3}")

