import pandas as pd
d={"name":["india","austrlia","srilanka","england"],"rank":[1,2,3,4]}
Team=["india","austrlia","srilanka","england"]
s=pd.Series(Team,index=['a','b','c','d'])
print(s)
df=pd.DataFrame(d)
print(df)
#print(s)
#print(s[:2])
#print(s.iloc[:2])