
print("4. lekce")
print("--------------------------------------------------------------- ÚKOL S FOR CYKLEM - SOUČET A NÁSOBENÍ")

seznam_cisel = [11, 22, 47, 33, 45, 77, 58, 42, 12, 34, 17, 112, 228]

soucet, nasobeni = 0, 1

for cislo in seznam_cisel:
    soucet += cislo
    nasobeni *= cislo

print(f"suma je {soucet}, produkt je {nasobeni}")

print("--------------------------------------------------------------- ÚKOL S FOR CYKLEM - SUDÁ ČÍSLA ")


numbers = [11, 22, 47, 33, 45, 77, 58, 42, 12, 34, 17, 112, 228]
soucet_2, nasobeni_2 = 0, 1

for num in numbers:
    if not num % 2:
        soucet_2 += num
        nasobeni_2 *= num

print(f"suma je {soucet_2}, produkt je {nasobeni_2}")

print("--------------------------------------------------------------- FOR CYKLUS - break, continue, pass ")

for letter in "Matous":
    if letter == "t":
        break
    print(letter)
print("-" * 10, "Konec smyčky!", "-" * 10, sep="\n")
      

print("--------------------------------------------------------------- FOR CYKLUS - ÚKOL S BREAK")


sekvence = [11, 22, 47, 33, 45, 77, 58, 42, 12, 34, 17, 112, 228]
soucet_3 = 0
nasobeni_3 = 1

for n in sekvence:
    soucet_3 += n
    nasobeni_3 *= n

    if n > 50:
        break

print(soucet_3)

print("--------------------------------------------------------------- FOR CYKLUS S CONTINUE ")

for number in [1, 11, 2, 33, 34, 7, 8]:
    if number > 10:
        continue
    print(number)



print("--------------------------------------------------------------- FOR CYKLUS - ÚKOL S CONTINUE ")


sekvence = [11, 22, 47, 33, 45, 77, 58, 42, 12, 34, 17, 112, 228]

soucet_4 = 0
for cislo in sekvence:
    if cislo % 2:
        continue

    soucet_4 += cislo

print(f"Suma je {soucet_4}")


print(str(12326)[-1] in "13579")  # zjistím, jestli je sudá nebo lichá bez použití %



print("--------------------------------------------------------------- FOR CYKLUS - ÚKOL S CONTINUE ")

csv_data = [
    'jmeno;prijmeni;email;projekt',
    'Matous;Holinka;m.holinka@firma.cz;hr',
    'Petr;Svetr;p.svetr@firma.cz;devops'
]

for line in csv_data:
    print("===")

    for cell in line.split(";"):
        print(cell)



print("--------------------------------------------------------------- FOR CYKLUS - ÚKOL: Pomocí vnořených for cyklů vypiš malou násobilku 1-5 ")


for a in range(1, 6):
    for b in range(1, 6):
        print(a * b, end=" ")
    print()
        

print("--------------------------------------------------------------- FOR CYKLUS - ÚKOL S RANGE")

soucet_milion = 0
for cisla in range(1, 1000000):
    soucet_milion += cisla

print(soucet_milion)

print("--------------------------------------------------------------- FUNKCE ENUMERATE ")


jmena = ("Java", "C", "Rust", "Python")
print(tuple(enumerate(jmena)))

print("--------------------------------------------------------------- FUNKCE ZIP ")

first_names = ("Petr", "Marek", "David")
surnames = ("Svetr", "Pavel", "Dvořák")

print(zip(first_names, surnames))
print(list(zip(first_names, surnames)))

print("--------------------------------------------------------------- ÚKOL S RANGE")

"""
pocet_hodnot = int(input("Kolik hodnot chceš zadat?"))

hodnoty = []

for x in range(pocet_hodnot):
    numb = input(f"Zadej {x+1}. hodnotu: ")

    if not numb.isdigit():
        continue

    hodnoty.append(int(numb))

if len(numb) < pocet_hodnot:
    print(f"Zadal jsi jen {len(numb)} hodnot.")

if len(numb) == 0:
    print("Nemůžu vybrat min a max.")
else:
    print(f"Minimum je {min(hodnoty)}, maximum {max(hodnoty)}.")

"""


print("--------------------------------------------------------------- ÚKOL S ENUMERATE ")
"""
names = input("Zadejte čárkou oddelený seznam jmen: ")
ordered_names = {}


for i, name in enumerate(names.split(",")):
    if name in ordered_names:
        print(f"{name} jiz v seznamu je s pozici {ordered_names[name]}")
        continue
    
    ordered_names[name] = i
    
print(ordered_names)

"""


print("--------------------------------------------------------------- ÚKOL K LEKCI 4")


samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for x in range(len(veta)):
      
    if not veta[x].isalpha():
        continue
   
    if veta[x].lower() in samohlasky:
        vysledky["samohlasky"] += 1

    if veta[x].lower() in souhlasky:
        vysledky["souhlasky"] += 1
print(f"Počet souhlásek: {vysledky['souhlasky']} | Počet samohlásek: {vysledky['samohlasky']}")

print(vysledky)


print("--------------------------------------------------------------- ÚKOL K LEKCI 3")


jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if jmeno in uzivatel and heslo == uzivatel["Marek"]:
    zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
    zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"

print(zprava)










