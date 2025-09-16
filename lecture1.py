import pandas as pd

df = pd.DataFrame([[1,2,3],[4,6,7],[9,8,3]], columns=["A","B","C"])

df.head()
df.head(1)
df.tail(2)
df.columns
df.index
df.index.tolist()
