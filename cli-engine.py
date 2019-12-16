from ccore import convertor, chkBond, displax

iupac = input('Enter the IUPAC name of the carbon compound <x> ')
a = convertor(iupac)
b = chkBond(a)
print()
print()
print(" ============== COMPUTED RESULT ===============")
print()
displax(b)
print()
print("""
The carbonic repository is not completely tested.
We require testers who can check if the different 
IUPAC names corresponds to the result.
I am looking forward for Issues, Feature Requests.

Contribute on https://github.com/srevinsaju/carbonic
Created by a 16 dev
""")
