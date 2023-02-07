import pandas as pd
import numpy as np
data1=pd.read_excel("C://hcl1/emp.xlsx",sheet_name='Sheet1')
#exceldata3=pd.concat([exldata1,exldata1],axis=1,join='inner')
data2=pd.read_excel("C://hcl1/emp.xlsx",sheet_name='Sheet2')
print(data1)
print(data2)
print(data1.compare(data2))
#data1['price]=np.where(data1['prisr']==data2['pricre],0,data2['prise]-data1['prise'])
