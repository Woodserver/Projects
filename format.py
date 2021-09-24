vcardfile = open('vcard-non-apple.txt','a+')
phonenumber = "919-867-5309"
lastname = "Roberts"
firstname = "Jonathan"

vcardfile.write(f"""
BEGIN:VCARD
VERSION:3.0
FN:{lastname}, {firstname}
TEL;TYPE=VOICE,CELL;VALUE=text:{phonenumber}
END:VCARD""" * 8)