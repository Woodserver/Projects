import xlrd
location = ('vcards\Book1.xlsx')                 #point the script to the location of the spreadsheet
vcardfile = open('vcard-apple.vcf','a+')
workbook = xlrd.open_workbook(location)
spreadsheet = workbook.sheet_by_index(0)
fullname = ''
userphonenumber_list = []
userfullname_list = []

def write_to_vcard(lastname, firstname, phonenumber):
    vcardfile.write(f"""
BEGIN:VCARD
VERSION:3.0
N:{lastname};{firstname}
FN:{lastname}, {firstname}
TEL;TYPE=CELL;TYPE=VOICE:{phonenumber}
END:VCARD""")

#The next two for loops processes the data in the spreadsheet by appending every other value to either the
#userphonenumber_list or userfullname_list
for datalines in range(spreadsheet.nrows):
    phonenumbers_filtered_from_spreadsheet = spreadsheet.cell_value(datalines, 0)
    userphonenumber_list.append(phonenumbers_filtered_from_spreadsheet)
#grabbing the numbers mason
for datalines in range(spreadsheet.nrows):
    fullnames_filtered_from_spreadsheet = spreadsheet.cell_value(datalines, 1)
    userfullname_list.append(fullnames_filtered_from_spreadsheet)

#now we zip both lists into a single for loop to finally create the vcard
zip_both_lists = zip(userfullname_list, userphonenumber_list)
for user_fullnames, user_phonenumbers in zip_both_lists:
    phonenumber = user_phonenumbers
    fullname = user_fullnames
    firstname = fullname.split()[0]
    lastname = fullname.split()[-1]
    write_to_vcard(lastname, firstname, phonenumber)