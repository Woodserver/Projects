test = "testing"
print (test[2])
    
    
    #this will be how we write to the final txt file. below is the fomat
    #vcardfile.write is the method used
    #vcardfile.write(spreadsheet.cell_value(datalines, 0))

    #(f"""BEGIN:VCARD
    #VERSION:3.0
    #FN:{lastname}, {firstname}
    #TEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}
    #END:VCARD
    #""")
