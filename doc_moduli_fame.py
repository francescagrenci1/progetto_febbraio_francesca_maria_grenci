# Definizione dei caratteri validi per legami, atomi e delimitatori di ramificazione:
legami: str = "-=#"
atomi: str = "CNOHFS"
delimitatori_ramificazione: str = "^&"
# Definizione di dizionari che contengono gli atomi e i legami validi associati alle proprie valenze:
valenza_atomi: dict = {"C": 4, "N": 3, "O": 2, "H": 1, "F": 1, "S": 2 }
valenza_legami: dict = {"-": 1, "=": 2, "#": 3}
categorie: dict = {"H":"atomo", "O":"atomo", "C":"atomo", "F": "atomo", "N":"atomo", "S":"atomo",
                   "-":"legame", "=":"legame", "#":"legame", "^":"inizio_ram", "&": "fine_ram"}

def verifica_sintassi_fame(molecola: str) -> bool:
    '''Funzione che verifica la correttezza sintattica della stringa FAME.
        - Argomento: molecola (str): stringa FAME
        - valore di ritorno: (bool). Restituisce True se la sintassi è corretta, False se non lo è
       La molecola sarà valida se:
       - stato = 1: perchè ho terminato con un atomo e la sequenza è composta da più caratteri che rispettano la sintassi FAME
         (la stringa composta da un solo atomo non è una molecola)
       - stato = 6: perchè ho terminato con una ramificazione e la sequenza rispetta la sintassi FAME
       In tutti gli altri stati, l'encoding FAME non è valido'''

    stato = 0
    for c in molecola:
        if c not in categorie:
            print(f"Il carattere {c} non è consentito nell'encoding FAME")
            return False
        categoria_elemento = categorie[c]
        print(f"input {c} - categoria elemento {categoria_elemento}")
        if stato == 0:  # stato di partenza
            if categoria_elemento == "atomo":
                stato = 1
            else:
                return False
        elif stato == 1:  # atomo
            if categoria_elemento == "legame":
                stato = 2
            elif categoria_elemento == "inizio_ram":
                stato = 3
            else:
                print(f"Errore. Il carattere {c} non è consentito: dopo un atomo ci possono essere solo legami o inizio ramificazioni")
                return False
        elif stato == 2:  # legame
            if categoria_elemento == "atomo":
                stato = 1
            else:
                print(f"Errore. Il carattere {c} non è consentito: ci possono essere solo atomi dopo un legame")
                return False
        elif stato == 3:  # ingresso dentro la ramificazione
            if categoria_elemento == "legame":
                stato = 4
            else:
                print(f"Errore. Il carattere {c} non è consentito: ci possono essere solo legami dopo l'inizio di una ramificazione")
                return False
        elif stato == 4:  # legame dentro la ramificazione
            if categoria_elemento == "atomo":
                stato = 5
            else:
                print(f"Errore. Il carattere {c} non è consentito: dentro la ramificazione, ci possono essere solo atomi dopo un legame")
                return False
        elif stato == 5:  # atomo dentro la ramificazione
            if categoria_elemento == "legame":
                stato = 4
            elif categoria_elemento == "fine_ram":
                stato = 6
            else:
                print(f"Errore. Il carattere {c} non è consentito: dentro la ramificazione, dopo un atomo, ci possono essere solo legami o fine ramificazione")
                return False
        elif stato == 6:  # uscita dalla ramificazione
            if categoria_elemento == "legame":
                stato = 2
            else:
                print(f"Errore. Il carattere {c} non è consentito: dopo una ramificazione possono esserci solo legami")
                return False
    # al termine della scansione della molecola, verifico lo stato
    if (stato == 1 and len(molecola) != 1) or stato == 6:
        return True
    else:
        return False

