import pandas as pd
import math
import matplotlib.pyplot as plt
df = pd.read_csv("annotations2.csv")
print(df.head())
b = (max(df["Nodule_diameter_mm"])-min(df["Nodule_diameter_mm"]))/0.2
print(b)
plt.hist(df["Nodule_diameter_mm"],bins=math.ceil(b))
plt.xlabel("Nodule Diameter in mm")
plt.ylabel("Frequency")
plt.title("Nodule diameter graph")
print(plt.show())
plt.savefig("output.jpg")