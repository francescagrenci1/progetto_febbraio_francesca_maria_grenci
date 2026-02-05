legami= "-=#"
atomi = "CNOHFS"
delimitatori_ramificazione = "^&"
valenza_atomi = {"C": 4, "N": 3, "O": 2, "H": 1, "F": 1, "S": 2 }
valenza_legami = {"-": 1, "=": 2, "#": 3}
categorie = {"H":"atomo", "O":"atomo", "C":"atomo", "F": "atomo", "N":"atomo", "S":"atomo",
                   "-":"legame", "=":"legame", "#":"legame", "^":"inizio_ram", "&": "fine_ram"}

def verifica_sintassi_fame(molecola):
    stato = 0
    for c in molecola:
        if c not in categorie:
            print(f"Il carattere {c} non è consentito nell'encoding FAME")
            return False
        categoria_elemento = categorie[c]
        print(f"input {c} - categoria elemento {categoria_elemento}")
        if stato == 0:
            if categoria_elemento == "atomo":
                stato = 1
            else:
                return False
        elif stato == 1:
            if categoria_elemento == "legame":
                stato = 2
            elif categoria_elemento == "inizio_ram":
                stato = 3
            else:
                print(f"Errore. Il carattere {c} non è consentito dopo un atomo: solo legami o inizio ramificazioni")
                return False
        elif stato == 2:
            if categoria_elemento == "atomo":
                stato = 1
            else:
                print(f"Errore. Il carattere {c} non è consentito: solo atomi dopo un legame")
                return False
        elif stato == 3:
            if categoria_elemento == "legame":
                stato = 4
            else:
                print(f"Errore. Il carattere {c} non è consentito: solo legami dopo l'inizio di una ramificazione")
                return False
        elif stato == 4:
            if categoria_elemento == "atomo":
                stato = 5
            else:
                print(f"Errore. Il carattere {c} non è consentito: dentro la ramificazione, solo atomi dopo un legame")
                return False
        elif stato == 5:
            if categoria_elemento == "legame":
                stato = 4
            elif categoria_elemento == "fine_ram":
                stato = 6
            else:
                print(
                    f"Errore. Il carattere {c} non è consentito: dentro la ramificazione, dopo un atomo, solo legame o fine ramificazione")
                return False
        elif stato == 6:
            if categoria_elemento == "legame":
                stato = 2
            else:
                print(f"Errore. Il carattere {c} non è consentito: dopo una ramificazione possono esserci solo legami")
                return False
    if (stato == 1 and len(molecola) != 1) or stato == 6:
        return True
    else:
        return False