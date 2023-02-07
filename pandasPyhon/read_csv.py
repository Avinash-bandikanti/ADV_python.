import numpy as np
import pandas as pd
df=pd.read_csv("..//data1/submission.csv")
#print(df.shape)
#print(df)
#print(df.isna().any())
#df.drop(['Survived'],axis=1,inplace=True)
#df.drop(method='ffill',inplace=True)
#print(df.isna().sum())
#print(df['embarked'])
#print(pd.crosstab(index=df["PassengerId"],columns=df["Survived"]))
#print(df.groupby(['Sex','Survived'])['Survived'].count().plot.bar)
#print(pd.pivot_table(df,index=['PassengerId','Survived'],aggfunc=np.sum))
#print(df.sort_values(by=['Pclass','Age'],ascending=False))
