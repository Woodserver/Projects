import xlrd

#specifing where the data is located on the machine
location = ('testing.xlsx')
vcardfile = open('vcard-non-apple.txt','a+')
workbook = xlrd.open_workbook(location)
spreadsheet = workbook.sheet_by_index(0)
fullname = ""
firstname = ""
lastname = ""
phonenumber = ""

def write_to_vcard():
    vcardfile.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{lastname}, {firstname}\nTEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}\nEND:VCARD\n")

for datalines in range(spreadsheet.nrows)[1::2]:
    





        #phonenumber = (spreadsheet.cell_value(datalines, 0))
    #print (spreadsheet.cell_value(datalines, 0))
    #for datalines in range(spreadsheet.nrows)[2::2]:
    #    fullname = (spreadsheet.cell_value(datalines, 0))
     #   firstname = fullname.split()[0]
      #  lastname = fullname.split()[-1]
    #print (spreadsheet.cell_value(datalines, 0))
#write_to_vcard()