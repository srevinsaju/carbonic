"""
carbonic on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC COMMAND LINE INTERFACE
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic

ALL CODE IS LICENSED UNDER GNU-AGPL LICENSE. READ LICENSE FOR MORE INFORMATION

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