def calcola_valenza_legami_ramificazione(substr: str) -> tuple[int, int]:
    '''Funzione che cerca la ramificazione di prossimità all'atomo corrente nella stringa.
        - Argomento: substr (str): sottostringa successiva all'atomo corrente, che inizia con "^" e termina con "&"
        - valore di ritorno (bool): tuple[int, int]:
          -> se ci sono ramificazioni, restituisce, rispettivamente, la lunghezza della ramificazione,
             ossia il numero di caratteri compresi tra "^" e "&", e la valenza dei legami associati all'atomo a sinistra;
          -> se non ci sono ramificazioni restituisce 0,0 '''
    if substr[0] == "^":
        # se il primo carattere della sottostringa coincide con "^" ho trovato l'inizio della ramificazione
        k = 0
        valenza = 0
        terminatore_trovato = False
        # l'indice k scorre finché non trova il terminatore "&"
        while k < len(substr) and not terminatore_trovato:
            if substr[k] == "&":
                terminatore_trovato = True
            else:
                # ogni volta che viene trovato un legame, la sua valenza viene sommata a quella totale di tutti i legami trovati
                if substr[k] in valenza_legami:
                    valenza = valenza_legami[substr[k]] + valenza
                k += 1
        # restituisce la lunghezza della ramificazione (k-1 per escludere il terminatore dal conteggio dei suoi caratteri) e la valenza trovata
        return k - 1, valenza
    else:
        # se nella stringa non viene trovato un iniziatore di ramificazione "^", la ramificazione risulta non presente
        print("ramificazione non trovata")
        return 0, 0

def calcola_valenza_atomi_ramificazione(ramificazione: str) -> bool:
    '''Funzione invocata per calcolare la valenza di ogni atomo contenuto nella ramificazione,
       verificando il rispetto della valenza massima.
       - Argomento: ramificazione (str): ramificazione (sottostringa) trovata da "calcola_valenza_legami_ramificazione";
       - Valore di ritorno: verifica_valenza (bool): restituisce True se tutti gli atomi interni hanno valenza valida.'''

    k = 2 # si parte dall'indice 2 (dopo "^" e il primo legame) perché esso corrisponde al primo atomo
    valenza = 0
    verifica_valenza_atomo = True
    while k < len(ramificazione):
        # verifica solo il legame a sinistra perché gli atomi della ramificazione non sono collegati tra loro
        valenza = valenza_legami[ramificazione[k - 1]]
        # condizione di validità della valenza dell'atomo corrente:
        if valenza == valenza_atomi[ramificazione[k]]:
            print(f"La valenza di {ramificazione[k]} è corretta e vale {valenza}")
        else:
            print(f"La valenza di {ramificazione[k]} non è corretta")
            verifica_valenza_atomo = False
        k +=2 #il cursore avanza di due posizioni perché si sposta da un atomo a quello successivo
    return verifica_valenza_atomo

