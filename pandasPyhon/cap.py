from openpyxl import Workbook
from pandas import read_excel
sheet=[]
file="C://hcl1/"
for f in ['jan',"feb","march","april"]:
    name='HCL_SALES'+f
    df=read_excel(file,f)
    sheet.append(df)
print(sheet)