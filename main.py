import pandas as pd

df = pd.read_csv("./dataset/laptops.csv")

# what is the count of the different processor brands?
print(df["processor_brand"].value_counts())
print()

# what are the results for showing laptoops with a certain processor brand and below a certain price?
df_cpu = df["processor_brand"] == "amd"
df_price = df["Price"] < 22000
print(df[df_cpu & df_price])
print()

# what are the 5 most expensive (or cheap) laptops?
df_sorted_price = df.sort_values("Price", ascending = False).head()
print(df_sorted_price)
