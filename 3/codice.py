import random

# Simula una singola partita
def simula_partita():
    pos = [0]*13        # pos[k] = riga attuale colonna k (ignoriamo pos[0])
    mosse = 0
    while True:
        mosse += 1
        # Lancia due dadi
        s = random.randint(1,6) + random.randint(1,6)
        if 1 <= s <= 12:
            pos[s] += 1  # la pedina in colonna s avanza
        # Controlla se questa colonna ha raggiunto la riga 19 (19 avanzamenti)
        if pos[s] >= 19:
            return s, mosse  # ritorna colonna vincente e numero di mosse

# Esempio: 10000 simulazioni per stimare P(colonna k vince) e distribuzione durate
simulazioni = 100000
win_count = [0]*13
durate = []
for _ in range(simulazioni):
    vincitore, N = simula_partita()
    win_count[vincitore] += 1
    durate.append(N)

# Calcola probabilità di vittoria per colonna k
prob_vittoria = [win_count[k]/simulazioni for k in range(13)]

# Calcola P(T=N) per N fino a 200 (conteggio frequenze)
freq_T = {}
for N in durate:
    if N <= 200:
        freq_T[N] = freq_T.get(N,0) + 1
prob_T = {N: freq_T.get(N, 0)/simulazioni for N in range(1, 201)}

# Esempio di risultati stampati (troncati)
print("Prob vittoria colonne k=1..12:\n", prob_vittoria[1:13])
print("Durata media:", sum(durate)/len(durate))
