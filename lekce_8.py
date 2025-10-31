print("---------------------------------------------------- KLÍČOVÉ PARAMETRY")

def vypocitej_hodnotu(koef_1, koef_2, koef_3):
    """
    Vypocitej hodnotu na zaklade tri zadanych koeficinetu.
    """
    return (1 / koef_1) * (koef_2 ** koef_3)

print(vypocitej_hodnotu(koef_1=0.5, koef_2=3, koef_3=2)) # tohle je ZÁPIS POMOCÍ KLÍČOVÝCH ARGUMENTŮ --> takhle je to o dost přehlednější, než když napíšu jen (0.5, 3, 2)
print(vypocitej_hodnotu(0.5, 3, 2))    # tohle je POZIČNÍ ZÁPIS


print("---------------------------------------------------- DEFAULTNÍ PARAMETRY")

def vytvor_pozdrav(jmeno = "Matous"):  # dám si tady defoultní hodnotu
    print("Ahoj,", jmeno)

vytvor_pozdrav()
vytvor_pozdrav("Lukas")   # pokud ale zavolám s něčím jiným, bude se pracovat s tímto "Lukas"¨

print("-------")

def funkce(l: list = []):   #nevytvoří se pro každé volání nový list, ale existuje jen 1 list - ten postupně měním s voláním každé funkce --> list, dict atd. by neměly být defaultní parametry
    l.append(2)
    print(l)

funkce()
funkce()

print("-------")

def funkce2(
        l: list | None = None
    ) -> str:
    if l is None:                   # testuju, jestli je list prázdný
        l = []
    l.append(3)
    print(l)

funkce2()
funkce2()




print("---------------------------------------------------- *ARGS")  # 1 parametr může přijímat více hodnot; vždy se vytvoří tuple


def vypocitej_prumer(*args):
    print(args, type(args))
    return sum(args) / len(args)

print(vypocitej_prumer(1, 2, 3, 4, 5))

print("Ahoj", "Petre")
print(min(1, 5, 2, 9))

print("-----")

def vypocitej_prumer(*args, stupen):            # pokud tam mám *, vše vpravo se už pak může zapsat pouze pomocí KLÍČOVÉHO zápisu
    return (sum(args) / len(args)) ** stupen

print(vypocitej_prumer(1, 2, 3, 4, 1, 2, 3, 10, stupen=20))

print("------------- ")

jiz_existujici_list = [1, 2, 3, 4, 5]

def vypocitej_prumer2(*args):          
    return (sum(args) / len(args)) ** 2


print(vypocitej_prumer2(jiz_existujici_list[0], jiz_existujici_list[1], jiz_existujici_list[2])) # vypisuju všechno po jednom
print(vypocitej_prumer2(*jiz_existujici_list))   # takhle si to ulehčím pomocí *


print("----------------")

def uloz_informace(*, jmeno: str, prijmeni: str = "", novy_parametr: str = "", telefon: str = "") -> dict:   #vše napravo od hvězdičky se může přidávat pouze pomocí KLÍČŮ
    return {"jmeno": jmeno, "prijmeni": prijmeni, "telefon": telefon}

uloz_informace(jmeno="Matous", prijmeni="Holinka", telefon="888888888")    # pokud je nahoře hvězdička, musí tady být KLÍČOVÉ pozice


print("---------------------------------------------------- **KWARGS")   #pokud má funkce pracovat s různým množstvím hodnot v párech klíč, hodnota.


def vytvor_slovnik(kwargs: dict) -> None:
    """
    Vypiš slovník, který obsahuje libovolné množství sbalených hodnot. 
    """
    print(type(kwargs))
    for klic, hodnota in kwargs.items():
        print(klic.upper(), hodnota, sep=":")

vytvor_slovnik(
    {
        "jmeno": "Matous", "prijmeni": "Holinka", "jakykoliv_klic": "libovolna hodnota"
    }
)


print("------------------------------------------------------ CVIČENÍ ")

def spoj_slova(*args: str):
    if len(args) == 0:
        return None
    return "-".join(args) 

print(spoj_slova("Hello", "world", "!"))

print(spoj_slova("pes", "běží", "rychle"))   # ➡ "pes-běží-rychle"
print(spoj_slova())                          # ➡ None
print(spoj_slova("Python", "je", "super"))   # ➡ "Python-je-super"



print("------------------------------------------------------ RÁMCE - cvičení ")




def preved_format_na_kapitalku(text: str) -> str:
    naformatovana_slova = [slovo.title() for slovo in text.split()]
    return " ".join(naformatovana_slova)        

def zobraz_text(zadany_text: str):
    print("Formátovaný text:", zadany_text)


zadany_string = "toto je ukázkový text"
naformatovana_zprava = preved_format_na_kapitalku(zadany_string)
zobraz_text(naformatovana_zprava)


print("--------------------------------------------------- CVIČENÍ NA KONCI LEKCE ")


zadany_text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com,
dapibus lacinia vulputate vitae, ullamcorper in justo.
vitae massa. Cras abc@gmail.com vel libero felis.
In augue elit, porttitor nec molestie quis, auctor
a quam. Quisque b2b@money.fr pretium dolor et tempor
luctus lacinia risus. Maecenas posuere leo sit amet
spam@info.cz. elit tincidunt maximus. Aliquam erat
volutpat. Donec eleifend felis at leo ullamcorper
fringilla est. Maecenas gravida turpis nec ultrices
aliquet.'''

def je_email(slovo):
    if "@" in slovo:
        return True
    else:
        return False


def uloz_emailove_adresy(text, kontrola):
    emailove_adresy = set()
    words_in_text = text.split()
    for word in words_in_text:
        ciste_slovo = word.strip(",.:;")
        if kontrola(ciste_slovo) is True:
            emailove_adresy.add(ciste_slovo)
            
    return emailove_adresy

vysledky = uloz_emailove_adresy(zadany_text, je_email)

print(f"Načtené emaily: {vysledky}")

print("Načtené emaily:", ", ".join(vysledky))
