#Nome: Fabio Monaco
#Partner: Jason Mezzadri

import random

# Funzione per generare il numero iniziale di armate per ogni giocatore
def armate_iniziali():
    return random.randint(5, 8)

# Funzione per lanciare i dadi
def lancia_dadi():
    dadi = [random.randint(1, 6) for _ in range(3)]
    return dadi

# Funzione per eseguire un turno di combattimento
def combattimento(attaccante, difensore):
    # Lancia i dadi per entrambi i giocatori
    dadi_attacco = lancia_dadi()
    dadi_difesa = lancia_dadi()
    
    print(f"Dadi attacco: {dadi_attacco}")
    print(f"Dadi difesa: {dadi_difesa}")
    
    # Confronta i dadi
    armate_perse_attaccante = 0
    armate_perse_difensore = 0
    
    for i in range(3):
        if dadi_attacco[i] > dadi_difesa[i]:
            armate_perse_difensore += 1
        else:
            armate_perse_attaccante += 1
    
    # Aggiorna le armate
    attaccante -= armate_perse_attaccante
    difensore -= armate_perse_difensore
    
    return attaccante, difensore, armate_perse_attaccante, armate_perse_difensore

# Funzione principale per il combattimento
def gioca():
    # Inizializza le armate per entrambi i giocatori
    attaccante = armate_iniziali()
    difensore = armate_iniziali()
    
    turno = 1
    while attaccante > 0 and difensore > 0:
        print(f"Turno {turno}")
        print(f"Armate attaccante: {attaccante}, Armate difensore: {difensore}")
        
        # Simula il combattimento per il turno
        attaccante, difensore, armate_attaccante, armate_difensore = combattimento(attaccante, difensore)
        
        print(f"Attaccante ha perso {armate_attaccante} armate.")
        print(f"Difensore ha perso {armate_difensore} armate.")
        
        turno += 1
    
    # Determina il vincitore
    if attaccante > 0:
        print("\nL'attaccante ha vinto!")
    else:
        print("\nIl difensore ha vinto!")

# Avvia il gioco
if __name__ == "__main__":
    gioca()
