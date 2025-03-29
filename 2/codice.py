import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Numero totale di elettori (N + M = 10^6)
total = int(1e6)

# Valori di M (numero di sostenitori di A) da 0 a 5000 con passo 10
M_values = np.arange(0, 5001, 10)

# Lista per memorizzare le probabilità calcolate
probabilities = []

# Iterazione sui valori di M
for M in M_values:
    # Calcolo di N (numero di elettori indecisi)
    N = total - M
    
    # Calcolo della soglia (numero minimo di voti per vincere)
    threshold = (N - M) // 2 + 1  # t_start
    
    # Parametri della distribuzione binomiale approssimata con una normale
    mu = N * 0.5  # Media
    sigma = np.sqrt(N * 0.25)  # Deviazione standard
    
    # Calcolo dello z-score con correzione di continuità
    z = (threshold - 0.5 - mu) / sigma
    
    # Calcolo della probabilità usando la distribuzione normale cumulativa
    prob = 1 - norm.cdf(z)
    probabilities.append(prob)
    
    # Stampa del valore di M e della probabilità calcolata
    print(f"M = {M}, Probabilità di vittoria di A = {prob:.6f}")

# Generazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(M_values, probabilities, 'b-', label='Probabilità di vittoria di A')
plt.xlabel('M (Numero di sostenitori di A)')
plt.ylabel('Probabilità di vittoria di A')
plt.title('Probabilità di vittoria di A al variare di M')
plt.grid(True)
plt.legend()
plt.savefig('probability_plot.pdf', format='pdf')
plt.show()