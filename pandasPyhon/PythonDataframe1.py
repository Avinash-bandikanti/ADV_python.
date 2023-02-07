import pandas as pd
d={"name":["india","austrlia","srilanka","england"],"rank":[1,2,3,4],"win_per":[90,80,70,60]}
df=pd.DataFrame(d)
df.rename(columns={"rank":"RANKING"},inplace=True)
df.set_axis(df['name'],inplace=True)
#print(df.loc[df['RANKING']>=3])
df.drop('win_per',axis=1,inplace=True)
print(df)