#!/usr/bin/env python3
"""
carbonic on github by @srevinsaju

THIS IS MAIN MODULE FOR GUI INTEGRATION PORT.

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""
# imports
import os
from math import ceil
import sys
import time



# reusable data
TERMINAL = ["CH₃", "CH₂"]
BOND = ["CH₃-", "CH₂-", "CH₁=", "CH₁-", " C ≡"]
counter2 = 1
answer = ""
k = 0
RESULT = ""
NNNRESULT = ""
NNNNRESULT = ""



def convertor(inp):
	func = None
	inp = inp.strip()
	inp = inp.lower()
	cyclic = False
	benzeneChildBool = False
	addOnBranches = []
	addOnBranchesNum = []
	listOfAdditionalStuff = ["methyl", "ethyl", "propyl", "butyl", "pentyl", "hexyl"]
	BenzeneChild = ["benz", "naphthal", "anthrac", "chrys", "pyrene", "corannulene", "coronene", "hexahelic"]
	count = 1
	print(inp.find("["), " is INDEX")
	if((inp.find("["))!=-1):

	    for i in listOfAdditionalStuff:
	        if(inp.find(i)==-1):
	            print("LOG: passed", i)
	            count+=1
	            continue
	            # continue : removed because repeated methyl or ethyl groups are not considered
	        else:
	            while inp.find(i)!=1:
	                print("found ", i)
	                indic = inp.find(i)
	                try:
	                    addOnNum = int(inp[inp.find("[")+1:indic-1])
	                except ValueError:

	                    print("WARNING: Getting out of loop")
	                    break

	                print("LOG : AddOnNum is ", addOnNum)
	                addOnBranchesNum.append(addOnNum)
	                addOnBranches.append(i)
	                inp=inp[(indic+len(i)+1):]

	                count+=1
	                print("LOG: inp:", inp)


	else:
	    print("HOHO")
	print(inp)
	print("LOG: addOnBranchesNum = ", addOnBranchesNum)
	print("LOG: addOnBranches = ", addOnBranches)
	# for use in emergency :)
	tmpinp = inp
	# initialize bondpos_chkBond value to prevent NameError
	bondpos_chkBond = []

	# check if the given name has halogen names
	haloIndexConv = []
	haloGroupConv = []

	halogens = ["bromo", "fluoro", "iodo", "chloro"]
	for halogen in halogens:
	    if inp.find(halogen)>-1:
	        while inp.find(halogen)>-1:
	            print("LOG: detected halogen", halogen)
	            haloIndex = inp.find(halogen)
	            if inp[haloIndex-1:haloIndex]=="-":
	                print("LOG: Found numeric value")
	                print("LOG: inp @ halo", inp)
	                if(inp[0]==","):
	                    print("LOG: comma pased in halo section")
	                    inp=inp[1:]
	                    print("LOG: inp after comma @ halo", inp)
	                    continue

	                else:
	                    print("LOG: No comma in ", inp)
	                try:
	                    print("LOG: inp[:haloIndex-1] is ", inp[:haloIndex-1])
	                    haloIndexConv.append(int(inp[:haloIndex-1]))
	                    haloGroupConv.append(halogen)
	                    inp = inp[haloIndex+len(halogen):]
	                    print("LOG: inp is", inp)
	                except ValueError:
	                    print("LOG: trying once again")
	                    try:
	                        print("LOG: inp[:haloIndex-2] is ", inp[:haloIndex-2])
	                        haloIndexConv.append(int(inp[:haloIndex-2]))
	                        haloGroupConv.append(halogen)
	                        inp = inp[haloIndex-1+len(halogen):]
	                        print("LOG: inp is", inp)
	                    except ValueError:
	                        try:
	                            print("LOG: inp[:haloIndex-3] is ", inp[:haloIndex-3])
	                            haloIndexConv.append(int(inp[:haloIndex-3]))
	                            haloGroupConv.append(halogen)
	                            inp = inp[haloIndex-2+len(halogen):]
	                            print("LOG: inp is", inp)
	                        except ValueError:
	                            print("LOG: Really sorry about that")
	                            break
	            else:
	                print("LOG: No halo value found ")
	                haloIndexConv.append(1)
	                haloGroupConv.append(halogen)
	                inp = inp[haloIndex+len(halogen):]
	                print("LOG: inp is", inp)
	                break

	    else:
	        continue

	print("LOG: haloIndexConv:", haloIndexConv)
	# read the #- value of the IUPAC name
	for i in tmpinp:
	    if(inp[0].isalpha()):
	        print("LOG: isAlpha")
	        break
	    try:
	        if(inp[0].isnumeric):
	            bondpos_chkBond.append(inp[0])
	            inp = inp[1:]
	        else:
	            print("LOG: No",i)
	    except IndexError:
	        print("No index, passing")
	    try:
	        if(inp[0]==","):
	            inp = inp[1:]
	    except IndexError:
	        print("No Index, passing")
	    try:
	        if(inp[0] == "-"):
	            inp = inp[1:]
	            break
	        else:
	            print("NONO", i)

	    except IndexError:
	        print("No Index, passing")

	# Check the carbon compound is alkane, alkene or alkyne
	if(inp.endswith("ane")):
	    if(inp.startswith("cyclo")):
	        print("LOG: Detected Cyclic Carbon Compounds")
	        bond_int = 4
	        inp = inp[5:]
	        print("LOG: Logging Cyclic inp=", inp)
	        cyclic = True
	    else:
	        bond_int = 1
	        print("LOG: alkane")
	    restOfInp = inp.partition("ane")
	elif(inp.endswith("ene")):
	    print("alken")

	    for i in BenzeneChild:
	        if (inp.startswith(str(i))):
	            childOfBenzeneType = i
	            benzeneChildBool = True
	            break

	    bond_int = 2
	    restOfInp = inp.partition("ene")

	elif(inp.endswith("yne")):
	    bond_int = 3
	    print("LOG: alkyne")
	    restOfInp = inp.partition("yne")
	elif(inp.endswith("one")):
	    bond_int = 5
	    print("LOG: Detected Ketone")
	    restOfInp = inp.partition("one")
	elif(inp.endswith("oic acid")):
	    bond_int = 7
	    print("LOG: Detected Carboxylic Acid")
	    restOfInp = inp.partition("oic acid")
	elif(inp.endswith("ol")):
	    bond_int = 8
	    print("LOG: Detected Alcohol")
	    restOfInp = inp.partition("ol")
	elif(inp.endswith("al")):
	    bond_int = 6
	    print("LOG: Detected Aldehyde")
	    restOfInp = inp.partition("al")

	else:
	    bond_int = 0

	    print("ERROR: INVALID")
	    return "ERROR 344"
	restOfInp = list(restOfInp)
	noofc0 = 0
	sepInp = restOfInp
	if(restOfInp[0].find("hect")>-1):
	    restOfInp[0]=restOfInp[0][5:]
	    hect = True
	else:
	    hect = False

	if(restOfInp[0].find("triacont")>-1):
	    try:
	        noofc0 +=30
	        restOfInp[0] = restOfInp[0].replace('triacont', '')
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("tetracont")>-1):
	    try:
	        noofc0 +=40
	        restOfInp[0] = restOfInp[0].replace('tetracont', '')
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("pentacont")>-1):
	    try:
	        noofc0 +=50
	        restOfInp[0] = restOfInp[0].replace('pentacont', '')
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("hexacont")>-1):
	    try:
	        restOfInp[0] = restOfInp[0].replace('hexacont', '')
	        noofc0 +=60
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("heptacont")>-1):
	    try:
	        restOfInp[0] = restOfInp[0].replace('heptacont', '')
	        noofc0 +=70
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("octacont")>-1):
	    try:
	        restOfInp[0] = restOfInp[0].replace('octacont', '')
	        noofc0 +=80
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("nonacont")>-1):
	    try:
	        restOfInp[0] = restOfInp[0].replace('nonacont', '')
	        noofc0 +=90
	    except UnboundLocalError:
	        print("ERROR")


	if(restOfInp[0].startswith("meth")or restOfInp[0].startswith("un")or restOfInp[0].startswith("hen")):
	    if(restOfInp[0].startswith("meth")or restOfInp[0].startswith("hen")):
	        noofc0 += 1
	    else:
	        noofc0 += 1 #*restOfInp[0].count("un")

	if(restOfInp[0].startswith("eth")or restOfInp[0].startswith("do")):
	    if(restOfInp[0].startswith("eth")):
	        noofc0 += 2
	    else:
	        noofc0 += 2 #*restOfInp[0].count("do")
	if(restOfInp[0].startswith("prop")or restOfInp[0].startswith("tri")):
	    if(restOfInp[0].startswith("prop")):
	        noofc0 += 3
	    else:
	        noofc0 += 3 #*restOfInp[0].count("tri")
	if(restOfInp[0].startswith("but")or restOfInp[0].startswith("tetra")):
	    if(restOfInp[0].startswith("but")):
	        noofc0 += 4
	    else:
	        noofc0 += "4" # *restOfInp[0].count("tetra")
	if(restOfInp[0].startswith("pent")):
	    noofc0 += 5
	if(restOfInp[0].startswith("hex")):
	    noofc0 += 6
	if(restOfInp[0].startswith("sept") or restOfInp[0].startswith("hept")):
	    noofc0 += 7
	if(restOfInp[0].startswith("oct")):
	    noofc0 += 8
	if(restOfInp[0].startswith("non")):
	    noofc0 += 9
	if(restOfInp[0].startswith("dec")):
	    noofc0 += 0

	if(restOfInp[0].find("dec")>-1):
	    try:
	        noofc0 = 10+noofc0
	    except UnboundLocalError:
	        print("ERROR")
	if(restOfInp[0].find("cos")>-1):
	    try:
	        noofc0 = 20+noofc0
	    except UnboundLocalError:
	        print("ERROR")
	if hect:
	    noofc0 = 100+noofc0

	restOfInp = restOfInp[:-1]
	print(restOfInp)
	print(noofc0)

	return noofc0, bond_int, bondpos_chkBond, addOnBranchesNum, addOnBranches, benzeneChildBool, haloIndexConv, haloGroupConv

def addfunctionalgrp(noofc):
	functionalgrp = input(
	    "Enter the type of functional group you would like to append to the current Carbon chain ---> ")
	if (functionalgrp == "none"):
	    print("Thank you for using SS Carbon Calculator! ")
	elif (functionalgrp == "Haloalkane"):
	    halocounter = input("Enter the position of the halogen bond --> ")
	    if (halocounter == noofc or halocounter == 0):
	        print("Invalid Input!")
	    else:
	        halogen = input("Enter the symbol of the halogen ---> ")
	        if(halocounter == 1):
	            tempterminal = answer[-4:]
	            tempterminal = tempterminal.replace("CH₃", "CH₂")
	            answer = answer[:-5]+tempterminal


	    restxt = self.chkBond(bondorder, noofc, bondpos_chkBond, numbranch, branch, benzylBool, haloIndexConv, haloGroupConv)

	    leng = len(restxt); print(restext)
   
def alkenebond(bondpos=1, answer_src = "" ):
	# Check the inputted value,
	# Check if bondpos value and answer_src is valid
	
	if bondpos is None:
		bondpos = placer.value()
	else:
		bondpos = bondpos
	if answer_src is None:
		answer = elf.output.text()
	else:
		answer = answer_src
	print(answer+"ANS")
	answer = answer[:(4 * (bondpos - 1))] + \
			            BOND[2] + answer[(4 * (bondpos)):]
	answer = answer.replace("=CH₂-", "=CH₁-")
	answer = answer.replace("=CH₁=", "= C =")
	print(answer)
	noofcc = answer.count("C")

def alkynebond():
	bondpos = placer.value()
	answer = output.text()
	print(answer+"ANS")

	# -------------------------------------
	answer = answer[:(4 * (bondpos - 1))] + \
	                    BOND[4] + answer[(4 * (bondpos)):]
	answer = answer.replace("≡CH₂-", "≡ C -")

	if (answer[(4 * (bondpos - 1) + 3):(4 * (bondpos - 1) + 8)] == "≡CH₂-"):
	    print("≡")
	    answer = answer[:(4 * (bondpos - 1) + 3)] + \
	        "≡ C -" + answer[(4 * (bondpos - 1) + 8):]

	print(answer)
	# -------------------------------------
	noofcc = answer.count("C")
	# FIXME :: ->
	#self.output.setText(answer)

	#self.placer.setMinimum(int(bondpos)+2)
	#self.placer.setValue(int(bondpos)+2)
	#self.placertxt.setText(str(bondpos+2))
	if(bondpos+2>noofcc - 2):
	    print("Disabling Slider")
	    #self.placer.setEnabled(False)
	    #self.pushButton_3.setEnabled(False)
	else:
		pass
	    #self.placer.setMaximum(noofcc - 2)



def alkane(noofc):
	#pushButton_3.setEnabled(False)
	if (noofc == 1):

	    answer = "CH₄"
	else:

	    answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
	print(answer)
	#self.output_hi1_2.setText(" "*len(answer))
	#self.output_hi2_2.setText(" "*len(answer))
	#self.output_lo1_2.setText(" "*len(answer))
	#self.output_lo2_2.setText(" "*len(answer))
	return answer

def ketone(noofc, bondpos_chkBond):
	if(bondpos_chkBond == []):
	    bondpos_chkBond =[2]
	else:
	    pass
	if (noofc == 1):

	    answer = "R-CO"
	    print(answer)
	elif (noofc == 2):
	    answer = "methylenecyclopropyl"
	    print(answer)
	else:
	    k = 1
	    answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
	    for i in bondpos_chkBond:

	        bondpos = int(i)
	        print("LOG:", bondpos, '=', noofc)
	        if((bondpos==noofc)or(bondpos==1)):
	            answer = "Error! Ketone functional group cannot be placed at the terminal ends of a carbon structure."
	            break

	        answer = answer[:(4 * (bondpos - 1))] + \
	                        "CO -" + answer[(4 * (bondpos)):]

	        answer = answer.replace("=CH₂-", "=CH₁-")
	        answer = answer.replace("=CH₁=", "= C =")
	        print(answer)

	    #self.placer.setMinimum(2)
	    #self.placer.setMaximum(noofc - 2)
	    #self.placer.setEnabled(True)
	    #self.pushButton_3.setEnabled(True)
	return answer

def aldehyde(noofc, bondpos_chkBond):
	if not bondpos_chkBond:
	    bondpos_chkBond = [noofc-1]
	    ans = alkane(noofc-1)
	else:

	    ans = alkene(noofc-1, bondpos_chkBond, True)



	branchConv_aldehyde = "CHO"
	spac = " "
	rndcnt = 1
	self.output_lo2_2.setText(len(ans)*spac)
	self.output_lo1_2.setText(len(ans)*spac)
	self.output_hi2_2.setText(len(ans)*spac)
	self.output_hi1_2.setText(len(ans)*spac)
	for i in bondpos_chkBond:
	    nooc00 = noofc-1
	    bondpos = int(i)
	    print("LOG: nooc00", nooc00)

	    print(bondpos, '=', noofc)
	    if(bondpos==1):
	        ans = "CHO-CH₂-"+ans[4:]
	        self.output_lo2_2.setText(len(ans)*spac)
	        self.output_lo1_2.setText(len(ans)*spac)
	        self.output_hi2_2.setText(len(ans)*spac)
	        self.output_hi1_2.setText(len(ans)*spac)
	        continue
	    elif (bondpos==noofc-1):
	        ans = ans[:-3]+"CH₂-CHO"
	        self.output_lo2_2.setText(len(ans)*spac)
	        self.output_lo1_2.setText(len(ans)*spac)
	        self.output_hi2_2.setText(len(ans)*spac)
	        self.output_hi1_2.setText(len(ans)*spac)
	        continue

	    if((bondpos%2==0)and (1<bondpos<noofc-1)):
	        print("LOG: using lo")
	        self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (bondpos - 1))] + \
	                        "CHO " + self.output_lo2_2.text()[(4 * (bondpos)):])
	        self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (bondpos - 1))] + \
	            " ╵  " + self.output_lo1_2.text()[(4 * (bondpos)):])
	    elif((bondpos%2==1)and (1<bondpos<noofc-1)):
	        print("LOG: using hi")
	        self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (bondpos - 1))] + \
	                    "CHO " + self.output_hi2_2.text()[(4 * (bondpos)):])
	        self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (bondpos - 1))] + \
	            " ╷  " + self.output_hi1_2.text()[(4 * (bondpos)):])
	    else:
	        print("ERROR: An unhandled error occured. #101")

	    """
	    if(int(i) == int(ceil((nooc00/2) ))):

	        print("LOG : DIVIDER IS CENTERED ")
	        self.output_lo1.setText(self.output_lo1.text()[(3+((intOfI-1)*4)):])
	        self.output_lo2.setText(" "+ spac*(len(branchConv)) +branchConv)

	    elif(int(i) > int(ceil((nooc00/2) ))):
	        self.output_lo2.setText()
	        self.output_lo1.setText(spac*8*(int(i)-int(ceil((nooc00/2))))+"|")
	    elif(int(i) < int(ceil((nooc00/2) ))):
	        self.output_lo2.setText(spac*(len(branchConv)-1) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-int(i))))
	        self.output_lo1.setText("|" + spac*(8*(int(ceil((nooc00/2)))-int(i))))
	    """
	return ans


def carboxylic(self, noofc, bondpos_chkBond):
	if not bondpos_chkBond:
	    bondpos_chkBond = [1]
	    ans = alkane(noofc)
	else:

	    ans = alkene(noofc, bondpos_chkBond, True)

	spac = " "
	rndcnt = 1
	self.output_lo2_2.setText(len(ans)*spac)
	self.output_lo1_2.setText(len(ans)*spac)
	self.output_hi2_2.setText(len(ans)*spac)
	self.output_hi1_2.setText(len(ans)*spac)
	print("WARNING: for Caarboxylic, only one -COOH functional group is added per structure")
	nooc00 = noofc
	bondpos = int(bondpos_chkBond[0])
	print("LOG: nooc00", nooc00)

	print(bondpos, '=', noofc)
	if((bondpos==1)or(bondpos==noofc)):
	    if(noofc == 1):
	        ans = "H-COOH"
	        pass
	    elif(noofc==2):
	        ans = "CH3-CH2-COOH"
	    else:
	        ans = ans[:-3]+"CH₂-COOH"
	        self.output_lo2_2.setText(len(ans)*spac)
	        self.output_lo1_2.setText(len(ans)*spac)
	        self.output_hi2_2.setText(len(ans)*spac)
	        self.output_hi1_2.setText(len(ans)*spac)

	elif((bondpos%2==0)and (1<bondpos<noofc)):
	    print("LOG: using lo")
	    self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (bondpos - 1))] + \
	                    "COOH" + self.output_lo2_2.text()[(4 * (bondpos)):])
	    self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (bondpos - 1))] + \
	        " ╵  " + self.output_lo1_2.text()[(4 * (bondpos)):])
	elif((bondpos%2==1)and (1<bondpos<noofc)):
	    print("LOG: using hi")
	    self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (bondpos - 1))] + \
	                "COOH" + self.output_hi2_2.text()[(4 * (bondpos)):])
	    self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (bondpos - 1))] + \
	        " ╷  " + self.output_hi1_2.text()[(4 * (bondpos)):])
	else:
	    ans ="ERROR: An unhandled error occured. #101"
	    print(ans)

	    """
	    if(int(i) == int(ceil((nooc00/2) ))):

	        print("LOG : DIVIDER IS CENTERED ")
	        self.output_lo1.setText(self.output_lo1.text()[(3+((intOfI-1)*4)):])
	        self.output_lo2.setText(" "+ spac*(len(branchConv)) +branchConv)

	    elif(int(i) > int(ceil((nooc00/2) ))):
	        self.output_lo2.setText()
	        self.output_lo1.setText(spac*8*(int(i)-int(ceil((nooc00/2))))+"|")
	    elif(int(i) < int(ceil((nooc00/2) ))):
	        self.output_lo2.setText(spac*(len(branchConv)-1) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-int(i))))
	        self.output_lo1.setText("|" + spac*(8*(int(ceil((nooc00/2)))-int(i))))
	    """
	return ans


def alcohol(self, noofc, bondpos_chkBond):
	if not bondpos_chkBond:
	    bondpos_chkBond = [1]
	    ans = alkane(noofc)
	else:

	    ans = alkene(noofc, bondpos_chkBond, True)

	spac = " "
	rndcnt = 1
	self.output_lo2_2.setText(len(ans)*spac)
	self.output_lo1_2.setText(len(ans)*spac)
	self.output_hi2_2.setText(len(ans)*spac)
	self.output_hi1_2.setText(len(ans)*spac)
	print("WARNING: for Alcohol, only one -OH functional group is added per structure")
	nooc00 = noofc
	bondpos = int(bondpos_chkBond[0])
	print("LOG: nooc00", nooc00)

	print(bondpos, '=', noofc)
	if((bondpos==1)or(bondpos==noofc)):
	    if(noofc == 1):
	        ans = "CH3-OH "
	        pass
	    elif(noofc==2):
	        ans = "CH3-CH2-OH "
	    else:
	        ans = ans[:-3]+"CH₂-OH "
	        self.output_lo2_2.setText(len(ans)*spac)
	        self.output_lo1_2.setText(len(ans)*spac)
	        self.output_hi2_2.setText(len(ans)*spac)
	        self.output_hi1_2.setText(len(ans)*spac)

	elif((bondpos%2==0)and (1<bondpos<noofc)):
	    print("LOG: using lo")
	    self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (bondpos - 1))] + \
	                    " OH " + self.output_lo2_2.text()[(4 * (bondpos)):])
	    self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (bondpos - 1))] + \
	        " ╵  " + self.output_lo1_2.text()[(4 * (bondpos)):])
	elif((bondpos%2==1)and (1<bondpos<noofc)):
	    print("LOG: using hi")
	    self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (bondpos - 1))] + \
	                " OH " + self.output_hi2_2.text()[(4 * (bondpos)):])
	    self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (bondpos - 1))] + \
	        " ╷  " + self.output_hi1_2.text()[(4 * (bondpos)):])
	else:
	    ans ="ERROR: An unhandled error occured. #101"
	    print(ans)

	    """
	    if(int(i) == int(ceil((nooc00/2) ))):

	        print("LOG : DIVIDER IS CENTERED ")
	        self.output_lo1.setText(self.output_lo1.text()[(3+((intOfI-1)*4)):])
	        self.output_lo2.setText(" "+ spac*(len(branchConv)) +branchConv)

	    elif(int(i) > int(ceil((nooc00/2) ))):
	        self.output_lo2.setText()
	        self.output_lo1.setText(spac*8*(int(i)-int(ceil((nooc00/2))))+"|")
	    elif(int(i) < int(ceil((nooc00/2) ))):
	        self.output_lo2.setText(spac*(len(branchConv)-1) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-int(i))))
	        self.output_lo1.setText("|" + spac*(8*(int(ceil((nooc00/2)))-int(i))))
	    """
	return ans


def alkene(noofc=1, bondpos_chkBond=[2], normallity=False):
	if(bondpos_chkBond == []):
	    bondpos_chkBond =[2]
	else:
	    pass
	if not normallity:

	    if (noofc == 1):

	        answer = "Not possible"
	        print(answer)
	    elif (noofc == 2):
	        answer = "CH₂=CH₂"
	        print(answer)
	    else:
	        k = 1
	        answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
	        print("LOG: Engine received ", bondpos_chkBond)
	        for i in bondpos_chkBond:

	            bondpos = int(i)
	            print(bondpos, '=', noofc)
	            if((bondpos==noofc)or(bondpos==1)):
	                answer = "Error! Double bondorder cannot be placed at terminal ends"
	                break

	            answer = answer[:(4 * (bondpos - 1))] + \
	                            BOND[2] + answer[(4 * (bondpos)):]

	            answer = answer.replace("=CH₂-", "=CH₁-")
	            answer = answer.replace("=CH₁=", "= C =")
	            print(answer)

	else:
	    k = 1
	    answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
	    print("LOG: Non-alkanised answer 001 :", answer)
	    for i in bondpos_chkBond:

	        bondpos = int(i)
	        print(bondpos, '=', noofc)


	        answer = answer[:(4 * (bondpos - 1))] + \
	                        BOND[2] + answer[(4 * (bondpos)):]
	        answer = answer.replace("=CH₂-", "=CH₁-")
	        answer = answer.replace("=CH₁=", "= C =")
	        answer = answer.replace("=", "-")

	        print("LOG: Non-alkanised alkene answer", answer)

	    self.placer.setMinimum(2)
	    self.placer.setMaximum(noofc - 2)
	    self.placer.setEnabled(True)
	    self.pushButton_3.setEnabled(True)
	    """
	    while (k == 1):

	        bondpos = int(input(
	            "Enter the postion of the bond (from least to greatest or left to right) --> "))

	        if (bondpos == 0):
	            k = 0
	        elif (bondpos == 1):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0

	        elif (bondpos == noofc):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0
	        elif (bondpos == noofc - 1):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0
	        else:

	            if (counter3 > bondpos):
	                print("Enter in ascending order")
	                k = 0
	            else:
	                answer = answer[:(4 * (bondpos - 1))] + \
	                    BOND[2] + answer[(4 * (bondpos)):]

	                answer = answer.replace("=CH₂-", "=CH₁-")
	                answer = answer.replace("=CH₁=", "= C =")
	                print(answer)
	                counter3 = bondpos
	  """

	print("OUTPUT 0 : ", answer)
	return answer


def alkyne(noofc=2, bondpos_chkBond=[2]):
	if(bondpos_chkBond == []):
	    bondpos_chkBond =[2]
	else:
	    pass
	if (noofc == 1):

	    answer = "Not possible"
	    print(answer)
	elif (noofc == 2):
	    answer = "CH ≡ CH"
	    print(answer)
	else:
	    k = 1
	    answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
	    counter3 = 0
	    tmp_i=-1
	    for i in bondpos_chkBond:

	        bondpos = int(i)
	        if(bondpos-tmp_i==1):
	            print("Triple bondorder cannot be placed near by because of Carbon tetravalency")
	            answer = "Triple bondorder cannot be placed near by because of Carbon tetravalency"
	            break
	        else:
	            tmp_i = bondpos
	        print(bondpos, '=', noofc)
	        if((bondpos==noofc)or(bondpos==1)):
	            answer = "Error! Triple bondorder cannot be placed at terminal ends"
	            break

	        answer = answer[:(4 * (bondpos - 1))] + \
	                    BOND[4] + answer[(4 * (bondpos)):]
	        answer = answer.replace("≡CH₂-", "≡ C -")

	        if (answer[(4 * (bondpos - 1) + 3):(4 * (bondpos - 1) + 8)] == "≡CH₂-"):
	            print("≡")
	            answer = answer[:(4 * (bondpos - 1) + 3)] + \
	                "≡ C -" + answer[(4 * (bondpos - 1) + 8):]


	    counter3 = 0

	    """
	    while (k == 1):

	        bondpos = int(input(
	            "Enter the postion of the bond (from least to greatest or left to right) --> "))

	        if (bondpos == 0):
	            k = 0
	        elif (bondpos == 1):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0

	        elif (bondpos == noofc):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0
	        elif (bondpos == noofc - 1):
	            print("Double bondorder on terminal carbon atoms are invalid")
	            k = 0

	        else:

	            if (counter3 > bondpos):
	                print("Enter in ascending order")
	                k = 0
	            elif (bondpos == counter3 + 1):
	                print("Valency of Carbon is 4")
	                k = 0
	            else:
	                answer = answer[:(4 * (bondpos - 1))] + \
	                    BOND[4] + answer[(4 * (bondpos)):]
	                answer = answer.replace("≡CH₂-", "≡ C -")

	                if (answer[(4 * (bondpos - 1) + 3):(4 * (bondpos - 1) + 8)] == "≡CH₂-"):
	                    print("≡")
	                    answer = answer[:(4 * (bondpos - 1) + 3)] + \
	                        "≡ C -" + answer[(4 * (bondpos - 1) + 8):]

	                print(answer)
	                counter3 = bondpos
	    """
	return answer

def cyclic(self, noofc,):
	print("LOG: Entered chkbond function with Cyclic entry")
	print("LOG: noofc = ", noofc)
	# check if nmber of carbon is even or not
	if(noofc%2==0):
	    print("LOG: Number of carbons are even")
	    if(noofc>3):
	        print("LOG: condition is true [001]")
	        n = (noofc-2)//2
	        holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
	        self.output_hi2_2.setText(holder) # text box 1
	        self.output_hi1_2.setText("/"+" "*len(holder)+"\\") # text box 2
	        self.output_lo1_2.setText("\\"+" "*len(holder)+"/") # text box 3
	        self.output_lo2_2.setText(holder) # text box 4
	        res = TERMINAL[1] + " "*(len(holder)) + TERMINAL[1]
	        return res

	    else:
	        msg = "ERROR: An unhandled error occured"
	        print(msg)
	        return msg
	else:

	    print("LOG: Number of carbons are odd")
	    if(noofc ==3):
	        print("LOG: Detected cyclopropane")

	        self.output_hi2.setText(TERMINAL[1])
	        self.output_hi1.setText("/   \\")
	        res =  TERMINAL[1]+"-"+TERMINAL[1]
	        return res
	    else:
	        print("LOG: detected noofc ", noofc)
	        print("LOG: condition is false, but odd [002]")
	        n = (noofc-1)//2
	        holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
	        self.output_hi2_2.setText(holder) # text box 1
	        self.output_hi1_2.setText("/"+" "*(len(holder)-2)+"╷"+" ") # text box 2
	        self.output_lo1_2.setText("\\"+" "*(len(holder)-2)+"╵"+" ") # text box 3
	        self.output_lo2_2.setText(holder) # text box 4
	        res = " " + TERMINAL[1] + " "*(len(holder)-2) + "|" +"    "
	        return res


def chkBond(bondorder, noofc, bondpos_chkBond=[2], numbranch=[], branch=[], benzylBool=False, haloIndexConv=[], haloGroupConv=[]):
	branchesList = ["CH₃ ", "CH₂-CH₃ ", "CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₂-CH₃ "]
	counterX = 1
	if(benzylBool):
	    res = cyclic(6)
	    noofc = 6
	    n = (noofc-2)//2
	    holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
	    # FIXME :::::::: __>
	    #self.output_hi2_2.setText(holder) # text box 1
	    #self.output_hi1_2.setText("╔"+" "*len(holder)+"╗") # text box 2
	    #self.output_lo1_2.setText("\\"+" "*len(holder)+"/") # text box 3
	    #self.output_lo2_2.setText(holder.replace("-", "=")) # text box 4
	    return res

	if (bondorder == 1):
	    res = alkane(noofc)
	elif (bondorder == 2):
	    res = alkene(noofc, bondpos_chkBond)

	elif (bondorder == 3):
	    res = alkyne(noofc, bondpos_chkBond)
	elif (bondorder ==4 ):
	    res = cyclic(noofc) #TODO add support for benzene and children
	    return res
	elif bondorder == 5:
	    res = ketone(noofc, bondpos_chkBond)
	elif bondorder == 6:
	    res = aldehyde(noofc, bondpos_chkBond)
	elif bondorder == 7:
	    res = carboxylic(noofc, bondpos_chkBond)
	elif bondorder == 8:
	    print("LOG: Alcohol ++++++++++++++")
	    res = alcohol(noofc, bondpos_chkBond)

	else:
	    res = "Bye Bye!"
	    print(res)


	# halogen -------------------------




	for halogenzip in zip(haloIndexConv, haloGroupConv):
	    if halogenzip[1]=="bromo":
	        plugHalogen = " Br "
	    elif halogenzip[1]=="chloro":
	        plugHalogen = " Cl "
	    elif halogenzip[1]=="iodo":
	        plugHalogen = " I  "
	    elif halogenzip[1]=="fluoro":
	        plugHalogen = " F  "
	    else:
	        plugHalogen = " X  "

	    if not bondpos_chkBond:
	        bondpos_chkBond = [1]

	    # pre decalring variable to prevent UnboundLocalError
	    useHi = False
	    useLo = False
	    print("LOG: haloIndexConv =", halogenzip[0])
	    counter_halo = int(halogenzip[0])
	    spac = " "
	    rndcnt = 1
	    l1occ, l2occ, h1occ, h2occ = False, False, False,False
	    """
	    for m in self.output_lo2_2.text():
	        if m.isalpha():
	            l2occ = True
	    for m in self.output_lo1_2.text():
	        if m.isalpha():
	            l1occ = True
	    for m in self.output_hi2_2.text():
	        if m.isalpha():
	            h2occ = True
	    for m in self.output_hi1_2.text():
	        if m.isalpha():
	            h1occ = True

	    print("LOG: 88", self.output_lo2_2.text())
	    print("LOG: self.output_lo2_2.text().isspace() ", self.output_lo2_2.text().isspace(), l2occ)
	    print("LOG:  self.output_lo1_2.text().isspace()",  self.output_lo1_2.text().isspace(), l1occ)
	    print("LOG: self.output_hi2_2.text().isspace()", self.output_hi2_2.text().isspace(), h2occ)
	    print("LOG: self.output_hi1_2.text().isspace()", self.output_hi1_2.text().isspace(), h1occ)
	    """
	    if not l1occ and not l2occ:
	    	#FIXME
	        #self.output_lo2_2.setText(len(res)*spac)
	        #self.output_lo1_2.setText(len(res)*spac)
	        print("LOG: output lo spaced")
	        useHi = False
	        useLo = True
	    else:
	        if not h1occ and not h2occ:
	        	# FIXME 
	            #self.output_hi2_2.setText(len(res)*spac)
	            #self.output_hi1_2.setText(len(res)*spac)
	            print("LOG: output hi spaced")
	            useHi = True
	            useLo = False
	        else:
	            if h1occ and l1occ and h2occ and l2occ:
	            	# FIXME 
	                # print("LOG: needed area is '", self.output_lo2_2.text()[(halogenzip[0])*4:(halogenzip[0]+1)*4], "'")
	                if(self.output_lo2_2.text()[(halogenzip[0])*4:(halogenzip[0]+1)*4]).isspace():
	                    useLo = True
	                elif(self.output_hi2_2.text()[(halogenzip[0])*4:(halogenzip[0]+1)*4]).isspace():
	                    useHi = True
	                else:
	                    print("ERROR: A very very very unique situation has occured. Kindly report it to @srevinsaju on https://github.com/srevinsaju/carbonic/issues")


	    print("WARNING: for Halogen - functional group is added per structure")
	    nooc00 = noofc

	    print("LOG: nooc00", nooc00)

	    print("LOG: #104", counter_halo, '=', noofc)
	    print("LOG: #105 res", res)
	    # -----------------------
	    if(counter_halo==1):
	        theAlterer_halo = res[:3]
	        branchPosH = 3
	        print("LOG: 1")

	    elif counter_halo == noofc:
	        # theAlterer_halo = res[-3:]
	        branchPosH = halogenzip[0]*4
	        theAlterer_halo = res[(branchPosH-4):branchPosH]
	        print("LOG: 2")
	    else:
	        #theAlterer_halo = res[3+((noofc-1)*4):7+((noofc-1)*4)]
	        branchPosH = halogenzip[0]*4
	        theAlterer_halo = res[(branchPosH-4):branchPosH]
	        print("LOG: 3")
	    print("LOG: theAlterer_halo", theAlterer_halo)
	    if theAlterer_halo[2]=="₂":
	        tmpHolderH = "₁"
	    elif theAlterer_halo[2]=="₃":
	        tmpHolderH = "₂"
	    elif theAlterer_halo[2]=="₁":
	        tmpHolderH = "₀"
	    elif theAlterer_halo[2]=="₀":
	        msg = "ERROR: Carbon valency of 4 is completely utilized."
	        print(msg)
	        res = msg
	        return res
	    else:
	        msg = "ERROR: An unhandled error occured. Sorry. Report immediately to github.com/srevinsaju/carbonic/issues to refine this error"
	        print(msg)
	        res = msg
	        return res
	    # theAlterer = theAlterer[:2]+str(int(theAlterer[2])-1)+theAlterer[3:]

	    theAlterer_halo = theAlterer_halo[:2]+tmpHolderH+theAlterer_halo[3:]
	    theAlterer_halo  = theAlterer_halo.replace("CH₀"," C ")
	    print("LOG: 199++")
	    print("LOG: theAlterer_halo 199++", theAlterer_halo)
	    print("LOG: res[:(halogenzip[0]-4)]", res[:(halogenzip[0]-4)])
	    print("LOG: res[halogenzip[0]:]", res[halogenzip[0]:])
	    print("LOG: halogenzip[0]", halogenzip[0], type(halogenzip[0]))
	    # res = res[:(halogenzip[0]-4)]+theAlterer_halo+res[halogenzip[0]:]
	    if branchPosH == 3:
	        res = res[:(branchPosH-3)]+theAlterer_halo+res[branchPosH:]
	    else:
	        res = res[:(branchPosH-4)]+theAlterer_halo+res[branchPosH:]

	    # ---------------------
	    if(useLo and (1<=counter_halo<=noofc)):
	        print("LOG: using lo")
	        # FIXME
	        #self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (counter_halo - 1))] + \
	        #                plugHalogen + self.output_lo2_2.text()[(4 * (counter_halo)):])
	        #self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (counter_halo - 1))] + \
	        #    " ╵  " + self.output_lo1_2.text()[(4 * (counter_halo)):])
	    elif(useHi and (1<=counter_halo<=noofc)):
	        print("LOG: using hi")
	        #self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (counter_halo - 1))] + \
	        #            plugHalogen + self.output_hi2_2.text()[(4 * (counter_halo)):])
	        #self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (counter_halo - 1))] + \
	        #    " ╷  " + self.output_hi1_2.text()[(4 * (counter_halo)):])
	    else:
	        ans ="ERROR: An unhandled error occured. #101"
	        print(ans)


	counterX = 1
	for i in zip(numbranch, branch):
	    nooc00 = res.count("C")

	    print("LOG:", branch, "+ RAW")
	    branch00 = branch[counterX-1]
	    print("LOG:", branch00, "+ COOKED")
	    if(branch00 == "methyl"):
	        branchConv = branchesList[0]
	    elif(branch00 == "ethyl"):
	        branchConv = branchesList[1]
	    elif(branch00 == "propyl"):
	        branchConv = branchesList[2]
	    elif(branch00 == "butyl"):
	        branchConv = branchesList[3]
	    elif(branch00 == "pentyl"):
	        branchConv = branchesList[4]
	    elif(branch00 == "hexyl"):
	        branchConv = branchesList[5]
	    else:
	        branchConv = "Longer Carbon chain"
	    spac = " "
	    print("LOG: i[0]=",i[0])
	    if(i[0]== 1) or (i[0]==nooc00):
	        msg = "Error! Cannot place groups at terminal carbon molecules"
	        res = msg
	        print(msg)
	        break
	    print("LOG: res = ", res)
	    branchPos = i[0]*4
	    theAlterer = res[(branchPos-4):branchPos]
	    print("LOG: theAlterer = ", theAlterer)
	    nooh = theAlterer[1:]
	    print("LOG: nooh=", nooh)
	    if(nooh[0]=="C"):
	        msg = "ERROR: Carbon valency of 4 is completely utilized."
	        print(msg)
	        res = msg
	        return res

	    elif(nooh[0]=="H"):
	        print("LOG: Detected H",nooh[1])
	        if(nooh[1]):

	            print("LOG: Detected Numeric value for H")
	            if theAlterer[2]=="₂":
	                tmpHolder = "₁"
	            elif theAlterer[2]=="₃":
	                tmpHolder = "₂"
	            elif theAlterer[2]=="₁":
	                tmpHolder = "₀"
	            elif theAlterer[2]=="₀":
	                msg = "ERROR: Carbon valency of 4 is completely utilized."
	                print(msg)
	                res = msg
	                return res
	            else:
	                msg = "ERROR: An unhandled error occured. Sorry. Report immediately to github.com/srevinsaju/carbonic/issues to refine this error"
	                print(msg)
	                res = msg
	                return res
	            # theAlterer = theAlterer[:2]+str(int(theAlterer[2])-1)+theAlterer[3:]
	            theAlterer = theAlterer[:2]+tmpHolder+theAlterer[3:]
	            theAlterer  = theAlterer.replace("CH₀"," C ")
	        else:
	            print(msg)
	            res = msg
	            return res
	    res = res[:(branchPos-4)]+theAlterer+res[branchPos:]


	    print("LOG: i", i)
	    # FIXME
	    #lo1Hold = self.output_lo1.text()
	    #hi1Hold = self.output_hi1.text()
	    lo_contains = False
	    hi_contains = False
	    for j in lo1Hold:
	        if(j==" "):
	            continue
	        else:
	            lo_contains = True
	    for k in hi1Hold:
	        if(k==" "):
	            continue
	        else:
	            hi_contains = True
	    if (hi_contains and lo_contains):
	        print("WARNING: Lets wait for it")
	        if(counterX%2==0):
	            print("LOG: neither1")
	            # FIXME
	            """
	            self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
	                    " \  " + self.output_lo1.text()[(4 * (i[0])):])
	            self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
	                    "  \ " + self.output_lo2.text()[(4 * (i[0])):])
	            self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + \
	                (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
				"""

	            pass
	        elif(counterX%2==1):
	            print("LOG: neither2")
	            # FIXME
	            """
	            self.output_hi2.setText(self.output_hi2.text()[:(4 * (i[0] - 1))] + \
	                    "  / " + self.output_hi2.text()[(4 * (i[0])):])
	            self.output_hi1.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + \
	                    " /  " + self.output_hi1.text()[(4 * (i[0])):])
	            self.output_hi3.setText(self.output_hi3.text()[:(4 * (i[0] - 1))] + \
	                (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
	            """
	            pass
	    elif hi_contains:
	        print("LOG: hi_contains")
	        print("LOG: branchCOnv:", branchConv)
	        print("LOG: i[0]", i[0])
	        # FIXME
	        """
	        self.output_lo1.setText(" "*len(res))
	        self.output_lo2.setText(" "*len(res))
	        self.output_lo3.setText(" "*len(res))

	        self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
	                " \  " + self.output_lo1.text()[(4 * (i[0])):])
	        self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
	                "  \ " + self.output_lo2.text()[(4 * (i[0])):])
	        self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + " " +\
	                (" "*(len(branchConv)//2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
			"""

	        pass
	    elif lo_contains:
	        print("LOG: lo_contains")
	        # FIXME
	        """
	        self.output_hi1.setText(" "*len(res))
	        self.output_hi2.setText(" "*len(res))
	        self.output_hi3.setText(" "*len(res))
	        self.output_hi2.setText(self.output_hi2.text()[:(4 * (i[0] - 1))] + \
	                "  / " + self.output_hi2.text()[(4 * (i[0])):])
	        self.output_hi1.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + \
	                " /  " + self.output_hi1.text()[(4 * (i[0])):])
	        self.output_hi3.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + "  " +\
	                (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
	        """
	    else:
	        print("LOG: neither_contains")
	        if(counterX%2==0):
	            print("LOG: neither1")
	            # FIXME
	            """
	            self.output_lo1.setText(" "*len(res))
	            self.output_lo2.setText(" "*len(res))
	            self.output_lo3.setText(" "*len(res))
	            self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
	                    " \  " + self.output_lo1.text()[(4 * (i[0])):])
	            self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
	                    "  \ " + self.output_lo2.text()[(4 * (i[0])):])
	            self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + \
	                (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
				"""

	            pass
	        elif(counterX%2==1):
	            print("LOG: neither2")
	            # FIXME
	            """
	            self.output_hi1.setText(" "*len(res))
	            self.output_hi2.setText(" "*len(res))
	            self.output_hi3.setText(" "*len(res))
	            self.output_hi2.setText(self.output_hi2.text()[:(4 * (i[0] - 1))] + \
	                    "  / " + self.output_hi2.text()[(4 * (i[0])):])
	            self.output_hi1.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + \
	                    " /  " + self.output_hi1.text()[(4 * (i[0])):])
	            self.output_hi3.setText(self.output_hi3.text()[:(4 * (i[0] - 1))] + "  " +\
	                (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
	            pass
	            """

	        pass
	    counterX+=1
	    """
	    if(i[0] == int(ceil((nooc00/2) ))):

	        print("LOG : DIVIDER IS CENTERED ")
	        self.output_lo1.setText("\\")
	        self.output_lo2.setText(" "+ spac*(len(branchConv)) +branchConv)

	    elif(i[0] > int(ceil((nooc00/2) ))):
	        self.output_lo2.setText(spac + spac*(len(branchConv)) +spac*(8*(i[0]-int(ceil((nooc00/2)))))+branchConv)
	        self.output_lo1.setText(spac*8*(i[0]-int(ceil((nooc00/2))))+"\\")
	    elif(i[0] < int(ceil((nooc00/2) ))):
	        self.output_lo2.setText(spac + spac*(len(branchConv)) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-i[0])))
	        self.output_lo1.setText("\\" + spac*(8*(int(ceil((nooc00/2)))-i[0])))


	elif(counterX%2==0):
	    if(i[0] == int(ceil((nooc00/2) ))):

	        print("LOG : DIVIDER IS CENTERED ")
	        self.output_hi1.setText("/")
	        self.output_hi2.setText(" "+ spac*(len(branchConv)) +branchConv)

	    elif(i[0] > int(ceil((nooc00/2) ))):
	        self.output_hi2.setText(spac + spac*(len(branchConv)) +spac*(8*(i[0]-int(ceil((nooc00/2)))))+branchConv)
	        self.output_hi1.setText(spac*8*(i[0]-int(ceil((nooc00/2))))+"/")
	    elif(i[0] < int(ceil((nooc00/2) ))):
	        self.output_hi2.setText(spac + spac*(len(branchConv)) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-i[0])))
	        self.output_hi1.setText("/" + spac*(8*(int(ceil((nooc00/2)))-i[0])))self.output_hi2.setText(spac + spac*(len(branchConv)) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-i[0])))
	        self.output_hi1.setText("/" + spac*(8*(int(ceil((nooc00/2)))-i[0])))


	"""

	return res




