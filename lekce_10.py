data_1 = {
    'order': {
        'id': '1234', 'type': 'order.created', 
        'channel': 'eshop CZ'
    }
}

data_2 = {
    'order': {
        'id': '1234', 'type': 'order.created', 
        'channel': ''
    }
}

data_3 = {
    'order': {
        'id': '1234', 'type': 'order.created'
    }
}


def vrat_zemi_objednavky(data:dict) -> str:
    kod_zeme = None
    try:
        kod_zeme = data["order"]["channel"].split()[-1]
        return kod_zeme
    except KeyError:
        print("KeyError - WARNING: Chybí klíč channel!")
    except IndexError:
        print("IndexError - WARNING: Prázdá hodnota pro klíč channel!")
    finally:  # spustí se za každé příležitosti - vždy
        print("Ukončuji funkci.")





print(vrat_zemi_objednavky(data_1))
print()
print(vrat_zemi_objednavky(data_2))
print()
print(vrat_zemi_objednavky(data_3))



