location = ('Book1.xls')
vcardfile = open('vcard-non-apple.txt','a+')
workbook = xlrd.open_workbook(location)
spreadsheet = workbook.sheet_by_index(0)