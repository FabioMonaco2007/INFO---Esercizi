import random

def crea_giocatori():
    giocatori = {}
    nome1 = input("Scrivi il tuo nome: ")
    giocatori[nome1] = {'Simbolo': 'X', 'Punteggio': 0}
    print("---I DUE NOMI NON DEVONO ESSERE UGUALI!---")
    nome2 = input("Scrivi il tuo nome: ")
    
    if nome1 == nome2:
        print("I nomi non devono essere uguali! Riprova.")
        return None 
    
    giocatori[nome2] = {'Simbolo': 'O', 'Punteggio': 0}
    return giocatori
    
def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""

    matrice = []
    for i in range(3):
        tabellone = []
        matrice.append(tabellone)
        for _ in range(3):
            matrice[i].append("")
    return matrice


def mostra_tabellone(tabellone: list[list[str]]) -> None:
    """Stampa la griglia di gioco in modo leggibile."""
    pass

def gioca_turno(tabellone: list[list[str]], giocatore: str) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    pass

def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    """Verifica se c'è un vincitore e restituisce True in caso affermativo."""
    pass

def aggiorna_punteggio(giocatori: dict, vincitore: str) -> None:
    """Aggiorna il punteggio del giocatore vincente."""
    pass

def partita(giocatori: dict) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    pass

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    giocatori = crea_giocatori()
    print(giocatori)
    matrice = inizializza_tabellone()
    for i in range(3):
        print(matrice[i])
    
main()