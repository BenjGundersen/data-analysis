import pandas as pd

df = pd.read_csv("./dataset/laptops.csv")

# what is the count of the different processor brands?
print(df["processor_brand"].value_counts())
print()

# how to see data for laptops of a certain processor brand and price?
df_cpu = df["processor_brand"] == "amd"
df_price = df["Price"] < 22000
print(df[df_cpu & df_price])
print()

# what if we want to see the a descending or ascending list of prices? (5 laptops)
df_sorted_price = df.sort_values("Price", ascending = True).head()
print(df_sorted_price)
