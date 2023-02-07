from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook = load_workbook(filename="C://hcl1/sum.xlsx")
sheet=workbook.active
logo=Image("C://hcl1/download.png")
logo.height=150
logo.width=150
sheet.add_image(logo,"D10")
workbook.save(filename="C://hcl1/image.xlsx")