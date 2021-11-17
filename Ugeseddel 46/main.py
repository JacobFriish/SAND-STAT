import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics
from scipy.stats import kurtosis, skew, describe


data = pd.read_csv("data uge 46.csv")

print("\n")
print("Opgave 3.1")
# for at se data anvend:
# print(data)
print("Data er diskrete.")

print("\n")
print("Opgave 3.2")

# Vælg hvilke kolonner der skal plottes
studietimer = data['studietimer']
ids = data['id']
# Vælg hvordan data skal inddeles i bins

# Settings til histogrammet
plt.title('Histogram, karakterer og studietimer')
plt.xlabel('Studietimer')
plt.ylabel('Antal')
plt.tight_layout()

# Plot median-linje
median_studietimer = statistics.median(studietimer)
plt.axvline(median_studietimer, color='red', label='Median')

# Plot selve grafen
plt.hist(studietimer, histtype='bar', edgecolor='black')
plt.show()



