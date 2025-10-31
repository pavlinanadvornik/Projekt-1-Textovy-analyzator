from random import randint


print("ahoj Pajinko")

print("m" in "matous")

print("--------------------------------------------------- INPUT")

#x1 = input("První číslo: ") # výsledkem funkce input je vždy string
#x2 = input("Druhé číslo: ")
# print(x1 + x2)


#x = int(input("Zadej x: "))
#y = int(input("Zadej y: "))

#print(f"x = {x}, y = {y}")


message = "Ahoj, světe!"
print(sorted(message))
print(len(message))
print(message[4:-2])


print("--------------------------------------------------- LOWER, UPPER, TITLE, REPLACE, INDEX")

msg = "Ahoj Antoníne"

msg_lower = msg.lower()
msg_uuper = msg.upper()
msg_title = msg.title()
msg_replace = msg.replace("Antoníne", "Franto")
msg_index = msg.index("A")

print(msg_lower, msg_uuper, msg_title, msg_replace, msg_index)

print("--------------------------------------------------- INDEX")

print("Ahoj sousede!".index("o"))
print("Ahoj sousede!".index("soused")) #vrátí pořadí prvního písmene v řetězci


print("--------------------------------------------------- COUNT")

print("nejzdevětadevadesáteronásobitelnější".count("e"))


print("--------------------------------------------------- SPLIT")

numbers = "1, 2, 3, 4, 5, 6, 7"
print(numbers.split())

numbers2 = "1,2,3,4,5,6"
print(numbers2.split(","))

ma_veta = "Dnes je středa."
print(ma_veta.split())

print("--------------------------------------------------- JOIN")
moje_parta = ("Jirka", "Petr", "Andrea")
x = ", ".join(moje_parta)
print(x)


print("--------------------------------------------------- ÚKOL SE SPLIT A JOIN")

#jmena = input("Zadej jména oddělená čárkou: ").split(", ")
#print(jmena)

#print("Jména jsou: " + " a ".join(jmena))


print("--------------------------------------------------- IS NĚCO")
print("13".isdigit())
print("AHOJ".isupper())


print("--------------------------------------------------- PODMÍNKY")

if 3 > 2:
    print("3 > 2")



print("--------------------------------------------------- ÚKOL - KALKULAČKA")

"""

operator = input("Zadejte operátor: ")
x = input("Zadejte čislo X: ")
y = input("Zadejte čislo Y: ")
result = 0

if x.isdigit() and y.isdigit():
   if operator == "+":
      result = int(x) + int(y)
      print(result)
   elif operator == "-":
      result = int(x) - int(y)
      print(result)
   elif operator == "/":
      result = int(x) / int(y)
      print(result)
   elif operator == "*":
      result = int(x) * int(y)
      print(result)
   else:
      print("nezadal jsi operátor (+, -, /, *)")
   
   if result is not None:
      print(f"{x} {operator} {y} = {result}")
else:
   print("Nazadal jsi čísla pro x a y.")

"""

print("--------------------------------------------------- PODMÁNKOVÝ STROM NA JEDNOM ŘÁDKU")


jmeno = "Marek"

print("Ahoj, Marku!") if jmeno == "Marek" else print("Ahoj, vsem!")


print("--------------------------------------------------- PRÁCE SE SEZNAMEM ")

cities = ["Londýn", "Praha", "Berlín", "Brno"]

print(cities)

cities.append("Karlovy Vary")
print("cities + KV: ", cities)

#cities.clear()

print("count: ", cities.count("Brno"))   #kopočet, kolikrát se tohle objevuje v seznamu

print("index", cities.index("Brno"))

cities.insert(1, "Praha - město")
print("insert: ", cities)

cities.pop(3)      # položka na 3. pozici se smazala
print("pop: ", cities)

cities.remove("Brno")
print("remove: ", cities)

cities.reverse()
print("reverse: ", cities)

cities.sort()
print("sort - podle abecedy: ", cities)



