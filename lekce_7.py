print("--------------------------------- FUNKCE V PYTHONU ")

a = 10
print(type(a))
print(id(a))

print(type(print))    # funkce jsou v pythonu taky objekty

print(type(enumerate))  # tohle není funkce, je to class
print()

for i, mesto in enumerate(("Praha", "Brno", "Ostrava")):
    print(i, mesto)

print()
print("Matouš", "Marek", "Lukáš", sep="\n")   # každé jmén ose vypíše na nový řádek

print()
ciselna_rada = [1, 2, 3, 4, "pět", 6]
#print(sum(ciselna_rada)) #hodí to type error, protože neumí počítat string

print("----------------------------------------------- IS INSTANCE ")
soucet_cisel = 0
for cislo in ciselna_rada:
    if isinstance(cislo, str):   #isinstance - kontroluje, jestli nějaký objekt patří k danému datovému typu
        continue    # pokud je str, tak to přeskočí a jde na další 
    soucet_cisel += cislo
print(soucet_cisel)

print()
print(isinstance(5, (int, float))) #jestli je 5 int nebo float
print()

soucet_cisel = 0
for cislo in ciselna_rada:
    if isinstance(cislo, (int, float)):
        soucet_cisel += cislo
print(soucet_cisel)

print("------------------------------------------- VYTVÁŘENÍ VLASTNÍCH FUNKCÍ ")

def secti_vsechny_cisla(sekvence):
    soucet_cisel = 0
    for cislo in sekvence:
        if isinstance(cislo, str): 
            continue
        soucet_cisel += cislo
    print(soucet_cisel)

secti_vsechny_cisla([1, 2, 3])
secti_vsechny_cisla([5, 6, 7, 3])

print()

def scitej_dve_hodnoty(cislo_1, cislo_2):            
    """
    Vraci soucet dvou hodnot uvnitr parametru.
    """                                              
    return cislo_1 + cislo_2

print(scitej_dve_hodnoty(3, 2))


print("----------------------------------------- CHOICES ")

from random import choices

print(choices([1, 2, 3], k=2))   #vybere 2 random čísla
print(choices(range(51), k=5))

print("------------------------------------------- ÚKOL ")

from random import choices

def vygeneruj_tuple(delka, max_hodnota):
    return tuple(choices(range(max_hodnota +1), k=delka))


print(
    vygeneruj_tuple(5, 50),
    vygeneruj_tuple(10, 100),
    vygeneruj_tuple(15, 150),
    sep="\n"
)



def ocistit_od_prazdnych(udaje):
    """
    Odstraní všechny hodnoty None z tuple a vrátí nový tuple bez těchto hodnot.
    """
    return tuple(hodnota for hodnota in udaje if hodnota is not None)

krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)

print(
    ocistit_od_prazdnych(krestni_jmena),
    ocistit_od_prazdnych(prijmeni),
    sep='\n'
)




print("----------------------------------------------------- ÚKOL NA KONCI LEKCE ")

"""
vstupni_text = "Ahoj všem, tady Engeto"
vysledek = ""

def zdvojnasob_znaky(vstupni_text):
    zdvojene = list()
    for x in range(len(vstupni_text)):
        zdvojene.append(2* vstupni_text[x])

    for y in range(len(zdvojene)):
        vysledek += zdvojene[y]
    
    print(f"Zdvojené znaky: {vysledek}")
zdvojnasob_znaky(vstupni_text)

"""



vstupni_text = "Ahoj všem, tady Engeto"

zdvojene = list()
def zdvojnasob_znaky(text):
    for pismeno in text:
        zdvojene.append(pismeno * 2)  
    vys = "".join(zdvojene)
    return vys

vysledek = zdvojnasob_znaky(vstupni_text)
print(f"Zdvojené znaky: {vysledek}")


