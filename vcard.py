import xlrd

#specifing where the data is located on the machine
location = ('Book1.xls')
vcardfile = open('vcard-non-apple.txt','a+')
workbook = xlrd.open_workbook(location)
spreadsheet = workbook.sheet_by_index(0)
fullname = ""
firstname = ""
lastname = ""
phonenumber = ""


 ###Sorting each dataline in the spreadsheet. Checking if the 3rd value is a number
for datalines in range(spreadsheet.nrows):
    if (spreadsheet.cell_value(datalines, 0))[2] == '9'or'8'or'7'or'6'or'5'or'4'or'3'or'2'or'1'or'0':
        phonenumber = (spreadsheet.cell_value(datalines, 0))
    elif (spreadsheet.cell_value(datalines, 0))[2] != '9'or'8'or'7'or'6'or'5'or'4'or'3'or'2'or'1'or'0':
        fullname = (spreadsheet.cell_value(datalines, 0))
    print(f"""BEGIN:VCARD
    VERSION:3.0
    FN:{lastname}, {fullname}
    TEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}
    END:VCARD
    """)