import pandas as pd

df = pd.read_csv('data/wine_sample.csv')

df.drop(columns=['Id'], inplace=True)

df.to_csv("data/wine_sample.csv", index=False)