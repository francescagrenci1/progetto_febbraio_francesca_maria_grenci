legami= "-=#"
atomi = "CNOHFS"
delimitatori_ramificazione = "^&"
valenza_atomi = {"C": 4, "N": 3, "O": 2, "H": 1, "F": 1, "S": 2 }
valenza_legami = {"-": 1, "=": 2, "#": 3}

def verifica_valenza(molecola):
    k = 0
    while k < len(molecola):
        print(f"Calcolo della valenza di {molecola[k]}")
        if k==0:
            ramificazione = molecola[k+1:len(molecola)]
            lunghezza_ramificazione, calcolo_valenza_ramificazione = calcola_valenza_legami_ramificazione(ramificazione)
            if lunghezza_ramificazione == 0:
                valenza = valenza_legami[molecola[k+1]]
                # print(valenza)
            else:
                print(f"Ramificazione trovata: {ramificazione[0:lunghezza_ramificazione+2]}, lunghezza  {lunghezza_ramificazione}")
                if not calcola_valenza_atomi_ramificazione(ramificazione[0:lunghezza_ramificazione+2]):
                    print(f"La ramificazione {ramificazione} non è valida")
                    return False
                else:
                    valenza = calcolo_valenza_ramificazione
                    spostamento = lunghezza_ramificazione + 3
                    if k + spostamento < len(molecola):
                        valenza = valenza + valenza_legami[molecola[k+spostamento]]
        elif k == len(molecola)-1:
            valenza = valenza_legami[molecola[k-1]]
            print(f"La valenza di {molecola[k]} è {valenza}")
        else:
            ramificazione = molecola[k + 1:len(molecola)]
            lunghezza_ramificazione, calcolo_valenza_ramificazione = calcola_valenza_legami_ramificazione(ramificazione)
            if lunghezza_ramificazione == 0:
                valenza = valenza_legami[molecola[k-1]] + valenza_legami[molecola[k+1]]
            else:
                print(f"Ramificazione trovata: {ramificazione[0:lunghezza_ramificazione+2]}, lunghezza  {lunghezza_ramificazione}")
                if not calcola_valenza_atomi_ramificazione(ramificazione[0:lunghezza_ramificazione+2]):
                    print(f"La ramificazione {ramificazione} non è valida")
                    return False
                else:
                    valenza = valenza_legami[molecola[k-1]] + calcolo_valenza_ramificazione
                    spostamento = lunghezza_ramificazione + 3
                    if k + spostamento < len(molecola):
                        valenza = valenza + valenza_legami[molecola[k+spostamento]]
        if valenza == valenza_atomi[molecola[k]]:
            print(f"La valenza di {molecola[k]} è corretta e vale {valenza}")
        else:
            print(f"La valenza di {molecola[k]} non è corretta e vale {valenza}")
            return False
        if lunghezza_ramificazione == 0:
            k += 2
        else:
            if lunghezza_ramificazione > 0:
                k = k + spostamento + 1
    return True

def calcola_valenza_legami_ramificazione(substr):
    if substr[0] == "^":
        k = 0
        valenza = 0
        terminatore_trovato = False
        while k < len(substr) and not terminatore_trovato:
            if substr[k] == "&":
                terminatore_trovato = True
            else:
                if substr[k] in valenza_legami:
                    valenza = valenza_legami[substr[k]] + valenza
                k += 1
        return k - 1, valenza
    else:
        print("ramificazione non trovata")
        return 0, 0

def calcola_valenza_atomi_ramificazione(ramificazione):
    k = 2
    valenza = 0
    verifica_valenza_atomo = True
    while k < len(ramificazione):
        valenza = valenza_legami[ramificazione[k - 1]]
        if valenza == valenza_atomi[ramificazione[k]]:
            print(f"La valenza di {ramificazione[k]} è corretta e vale {valenza}")
        else:
            print(f"La valenza di {ramificazione[k]} non è corretta")
            verifica_valenza_atomo = False
        k +=2
    return verifica_valenza_atomo
