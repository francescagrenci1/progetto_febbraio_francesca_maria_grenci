# VERIFICA DI UN ENCODING FAME
## Descrizione generale
In chemioinformartica, con "encoding" si intende la trascrizione di molecole sottoforma di stringa, al pari di quanto accade con le formule molecolari. 
In particolare, in questo progetto viene utilizzato un tipo di encoding detto "FAME", che segue delle regole di implementazione ben precise.
Il progetto consiste nello scrivere una funzione che verifichi la validità dell'encoding FAME di una determinata molecola data, analizzando sia la sua correttezza sintattica sia quella relativa alla valenza dei singoli atomi e legami, escludendo la presenza di legami aromatici.

### Regole dell'encoding FAME
Per la realizzazione di questo progetto, sono state seguite le seguenti regole di encoding FAME:
- presenza di atomi e legami: all'interno dell'encoding, gli atomi vengono rappresentati con caratteri standard MAIUSCOLI e gli unici presenti sono C, H, F, S, O, N, combinati in modi diversi. Gli atomi che formano un legame si trovano uno di seguito all’altro e sono inframezzati da simboli che corrispondono a legami covalenti: singoli (-), doppi (=) o tripli (#);
- valenza: ad ogni atomo, così come ad ogni legame, è associata una specifica valenza: C:4, F:1, S=2, N:3, H:1, O:2, "-" (legame singolo): 1, "="(legame doppio): 2, "#": 3 (legame triplo).
I singoli legami sono sempre validi per difetto: ciò significa che ogni atomo possiede legami con valenza minore o uguale alla propria;
- ramificazioni: sono sottostringe dell'encoding che iniziano con il simbolo "^" (che segue l'atomo da cui incipia la ramificazione), terminano con "&" e sono caratterizzate da almeno un legame. Se un atomo possiede ramificazioni, queste lo seguono immediatamente nella stringa. Inoltre, gli atomi all’interno della ramificazione non possiedono né legami tra loro né legami con altri atomi.

## Struttura del codice:
Il progetto prevede l'utilizzo di quattro funzioni, di cui due principali:
1. `verifica_sintassi_fame`: verifica la correttezza sintattica delle stringe FAME, seguendo le regole dell'encoding;
2. `verifica_valenza`: questa è la funzione principale del codice, la quale calcola la valenza dell'intera stringa FAME e viene eseguita solo se sintassi dell'encoding risulta corretta. Essa richiama al suo interno la funzione `trova_ramificazione_prox` per verificare la presenza di una ramificazione e, nel caso in cui la trovi, ne calcola la valenza tramite un'ulteriore funzione definita `calcolo_valenza_ramificazione`.
