import pandas as pd
d={"name":["india","austrlia","srilanka","england"],"rank":[1,2,3,4],"win_per":[90,80,70,60]}
df=pd.DataFrame(d)
print(df)
#df1=df.rename(columns={"rank":"Ranking"})
#print(df1)
df.rename(columns={"rank":"RANKING"},inplace=True)
print(df)
print(df.iloc[:,[0,1]])
print(df.iloc[:3,-1])