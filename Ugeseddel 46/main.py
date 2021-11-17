import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
from scipy.stats import kurtosis, skew, describe


data = pd.read_csv("data uge 46.csv")
print(data)


print("\n")
print("Opgave 3.1")
print("Data er diskrete.")

print("\n")
print("Opgave 3.2")

# Settings til histogrammet
plt.style.use('fivethirtyeight')
plt.title('Histogram, karakterer og studietimer')
plt.xlabel('Studietimer')
plt.ylabel('Density')
plt.tight_layout()
plt.show()