def verifica_valenza(molecola: str) -> bool:
    '''Funzione principale che verifica se la valenza dell'intera molecola è corretta o meno:
       - Argomento: molecola (str): stringa FAME completa
       - Valori di ritorno (bool): restituisce True se la valenza della molecola è valida, False se non lo è'''

    k = 0
    # scorre su tutta la lunghezza della molecola
    while k < len(molecola):
        print(f"Calcolo della valenza di {molecola[k]}")
        # inizio della molecola (calcola la valenza solo a destra) ----------
        if k==0:
            # sottostringa della possibile ramificazione, a partire dal carattere successivo al primo atomo fino alla fine della molecola
            ramificazione = molecola[k+1:len(molecola)]
            #chiamata della funzione per cercare la ramificazione e calcolare la valenza dei legami al suo interno
            lunghezza_ramificazione, calcolo_valenza_ramificazione = calcola_valenza_legami_ramificazione(ramificazione)
            if lunghezza_ramificazione == 0:
                # il valore della valenza è solo quello del legame a destra
                valenza = valenza_legami[molecola[k+1]]
                print(valenza)
            else:
                # ramificazione trovata
                print(f"Ramificazione trovata: {ramificazione[0:lunghezza_ramificazione+2]}, lunghezza  {lunghezza_ramificazione}")
                # chiamata della funzione per calcolare la valenza di ogni atomo della ramificazione
                if not calcola_valenza_atomi_ramificazione(ramificazione[0:lunghezza_ramificazione+2]):
                    # la valenza degli atomi della ramificazione non viene rispettata
                    print(f"La ramificazione {ramificazione} non è valida")
                    return False
                else:
                    # la valenza degli atomi della ramificazione è rispettata
                    # calcola la valenza dell'atomo corrente solo a destra
                    valenza = calcolo_valenza_ramificazione
                    # si sposta oltre la ramificazione per verificare la presenza di ulteriori legami
                    spostamento = lunghezza_ramificazione + 3 # (lunghezza ramificazione + terminatori ramificazione + una posizione)
                    if k + spostamento < len(molecola):
                        # si aggiunge la valenza del legame successivo alla ramificazione
                        valenza = valenza + valenza_legami[molecola[k+spostamento]]
                    # print(f"La valenza di {molecola[k]} è {valenza}")
        # fine della molecola (calcola la valenza solo a sinistra) -----------
        elif k == len(molecola)-1:
            valenza = valenza_legami[molecola[k-1]]
            print(f"La valenza di {molecola[k]} è {valenza}")
        # interno della molecola (calcola la valenza sia a sinistra che a destra) -----------
        else:
            # come nel caso di inizio molecola (k=0) si cerca la ramificazione a destra e si calcola la valenza dei legami
            ramificazione = molecola[k + 1:len(molecola)]
            lunghezza_ramificazione, calcolo_valenza_ramificazione = calcola_valenza_legami_ramificazione(ramificazione)
            if lunghezza_ramificazione == 0:
                # se non c'è nessuna ramificazione, la valenza dell'atomo è data dalla somma della valenza dei legami a sinistra e a destra
                valenza = valenza_legami[molecola[k-1]] + valenza_legami[molecola[k+1]]
                # print(f"La valenza di {molecola[k]} è {valenza}")
            else:
                # ramificazione trovata
                print(f"Ramificazione trovata: {ramificazione[0:lunghezza_ramificazione+2]}, lunghezza  {lunghezza_ramificazione}")
                # chiamata della funzione per calcolare la valenza di ogni atomo della ramificazione
                if not calcola_valenza_atomi_ramificazione(ramificazione[0:lunghezza_ramificazione+2]):
                    # la valenza degli atomi della ramificazione non viene rispettata
                    print(f"La ramificazione {ramificazione} non è valida")
                    return False
                else:
                    # la valenza degli atomi della ramificazione è rispettata:
                    # calcola la valenza dell'atomo corrente sommando la valenza dei legami di sinistra e quella dei legami della ramificazione
                    valenza = valenza_legami[molecola[k-1]] + calcolo_valenza_ramificazione
                    spostamento = lunghezza_ramificazione + 3
                    if k + spostamento < len(molecola):
                        # si aggiunge la valenza del legame successivo alla ramificazione
                        valenza = valenza + valenza_legami[molecola[k+spostamento]]
                    # print(f"La valenza di {molecola[k]} è {valenza}")
        # verifica se la valenza calcolata è valida
        if valenza == valenza_atomi[molecola[k]]:
            print(f"La valenza di {molecola[k]} è corretta e vale {valenza}")
        else:
            print(f"La valenza di {molecola[k]} non è corretta e vale {valenza}")
            return False
        # si posiziona sull'atomo successivo e calcola il movimento in base alla presenza o meno della ramificazione
        if lunghezza_ramificazione == 0:
            k += 2 # avanza all'atomo successivo (due posizioni) perché non ho trovato nessuna ramificazione
        else:
            if lunghezza_ramificazione > 0:
                k = k + spostamento + 1 # la ramificazione è presente, quindi avanza all'atomo successivo dopo la ramificazione
    return True




