from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df["target"] = wine.target
# print(wine_df.head())

wine.head()
