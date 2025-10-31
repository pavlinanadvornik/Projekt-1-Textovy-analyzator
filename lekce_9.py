
def tri_radky_prazdne():
    print()
    print()
    print()

muj_nacteny_txt_soubor = open('czech.txt', encoding='utf-8')

obsah_txt = muj_nacteny_txt_soubor.read()

muj_nacteny_viceradkovy_soubor = open("viceradkovy_soubor.txt", encoding="utf-8")
obsah_txt_list = muj_nacteny_viceradkovy_soubor.readlines()

print("OBSAH TXT: ", obsah_txt)
print("OBSAH TXT LIST: ", obsah_txt_list)

print("CLOSED: ", muj_nacteny_viceradkovy_soubor.closed)  # VRÁTÍ true/false
print()
muj_nacteny_viceradkovy_soubor.seek(0)    # vrátí kurzor na začátek textu

# muj_nacteny_viceradkovy_soubor.close()   #uzavře soubor
print("CLOSED: ", muj_nacteny_viceradkovy_soubor.closed)  # VRÁTÍ true/false

print("READ LINE: ", muj_nacteny_viceradkovy_soubor.readline())
print("READ LINE: ", muj_nacteny_viceradkovy_soubor.readline())


print("------------------------------------------------------------ FUNKCE NA ČTENÍ DOKUMENTU: ")

def precti_txt_soubor(jmeno_souboru: str,
                      mod: str = 'r') -> list:
    muj_nacteny_txt_soubor = open(jmeno_souboru,
                                  mode=mod)

    obsah_txt = muj_nacteny_txt_soubor.readlines()
    
    muj_nacteny_txt_soubor.close()
    
    return obsah_txt



print("------------------------------------------------------------  ")

muj_txt = open("viceradkovy_soubor_kopie.txt", mode="r", encoding="utf-8")
print(iter(muj_txt))        # vytvoří se iterátor - použít např. ve for cyklu
print()

for radek in muj_txt:
    print(radek, end="")



muj_druhy_txt_soubor = open(
    "muj_zapsany.txt",    # pokud již soubor existuje, všechen obsah se vymaže (v modu write); pokud takový soubor neexistuje, vytvoří se
    mode="w"        # write
)

# muj_druhy_txt_soubor.readlines()    # hodí error, protože v souboru nejde číst, pouze zapisovat

tri_radky_prazdne()

muj_string = "ahoj"
print(muj_druhy_txt_soubor.write(muj_string))

muj_druhy_txt_soubor.close()

tri_radky_prazdne()


muj_druhy_string = "Očekávám text na druhém řádku!"

muj_existujici_txt = open(
    "muj_zapsany.txt",
    mode="w"
)

print("------------------------------------------- ÚKOL ")

def zapis_zpravu_do_txt_souboru(zprava: str,
                                jmeno_souboru: str
                               ):
    # Vytvoříme spojení s daným argumentem a souborem ..
    muj_txt_soubor = open(jmeno_souboru,
                          mode='w',
                          encoding='UTF-8')
 
    # zapíšeme zprávu do souboru ..
    muj_txt_soubor.write(zprava)
 
    # uzavřeme spojení se souborem.
    muj_txt_soubor.close()

zapis_zpravu_do_txt_souboru(
    zprava= "Tohle je zpráva!",
    jmeno_souboru="ukazka.txt"
)

muj_soubor = open("muj_zapsany2.txt", mode="a", encoding="utf-8")   # a = apppend  - přidá se to na konec souboru
muj_soubor.write("První řádek")
muj_soubor.write("Druhý řádek")
muj_soubor.close()

muj_soubor = open("muj_zapsany2.txt", mode="r+", encoding="utf-8")   # r+ = můžu zároveň číst i psát

muj_soubor.tell()    # kurzor se dostane na první řádek
muj_soubor.write("Ještě jeden řádek!\n")
muj_soubor.write("Řádek #0! \n")
print("tell", muj_soubor.tell())


print("--------------------------------------- WITH - takhle je ideální pracovat se soubory ")

soubor = open("muj_zapsany.txt", mode="r")
soubor.__enter__
soubor.__exit__   #deinují, jestli je to KONTEXTOVÝ MANAŽER = můžeme to použít v zápisu s WITH


with open("muj_zapsany.txt", mode="r") as soubor_muj:         # díky téhle metodě se sám soubor otevře (__enter__) a zavře (__exit__)
    print(soubor_muj.readlines())
    print("uprostřed: ", soubor_muj.closed)   # test, jestli je soubor closed
print("na konci: ", soubor_muj.closed)


print("--------------------------------------- ÚKOL ")


zaznamy = """\
INFO 2023-07-26 10:30:22 Aplikace úspěšně spuštěna
INFO 2023-07-26 10:31:12 Uživatel přihlášen
WARN 2023-07-26 10:35:05 Nedostatek místa na disku
INFO 2023-07-26 10:36:17 Data úspěšně uložena
ERROR 2023-07-26 10:40:44 Připojení k databázi selhalo
WARN 2023-07-26 10:45:30 Možná chyba v konfiguraci
ERROR 2023-07-26 10:50:01 Nelze odeslat e-mail
INFO 2023-07-26 10:55:12 Aplikace úspěšně ukončena
"""

    
def precti_logy(jmeno_souboru: list[str]):
    with open(jmeno_souboru, mode="r") as soubor:
        return soubor.readlines()

def vyber_pouze_typy(obsah_txt: list[str]) -> tuple[str]:
    vysledne_typy = [
        zaznam.split()[0]
    ]
    for zaznam in obsah_txt:
        vysledne_typy.append()
    return tuple(vysledne_typy)



print("--------------------------------------- ÚKOL ")


def nacist_udaje(jmeno_souboru: str):
    zaznamy = []
    with open(jmeno_souboru, mode="r", encoding="utf-8") as soubor:
        for radek in soubor:
            jmeno, vek = print(radek.split(";"))
            vek = int(vek.strip())
            zaznamy.append((jmeno, vek))

def najdi_mladsi():
    pass


nacist_udaje("lidi.txt")








