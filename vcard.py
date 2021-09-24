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

def write_to_vcard():
    vcardfile.write(f"""
    BEGIN:VCARD
    VERSION:3.0
    FN:{lastname}, {firstname}
    TEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}
    END:VCARD""")
    break

def check_if_phonenumber(phonenumber: str) -> str:
    if ("9" in (spreadsheet.cell_value(datalines, 0))[2]):     ### Bug found, duplicating code based on multiple "9"'s in the string
        return phonenumber == (spreadsheet.cell_value(datalines, 0))
        

def check_if_name(firstname: str) -> str:
    if ("9" not in (spreadsheet.cell_value(datalines, 0))[2]):    #Duplicating names for some reason
        fullname = (spreadsheet.cell_value(datalines, 0))
        return firstname == fullname.split()[0]
        #return lastname == fullname.split()[-1]

 ###Sorting each dataline in the spreadsheet. Checking if the 3rd value is a number
for datalines in range(spreadsheet.nrows):
    phonenumber = (check_if_phonenumber)
    firstname = (check_if_name)
    #check_if_phonenumber(phonenumber)
    #check_if_name(firstname, lastname)
    write_to_vcard()