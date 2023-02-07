import pandas as pd
d1={'name':['apple','mango','banana'],'country':['india','japan','decock']}
df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'id':[1,2,3],'name':['sleep','hen','dfgh']})
print(df2)
df_merged=df1.merge(df2,how='right',on=df2['id'])
print(df_merged)