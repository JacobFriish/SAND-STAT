import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
from scipy.stats import kurtosis, skew, describe


y = np.array([1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0])
y0 = (y==0)
y1 = (y==1)

print("Opgave 1.1")
print("\n")
sum_y0 = sum(y0)
sum_y1 = sum(y1)
n = sum_y0 + sum_y1
f_y0 = sum_y0 / n
f_y1 = sum_y1 / n
y_m = f_y1
std_y0 = y0.std()
std_y1 = y1.std()
data_sorted = np.sort(y)

print("Mean f_y0: " + str(f_y0))
print("Mean f_y1: " + str(f_y1))
print("Std f_y0: " + str(std_y0))
print("Std f_y1: " + str(std_y1))

print("\n")
print("Opgave 1.2")
y_alt = y+1
y0_alt = (y_alt==1)
y1_alt = (y_alt==2)
sum_y0_alt = sum(y0_alt)
sum_y1_alt = sum(y1_alt)
n = sum_y0_alt + sum_y1_alt
f_y0_alt = sum_y0_alt / n
f_y1_alt = sum_y1_alt / n
std_y0_alt = y0_alt.std()
std_y1_alt = y1_alt.std()
data_sorted_alt = np.sort(y_alt)

print("Mean f_y0_alt: " + str(f_y0_alt))
print("Mean f_y1_alt: " + str(f_y1_alt))
print("Std f_y0_alt: " + str(std_y0_alt))
print("Std f_y1_alt: " + str(std_y1_alt))
print("Error: " + str(f_y0_alt - f_y0) + "," + str(f_y1_alt - f_y1) + " (0=correct calculation)")

print("\n")
print("Opgave 1.3")
print(describe(y))

print("\n")
print("Opgave 1.4")
print("1. Moment: " + str((y_m)))
print("2. Moment: " + str(y_m * (1-y_m)))
print("3. Moment: " + str(((1-y_m)-y_m)/(y_m*(1-y_m))**(0.5)))
print("4. Moment: " + str((1-6*(y_m*(1-y_m)))/(y_m*(1-y_m))+3))

print("\n")
print("Opgave 1.5")
print(statistics.median(data_sorted))
print("Anvendelsen af fraktiler er begrænset, og vil blot fortælle om det eksakte nummer på frkatilens plads.")