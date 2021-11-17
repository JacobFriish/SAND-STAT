import numpy as np
from numpy import cov
from matplotlib import pyplot as plt
import pandas as pd
import tabulate as tb
import statistics
from scipy.stats import kurtosis, skew, describe
from scipy.stats import pearsonr
import statsmodels.api as sm

# Tema for grafer.
plt.style.use("seaborn")

# Opsæt grid til grafer
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

data = pd.read_csv("data uge 46.csv")
n = len(data)
genstande = data['genstande']
bolig = data['bolig']

print("Opgave 4.1")

# Det er ikke lykkes at få de tre kolonner ind i samme tabel
gens_freq = data['genstande'].value_counts().sort_index()
gens_perc = gens_freq / sum(gens_freq) * 100
gens_cum = np.cumsum(gens_perc)
table = [gens_freq, gens_perc, gens_cum]
print(table)

data = pd.read_csv("data uge 46.csv")
gens_freq = data['bolig'].value_counts().sort_index()
gens_perc = gens_freq / sum(gens_freq) * 100
gens_cum = np.cumsum(gens_perc)
table = [gens_freq, gens_perc, gens_cum]
print(table)

print("\n")
print("Hvor mange drikker mere end 7 genstande om ugen?")

# Antal der drikker mere end eller lig 7 genstande om ugen
gens_over_syv = sum(i >= 7 for i in genstande)
print(gens_over_syv)

# Andelen af alle respondenter [bemærk, n er tidligere defineret som len(data)]
gens_over_syv_perc = gens_over_syv / n
print(gens_over_syv_perc)

print("\n")
print("Opgave 4.2")
print(describe(data['genstande']))

print("\n")
print("Opgave 4.3")
# Sætter antallet af kolonner og bredden i outputtet
pd.set_option('display.max_columns', 9)
pd.set_option('display.width', 1000)
print(data.groupby(['bolig'])['genstande'].describe())

print("\n")
print("Opgave 4.4")


