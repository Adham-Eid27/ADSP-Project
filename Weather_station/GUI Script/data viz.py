import pandas as pd

df = pd.read_csv('data.csv', header=None)
df = df.drop(df.columns[[0, 1, 2]], axis=1)
df.to_csv("data.csv", header=["Air Quality", "Wind Speed", "Temperature", "Humidity", "Time"],
          index=False)


