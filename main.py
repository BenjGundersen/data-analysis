import pandas as pd

df = pd.read_csv("./dataset/laptops.csv")
print(df["processor_brand"].value_counts())

print(df[df["processor_brand"] == "amd"])

