import pandas as pd

df = pd.DataFrame([[1,2,3],[4,6,7],[9,8,3]], columns=["A","B","C"])

df.head()
df.head(1)
df.tail(2)
df.columns
df.index
df.index.tolist()
df.describe() #gives values like count, mean, std , min etc 
df.shape

#NEXT CELL 
coffee= pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
coffee.head()

bios = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv")
bios.head()


#Accessing DATAS IN PANDAS
coffee.head() #top 5 data frames only 
coffee #all data frames 

