#1. Calcola la somma degli elementi apparteneni alla cornice più esterna di una matrice di interi
print("Esercizio 1:")

import random

def genera_matrice():
    matrice = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    return matrice

def somma_cornice(matrice):
    somma = 0
    
    somma += sum(matrice[0]) 
    somma += sum(matrice[2])
    
    somma += matrice[1][0]
    somma += matrice[1][2]
    return somma
    
def main():
    matrice = genera_matrice() 
    for riga in matrice:
        print(riga)
        
    somma = somma_cornice(matrice)
    print(f"Somma della cornice della matrice: {somma}")

if __name__ == "__main__":
    main()
    print("\n")

#2. Calcola la somma della prima diagonale e verifica che sia uguale alla seconda diagonale
print("Esercizio 2:")

def genera_matrice():
    matrice = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    return matrice

def somma_diagonali(matrice):
    somma1 = 0
    somma2 = 0
    
    #somma prima diagonale
    somma1 += matrice[0][0]
    somma1 += matrice[1][1]
    somma1 += matrice[2][2]
    
    #somma seconda diagonale
    somma2 += matrice[0][2]
    somma2 += matrice[1][1]
    somma2 += matrice[2][0]
    
    return somma1, somma2
  
def main():
    matrice = genera_matrice()  
    for riga in matrice:
        print(riga)
        
    somma1, somma2 = somma_diagonali(matrice)
    print(f"La somma della prima diagonale è: {somma1}")
    print(f"La somma della seconda diagonale è: {somma2}")
    
    if somma1 == somma2:
        print("La somma delle due diagonali è uguale!")
    else:
        print("La somma delle due diagonali NON è uguale!!")
        

if __name__ == "__main__":
    main()
    print("\n")
