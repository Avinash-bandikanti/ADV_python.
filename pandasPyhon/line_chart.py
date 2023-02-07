from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["YEAR","SALES"],
            [500,182],[1000,222],[1500,162],[2000,250],[2500,116]]
for i in sales_data:
    sheet.append(i)
line=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=5,min_col=1,max_col=2)
line.add_data(data,titles_from_data=True)
sheet.add_chart(line,"E2")
wb.save("C://hcl1/line_chart.xlsx")
