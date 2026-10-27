import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(
    "hf://datasets/Yoad22/craigslist-used-cars-eda/vehicles_clean.csv",
    index_col="manufacturer",
)


# load
# df = pd.read_csv("final2024.csv", index_col="Brand")
# df = df.dropna()
df.info()

# selection
df["paint_color"]
df.sample(5)
df.query('state == "ny"').info()
df.loc["alfa-romeo"].head(5)
df.query("price == 54241")
df.loc[df["price"] <= 10000.0].sample(5)
df.max()
df.describe()
df["year"].value_counts().head(5)
df.sort_values(by="price", ascending=False).head(5)
df.loc[df["year"] == 2005].head(5)

plt.title("used car correlations heatmap")
plt.figure(figsize=(12, 8))
sns.heatmap(
    df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1
)


# create
"""
df["Not_white"] = df["Color"] != "سفید"
# df.loc[df["Not_white"] != True].shape
df.query("Not_white == True")["Price"].sum()

df.query("Not_white == True").sort_values(by="Brand", ascending=False).head(5)
"""
