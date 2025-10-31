print("---------------------------------------------------------- BREAK ")  #break přeskočí i else

index = 1

while index <= 6:
   print("index:", index)
   # Pokud je index 4 vypiš a ukonči smyčku 
   if index == 4:
       print("Mám hodnotu 4")
       break
   index = index + 1


print("---------------------------------------------------------- CONTINUE ")

index = 0

while index <= 19:
   index = index + 1
   # pokud je aktuální hodnota proměnné sudá, 
   # pokračuj dále(přeskoč ji)
   if index % 2 == 0:
     continue
   print("index:", index)

print("---------------------------------------------------------- ELSE ")

index = 0

while index < 5:
   print("index:", index)
   index = index + 1

# vypíše se po ukončení smyčky
else:
   print("index:", index, "--> hodnoty jsou si rovny, ukončuji smyčku..")

print("Pokračuji..")


print("---------------------------------------------------------- CVIČENÍ ")

"""
kosik = []
while len(kosik) < 3:
   produkt = input("Zadej produkt: ")
   kosik.append(produkt)
   print("---")
print(kosik)

"""

"""
kosik = []
while True:                                                     # nekonečný while cyklus
   produkt = input("Zadej slovo. Pro ukončení napiš quit.")
   print(produkt)
   kosik.append(produkt)
   print("---")
   if produkt == "quit":
      break
   else:
      print(kosik)
print(kosik)

"""

print("---------------------------------------------------------- WALRUS := MROŽ operátor")

jmeno = "Matouš"
print(jmeno)

print(name := "Pajinka")

"""

TEXT = "Zapiš jméno: "

if (jmeno_1 := input(TEXT)) == "Matouš":
   print("Toto je ", jmeno_1, sep="")
else:
   print("Tak ", jmeno_1, ", toho neznám.", sep="")

"""

"""
TXT = "Zapiš libovolný text [nebo q pro ukončení]: "

vstup = input(TXT)

while (vstup := input(TXT)) != "q":
   print(vstup)
else:
   print(vstup, "Konec smyčky!", sep="\n")

"""


"""
kosik = []
while (produkt := input("Zadej slovo. Pro ukončení napiš quit.")) != "quit":
   kosik.append(produkt)
  
print(f"Ve vašem nákupním košíku je: {kosik}")

"""

print("---------------------------------------------------------- AUGMENTED ASSIGNMENT")


x = 2
x += 3
print(x)



print("---------------------------------------------------------- LIST COMPREHENSIONS") # ideálně používat, když vytvořím prázdný list a pak do listu něco přidávám

data = [1, 2, 3, "a", 5, 6, "@", "7", 7]
dvojnasobek = []
for cislo in data:
   if isinstance(cislo, int):
      dvojnasobek.append(cislo * 2)
print(dvojnasobek)

dvojnasobek_2 = [cislo_2 * 2 for cislo_2 in data if isinstance(cislo_2, int)]
print(dvojnasobek_2)



print("----------------------------------------------------------- ZÁVĚREČNÝ ÚKOL LEKCE: FIBONACCIHO POSLOUPNOST")

x = 0
y = 1
vysledky = [x, y]
delka_rady = 15

while len(vysledky) != delka_rady:
   vysledek = x + y
   print("x", x, "y", y, "vysledek", vysledek)
   vysledky.append(vysledek)
   x = y
   y = vysledek
   print("x", x, "y", y, "vysledek", vysledek)
print(vysledky)

print(f"Fibonacci: {vysledky}")


   

