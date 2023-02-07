from openpyxl.utils import FORMULAE
#print(FORMULAE)
import openpyxl
wb=openpyxl.load_workbook("C://hcl1/emp.xlsx")
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save("C://hcl1/sum.xlsx")
