import xlrd

#specifing where the data is located on the machine
location = ('Book1.xls')
vcardfile = open('vcard-non-apple.txt','w+')
workbook = xlrd.open_workbook(location)
spreadsheet = workbook.sheet_by_index(0)
firstname = ""
lastname = ""
phonenumber = ""


 #printing all first rows on each column
for datalines in range(spreadsheet.nrows):
    if spreadsheet.[2] == :
        print ('omge its 9')

    
    
    
    
    #this will be how we write to the final txt file. below is the fomat
    #vcardfile.write is the method used
    #vcardfile.write(spreadsheet.cell_value(datalines, 0))

    #(f"""BEGIN:VCARD
    #VERSION:3.0
    #FN:{lastname}, {firstname}
    #TEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}
    #END:VCARD
    #""")
