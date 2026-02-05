legami = "-=#"
atomi = "CNOHFS"
delimitatori_ramificazione = "^&"
valenza_atomi = {"C": 4, "N": 3, "O": 2, "H": 1, "F": 1, "S": 2 }
valenza_legami = {"-": 1, "=": 2, "#": 3}

acetilene = "H-C#C-H"
anidride_carbonica = "C^=O=O&"
acqua_1 = "O^-H-H&"
acqua_2 = "O^-H&-H"
propano = "C^-H-H-H&-C^-H-H&-C^-H-H-H&"
colesterolo_vuoto = ""
metano_errato = "C^-H-H-H-H?"
triossido_di_zolfo = "S^=O=O=O&"
gruppo_amminico = "N^-H-H&"
acido_ipofluoroso = "H-F-O"
acido_ipofluoroso_errato = "H-F=O&"
monossido_di_azoto = "N=O"
monossido_di_azoto_errato = "N-O"

from verifica_sintassi_fame import verifica_sintassi_fame
from verifica_valenza import verifica_valenza

if verifica_sintassi_fame(acetilene):
    verifica_valenza(acetilene)
else:
    print(f"la molecola non è sintatticamente corretta")


