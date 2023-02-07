from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class People():
    name : str
    num : int
    age : int
P=[People("Avinash",3,22),People("b",2,3),People("c",5,6)]
data=[[p.name,p.num,p.age]for p in P]
data=[['NAME','NUM','AGE']]+data
for d in data:
    sheet.append(d)
wb.save("C://hcl1/data_exl.xlsx")

