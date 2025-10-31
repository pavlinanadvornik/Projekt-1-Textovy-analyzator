
print("----------------------------------------------TEST ")
print(type(10.5))
print(11 % 3)
print("Hello" + "World")
print(bool(""))
x = 4
print("A") if x > 0 else print("B")

if 1 and "None" and [""]:
    print("Ano")


print("---------------------------------------------- DICTIONARY ")


uzivatel = {
    "jmeno": "Matouš",
    "vek": 55,
    "volny_cas": ["klavír", "čtení", "Python"],
    "kontakt": {
        "telefon": "000 123 456 789",
        "email": "lukas@gmail.com",
        "web": "www.lukas.cz"
        }
    }

print(uzivatel["vek"])
print(uzivatel["volny_cas"][2])

uzivatel["hobby"] = "fotbal"

print(uzivatel)
print(uzivatel["jmeno"])
print(uzivatel["kontakt"]["email"])

kopie_slovniku = uzivatel.copy()
kopie_slovniku["jmeno"] = "Lalalla"

print(uzivatel)
print(kopie_slovniku)

# del uzivatel["jmeno"]

vek = uzivatel.pop("vek")
print(vek)
#vek = uzivatel.popitem()

print(uzivatel.keys())
print(uzivatel.values())
print(uzivatel.items())

print(list["mrkev"])
print(dict((("a", 3), ("b", 4)))) #převede se na dict.

print(uzivatel.get("jmeno"))   #GET vypíše hodnotu jen v případě, že existuje
print(uzivatel.get("pohlavi"))

print(uzivatel.clear())


print("-----------------------------------------------------------------KALKULAČKA S POUŽITÍM FUNKCE")

"""
operator = input("Zadejte operátor: ")
x = input("Zadejte čislo X: ")
y = input("Zadejte čislo Y: ")
result = 0

OPERATIONS = {
   "+": lambda x, y: x + y,
   "-": lambda x, y: x - y,
   "*": lambda x, y: x * y,
   "**": lambda x, y: x ** y,
}

if x.isdigit() and y.isdigit():
   x = int(x)
   y = int(y)

   if operator in OPERATIONS:
      result = OPERATIONS[operator](x, y)
      print(f"{x} {operator} {y} = {result}")

   else:
      print("nezadal jsi operátor (+, -, /, *)")

else:
   print("Nazadal jsi čísla pro x a y.")

   """



print("--------------------------------------------------------- ÚKOL S DICTIONARY")
"""
student = {
    "jmeno": input("Zadej jméno studneta: "),
    "vek": input("Zadej věk studenta: "),
    "znamky": [
        int(input("Zadej 1. známku: ")),
        int(input("Zadej 2. známku: ")),
        int(input("Zadej 3. známku: "))
    ]
}

print(student)

average = sum(student["znamky"]) / 3

if average < 2:
    print("Student je výborný.")
elif average < 4:
    print("Student je průměrný")
else:
    print("Student je špatný.")


"""


print("----------------------------------------------------- DATOVÝ TYP SET = MNOŽINA") # unikátní hodnoty, nemá pořadí, jde měnit

"""
zensky_rod = {"žena", "růže", "píseň", "kost"}
print(zensky_rod) # neudržuje pořadí

print(" sjednocení |, průnik &, rozdíl -, symetrický rozdíl stříška")

muj_novy_set = set()
suda_cisla = {2, 4, 6, 8}

pismena = set("abcdeffffffffffffff") # f zobrazí jen jednou
print(pismena)

POSITIVE_ANSWERS = {"ano", "jo", "jsem", "true"} # velkými písmeny se píše, když nemáme v plánu to měnit

client = {
    "first_name": str(input("Zadejte jméno: ")),
    "last_name": str(input("Zadjte příjmení: ")),
    "age": int(input("Zadejte věk: ")),
    "balance": float(input("Zadejte zůstatek zaokrouhlený na celé koruny: ")),
    "currency": str(input("Zadejte měnu: ")),
    "PEP": True if input("Jste PEP?").lower() in POSITIVE_ANSWERS else False

}

print(f"Já, {client["first_name"]}, {client["last_name"]} ({client["age"]}) souhlasím, aby mi byl v bance Z1 založen účet. Na účet tímto vkládám {round(client["balance"])} {client["currency"]}." + "Jsem PEP. " if client["PEP"] else "")

"""

print("-------------------------------------------- MAP")

a = ["1", "2", "3", "4", "5"]
a1 = list(map(int, a))
print(a1)



"""
numbers = list(map(int, input("Zadej sekvenci čísel oddělené mezerou: ").split()))

print(numbers)
print(numbers[0], numbers[1], sep="\n")
print(*numbers, sep="\n")           #hvězdička - vezme vše
print(f"Soucet je {sum(numbers)}")

"""


print("-------------------------------------------- PRÁCE SE SLOVNÍKY")


# Metoda "items" vrací speciální objekt 
# obsahující tuple pro každý klíč a hodnotu
muj_slovnik = {"jmeno": "Lukas", "email": "lukas@gmail.com"}
print(muj_slovnik.items())



# Metoda "get" vrací hodnotu zadaného klíče, pokud existuje
muj_slovnik = {"jmeno": "Lukas", "email": "lukas@gmail.com"}
print(muj_slovnik.get("jmeno"))
print(muj_slovnik.get("adresa"))
print(muj_slovnik.get("vek", "Klic neexistuje!"))


# Metoda "pop" odstraní podle zadaného jména klíč i jeho hodnotu
muj_slovnik = {"jmeno": "Lukas", "email": "lukas@gmail.com"}
print(muj_slovnik.pop("email"))
print(muj_slovnik)


print("------------------------------------------------------------- ÚKOL")

jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if jmeno in uzivatel and uzivatel[jmeno] == heslo:
    zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
    zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"


g = 3

if g not in range(1,6):
    print(g)







