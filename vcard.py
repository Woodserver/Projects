import xlrd

#specifing where the data is located on the machine
location = ('Book1.xls')
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
#(0 is the row, 0 is the cell)
print(sheet.cell_value(0, 0))