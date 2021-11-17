import numpy as np
from numpy import cov
from matplotlib import pyplot as plt
import pandas as pd
import statistics
from scipy.stats import kurtosis, skew, describe
from scipy.stats import pearsonr
import statsmodels.api as sm

# Tema for grafer.
plt.style.use("seaborn")

# Opsæt grid til grafer
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

data = pd.read_csv("data uge 46.csv")

print("\n")
print("Opgave 3.1")
# for at se data anvend: print(data)
print("Data er diskrete.")

print("\n")
print("Opgave 3.2")

# Vælg hvilke datakolonner der skal plottes
studietimer = data['studietimer']
karakterer = data['gns_gym']
ids = data['id']
# Vælg hvordan data skal inddeles i bins

# Settings til histogrammet
ax1.set_title('Opgave 3.2')
ax1.set_xlabel('Studietimer')
ax1.set_ylabel('Antal')


# Plot median-linje
mean_studietimer = statistics.mean(studietimer)
ax1.axvline(mean_studietimer, color='red', label='Mean')

ax1.hist(studietimer, histtype='bar', edgecolor='black')


print("\n")
print("Opgave 3.3")
print("Opgave 3.3 udelades her.")

print("\n")
print("Opgave 3.4")
# kovariansmatricen udledes således
covariance = cov(karakterer, studietimer)
print("Kovariansmatrice: ")
print(covariance)

# korrelation, anvender (from scipy.stats import pearsonr)
correlation = pearsonr(karakterer, studietimer)
print("Korrelation: " + str(correlation))
print("Der er altså en positiv samvarians mellem karakterer og studietimer")

print("\n")
print("Opgave 3.4")
# I denne opgave anvendes [import statsmodels.api as sm] pakken.
model = sm.OLS(karakterer, studietimer)
results = model.fit()
print(results.summary())
# OBS! der er uoverstemmelse i resultaterne ift. rettevejledning.

print("\n")
print("Opgave 3.5")
ax2.set_title("Opgave 3.5")
ax2.set_xlabel("Studietimer")
ax2.set_ylabel("Karakterer")
theta = np.polyfit(studietimer, karakterer, 1)
y_line = theta[1] + theta[0] * studietimer
ax2.scatter(studietimer, karakterer)
ax2.plot(studietimer, y_line, 'r', label='Line of best fit')

# Vis grafer
plt.show()
