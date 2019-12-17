#!/usr/bin/env python3
"""
carbonic on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC CORE AI
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic

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
import collections

print("""

carbonic on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC CORE AI
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

""")
class carbox:
    def __init__(self, bondorder=1, noofc=1, bondpos_chkBond=[2], numbranch=[], branch=[], benzylBool=False, haloIndexConv=[], haloGroupConv=[], **kwargs):
        self.bondOrder=bondorder
        self.noofc=noofc
        self.bondPos=bondpos_chkBond
        self.numbranch=numbranch
        self.branch = branch
        self.benzyl = benzylBool
        self.haloIndexConv = haloIndexConv
        self.haloBranchConv = haloGroupConv


def displax(resource):
    if type(resource) is str:
        print(resource)
    elif type(resource) is list:
        if len(resource) == 1:
            print(resource[0])
        else:
            print(resource[6],resource[5],resource[4],resource[0], resource[1], resource[2], resource[3],sep="\n")


# reusable data
TERMINAL = ["CH₃", "CH₂"]
BOND = ["CH₃-", "CH₂-", "CH₁=", "CH₁-", " C ≡"]
counter2 = 1
answer = ""
k = 0
RESULT = ""
NNNRESULT = ""
NNNNRESULT = ""



def convertor(raw_iupac):
    func = None
    raw_iupac = raw_iupac.strip()
    raw_iupac = raw_iupac.lower()
    cyclic = False
    benzeneChildBool = False
    addOnBranches = []
    addOnBranchesNum = []
    listOfAdditionalStuff = ["methyl", "ethyl", "propyl", "butyl", "pentyl", "hexyl"]
    BenzeneChild = ["benz", "naphthal", "anthrac", "chrys", "pyrene", "corannulene", "coronene", "hexahelic"]
    count = 1
    print(raw_iupac.find("["), " is INDEX")
    if((raw_iupac.find("["))!=-1):

        for i in listOfAdditionalStuff:
            if(raw_iupac.find(i)==-1):
                print("LOG: passed", i)
                count+=1
                continue
                # continue : removed because repeated methyl or ethyl groups are not considered
            else:
                while raw_iupac.find(i)!=1:
                    print("found ", i)
                    indic = raw_iupac.find(i)
                    try:
                        addOnNum = int(raw_iupac[raw_iupac.find("[")+1:indic-1])
                    except ValueError:

                        print("WARNING: Getting out of loop")
                        break

                    print("LOG : AddOnNum is ", addOnNum)
                    addOnBranchesNum.append(addOnNum)
                    addOnBranches.append(i)
                    raw_iupac=raw_iupac[(indic+len(i)+1):]

                    count+=1
                    print("LOG: raw_iupac:", raw_iupac)


    else:
        print("HOHO")
    print(raw_iupac)
    print("LOG: addOnBranchesNum = ", addOnBranchesNum)
    print("LOG: addOnBranches = ", addOnBranches)
    # for use in emergency :)
    tmpinp = raw_iupac
    # initialize bondpos_chkBond value to prevent NameError
    bondpos_chkBond = []

    # check if the given name has halogen names
    haloIndexConv = []
    haloGroupConv = []

    halogens = ["bromo", "fluoro", "iodo", "chloro"]
    for halogen in halogens:
        if raw_iupac.find(halogen)>-1:
            while raw_iupac.find(halogen)>-1:
                print("LOG: detected halogen", halogen)
                haloIndex = raw_iupac.find(halogen)
                if raw_iupac[haloIndex-1:haloIndex]=="-":
                    print("LOG: Found numeric value")
                    print("LOG: raw_iupac @ halo", raw_iupac)
                    if(raw_iupac[0]==","):
                        print("LOG: comma pased in halo section")
                        raw_iupac=raw_iupac[1:]
                        print("LOG: raw_iupac after comma @ halo", raw_iupac)
                        continue

                    else:
                        print("LOG: No comma in ", raw_iupac)
                    try:
                        print("LOG: raw_iupac[:haloIndex-1] is ", raw_iupac[:haloIndex-1])
                        haloIndexConv.append(int(raw_iupac[:haloIndex-1]))
                        haloGroupConv.append(halogen)
                        raw_iupac = raw_iupac[haloIndex+len(halogen):]
                        print("LOG: raw_iupac is", raw_iupac)
                    except ValueError:
                        print("LOG: trying once again")
                        try:
                            print("LOG: raw_iupac[:haloIndex-2] is ", raw_iupac[:haloIndex-2])
                            haloIndexConv.append(int(raw_iupac[:haloIndex-2]))
                            haloGroupConv.append(halogen)
                            raw_iupac = raw_iupac[haloIndex-1+len(halogen):]
                            print("LOG: raw_iupac is", raw_iupac)
                        except ValueError:
                            try:
                                print("LOG: raw_iupac[:haloIndex-3] is ", raw_iupac[:haloIndex-3])
                                haloIndexConv.append(int(raw_iupac[:haloIndex-3]))
                                haloGroupConv.append(halogen)
                                raw_iupac = raw_iupac[haloIndex-2+len(halogen):]
                                print("LOG: raw_iupac is", raw_iupac)
                            except ValueError:
                                print("LOG: Really sorry about that")
                                break
                else:
                    print("LOG: No halo value found ")
                    haloIndexConv.append(1)
                    haloGroupConv.append(halogen)
                    raw_iupac = raw_iupac[haloIndex+len(halogen):]
                    print("LOG: raw_iupac is", raw_iupac)
                    break

        else:
            continue

    print("LOG: haloIndexConv:", haloIndexConv)
    # read the #- value of the IUPAC name
    for i in tmpinp:
        if(raw_iupac[0].isalpha()):
            print("LOG: isAlpha")
            break
        try:
            if(raw_iupac[0].isnumeric):
                bondpos_chkBond.append(raw_iupac[0])
                raw_iupac = raw_iupac[1:]
            else:
                print("LOG: No",i)
        except IndexError:
            print("No index, passing")
        try:
            if(raw_iupac[0]==","):
                raw_iupac = raw_iupac[1:]
        except IndexError:
            print("No Index, passing")
        try:
            if(raw_iupac[0] == "-"):
                raw_iupac = raw_iupac[1:]
                break
            else:
                print("NONO", i)

        except IndexError:
            print("No Index, passing")

    # Check the carbon compound is alkane, alkene or alkyne
    if(raw_iupac.endswith("ane")):
        if(raw_iupac.startswith("cyclo")):
            print("LOG: Detected Cyclic Carbon Compounds")
            bond_int = 4
            raw_iupac = raw_iupac[5:]
            print("LOG: Logging Cyclic raw_iupac=", raw_iupac)
            cyclic = True
        else:
            bond_int = 1
            print("LOG: alkane")
        restOfInp = raw_iupac.partition("ane")
    elif(raw_iupac.endswith("ene")):
        print("alken")

        for i in BenzeneChild:
            if (raw_iupac.startswith(str(i))):
                childOfBenzeneType = i
                benzeneChildBool = True
                break

        bond_int = 2
        restOfInp = raw_iupac.partition("ene")

    elif(raw_iupac.endswith("yne")):
        bond_int = 3
        print("LOG: alkyne")
        restOfInp = raw_iupac.partition("yne")
    elif(raw_iupac.endswith("one")):
        bond_int = 5
        print("LOG: Detected Ketone")
        restOfInp = raw_iupac.partition("one")
    elif(raw_iupac.endswith("oic acid")):
        bond_int = 7
        print("LOG: Detected Carboxylic Acid")
        restOfInp = raw_iupac.partition("oic acid")
    elif(raw_iupac.endswith("ol")):
        bond_int = 8
        print("LOG: Detected Alcohol")
        restOfInp = raw_iupac.partition("ol")
    elif(raw_iupac.endswith("al")):
        bond_int = 6
        print("LOG: Detected Aldehyde")
        restOfInp = raw_iupac.partition("al")

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

    # END OF CONVERTOR FUNCTION

    return carbox(bond_int, noofc0, bondpos_chkBond, addOnBranchesNum, addOnBranches, benzeneChildBool, haloIndexConv, haloGroupConv)

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


        #restxt = chkBond(carbox(bondorder, noofc, bondpos_chkBond, numbranch, branch, benzylBool, haloIndexConv, haloGroupConv))

        #leng = len(restxt); print(restext)

def alkenebond(bondpos=1, answer_src = "" ):
    # Check the inputted value,
    # Check if bondpos value and answer_src is valid

    answer = answer_src
    print(answer+"ANS")
    answer = answer[:(4 * (bondpos - 1))] + \
                                BOND[2] + answer[(4 * (bondpos)):]
    answer = answer.replace("=CH₂-", "=CH₁-")
    answer = answer.replace("=CH₁=", "= C =")
    print(answer)
    noofcc = answer.count("C")

def alkynebond(x, bondpos):

    answer = x
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


def alkane(noofc):

    if (noofc == 1):

        answer = "CH₄"
    else:

        answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
    print(answer)
    
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

    return [answer]

def aldehyde(noofc, bondpos_chkBond):
    if not bondpos_chkBond:
        bondpos_chkBond = [noofc-1]
        ans = alkane(noofc-1)
    else:

        ans = alkene(noofc-1, bondpos_chkBond, True)

    branchConv_aldehyde = "CHO"
    spac = " "
    rndcnt = 1
    try:
        trier = lo1Hold
    except NameError:
        lo2Hold = len(ans)*spac
        lo1Hold = len(ans)*spac
        lo3Hold = len(ans)*spac
    
    try:
        trier = hi1Hold
    except:
        hi1Hold = len(ans)*spac
        hi2Hold = len(ans)*spac
        hi3Hold = len(ans)*spac

    for i in bondpos_chkBond:
        nooc00 = noofc-1
        bondpos = int(i)
        print("LOG: nooc00", nooc00)

        print(bondpos, '=', noofc)
        if(bondpos==1):
            ans = "CHO-CH₂-"+ans[4:]
            continue
        elif (bondpos==noofc-1):
            ans = ans[:-3]+"CH₂-CHO"
            continue

        if((bondpos%2==0)and (1<bondpos<noofc-1)):
            print("LOG: using lo")
            lo2Hold = lo2Hold[:(4 * (bondpos - 1))] + "CHO " + lo2Hold[(4 * (bondpos)):]
            lo1Hold = lo1Hold[:(4 * (bondpos - 1))] + " ╵  " + lo1Hold[(4 * (bondpos)):]
        elif((bondpos%2==1)and (1<bondpos<noofc-1)):
            print("LOG: using hi")
            hi2Hold = hi2Hold[:(4 * (bondpos - 1))] + "CHO " + hi2Hold[(4 * (bondpos)):]
            hi1Hold = hi1Hold[:(4 * (bondpos - 1))] + " ╷  " + hi1Hold[(4 * (bondpos)):]
        else:
            print("ERROR: An unhandled error occured. #101")

    return [ans, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold]


def carboxylic(noofc, bondpos_chkBond):
    if not bondpos_chkBond:
        bondpos_chkBond = [1]
        ans = alkane(noofc)
    else:

        ans = alkene(noofc, bondpos_chkBond, True)

    spac = " "
    rndcnt = 1
    try:
        trier = lo1Hold
    except NameError:
        lo2Hold = len(ans)*spac
        lo1Hold = len(ans)*spac
        lo3Hold = len(ans)*spac

    try:
        trier = hi1Hold
    except:
        hi1Hold = len(ans)*spac
        hi2Hold = len(ans)*spac
        hi3Hold = len(ans)*spac
            

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
            ans = "CH3-COOH"
        else:
            ans = ans[:-3]+"-COOH"


    elif((bondpos%2==0)and (1<bondpos<noofc)):
        print("LOG: using lo")
        lo2Hold = lo2Hold[:(4 * (bondpos - 1))] + "COOH" + lo2Hold[(4 * (bondpos)):]
        lo1Hold = lo1Hold[:(4 * (bondpos - 1))] + " ╵  " + lo1Hold[(4 * (bondpos)):]
    elif((bondpos%2==1)and (1<bondpos<noofc)):
        print("LOG: using hi")
        hi2Hold = hi2Hold[:(4 * (bondpos - 1))] + "COOH" + hi2Hold[(4 * (bondpos)):]
        hi1Hold = hi1Hold[:(4 * (bondpos - 1))] + " ╷  " + hi1Hold[(4 * (bondpos)):]
    else:
        ans ="ERROR: An unhandled error occured. #101"
        print(ans)

    return [ans, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold]


def alcohol(noofc, bondpos_chkBond):
    if not bondpos_chkBond:
        bondpos_chkBond = [1]
        ans = alkane(noofc)
    else:

        ans = alkene(noofc, bondpos_chkBond, True)

    spac = " "
    rndcnt = 1
    try:
        trier = lo1Hold
    except NameError:
        lo2Hold = len(ans)*spac
        lo1Hold = len(ans)*spac
        lo3Hold = len(ans)*spac
        
    try:
        trier = hi1Hold
    except NameError:
        hi2Hold = len(ans)*spac
        hi1Hold = len(ans)*spac
        hi3Hold = len(ans)*spac
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
            try:
                trier = lo1Hold
            except NameError:
                lo2Hold = len(ans)*spac
                lo1Hold = len(ans)*spac
                lo3Hold = len(ans)*spac
                
            try:
                trier = hi1Hold
            except NameError:
                hi2Hold = len(ans)*spac
                hi1Hold = len(ans)*spac
                hi3Hold = len(ans)*spac

    elif((bondpos%2==0)and (1<bondpos<noofc)):
        print("LOG: using lo")
        lo2Hold = lo2Hold[:(4 * (bondpos - 1))] + " OH " + lo2Hold[(4 * (bondpos)):]
        lo1Hold = lo1Hold[:(4 * (bondpos - 1))] + " ╵  " + lo1Hold[(4 * (bondpos)):]
    elif((bondpos%2==1)and (1<bondpos<noofc)):
        print("LOG: using hi")
        hi2Hold = hi2Hold[:(4 * (bondpos - 1))] + " OH " + hi2Hold[(4 * (bondpos)):]
        hi1Hold = hi1Hold[:(4 * (bondpos - 1))] + " ╷  " + hi1Hold[(4 * (bondpos)):]
    else:
        ans ="ERROR: An unhandled error occured. #101"
        print(ans)
    return [ans, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold]


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

    return answer

def cyclic(noofc=3):
    print("LOG: Entered chkbond function with Cyclic entry")
    print("LOG: noofc = ", noofc)
    # check if nmber of carbon is even or not
    if(noofc%2==0):
        print("LOG: Number of carbons are even")
        if(noofc>3):
            print("LOG: condition is true [001]")
            n = (noofc-2)//2
            holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
            hi2Hold = holder # text box 1
            hi1Hold = "/"+" "*len(holder)+"\\" # text box 2
            lo1Hold = "\\"+" "*len(holder)+"/"
            lo2Hold = holder # text box 4
            res = TERMINAL[1] + " "*(len(holder)) + TERMINAL[1]
            return [res, lo1Hold, lo2Hold, " ", hi1Hold, hi2Hold, " "]

        else:
            msg = "ERROR: An unhandled error occured"
            print(msg)
            return [msg]
    else:

        print("LOG: Number of carbons are odd")
        if(noofc ==3):
            print("LOG: Detected cyclopropane")

            hi2Hold  = TERMINAL[1]
            hi1Hold = "/   \\"
            res =  TERMINAL[1]+"-"+TERMINAL[1]
            lo1Hold = " "
            lo2Hold = " "
            return [res, hi2Hold, hi1Hold, lo1Hold, lo2Hold]
        else:
            print("LOG: detected noofc ", noofc)
            print("LOG: condition is false, but odd [002]")
            n = (noofc-1)//2
            holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
            hi2Hold = holder # text box 1
            hi1Hold = "/"+" "*(len(holder)-2)+"╷"+" " # text box 2
            lo1Hold = "\\"+" "*(len(holder)-2)+"╵"+" " # text box 3
            lo2Hold = holder # text box 4
            res = " " + TERMINAL[1] + " "*(len(holder)-2) + "|" +"    "
            return [res, hi2Hold, hi1Hold, lo1Hold, lo2Hold]


def chkBond(carbox_struct):
    # retrieve data from carbox struvt
    bondorder = carbox_struct.bondOrder
    noofc=carbox_struct.noofc
    bondpos_chkBond= carbox_struct.bondPos
    numbranch=carbox_struct.numbranch
    branch=carbox_struct.branch
    benzylBool=carbox_struct.benzyl
    haloIndexConv=carbox_struct.haloIndexConv
    haloGroupConv=carbox_struct.haloBranchConv
    lo_contains = False
    hi_contains = False
    branchesList = ["CH₃ ", "CH₂-CH₃ ", "CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₂-CH₃ "]
    counterX = 1
    if(benzylBool):
        res =  cyclic(6)[0]
        noofc = 6
        n = (noofc-2)//2
        holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
        # FIXME :::::::: __>
        hi2Hold = holder
        hi1Hold = "╔"+" "*len(holder)+"╗" # text box 2
        lo1Hold = "\\"+" "*len(holder)+"/" # text box 3
        lo2Hold = holder.replace("-", "=") # text box 4
        return [res, lo1Hold, lo2Hold, " ", hi1Hold, hi2Hold, " "]

    if (bondorder == 1):
        res = alkane(noofc)
    elif (bondorder == 2):
        res = alkene(noofc, bondpos_chkBond)

    elif (bondorder == 3):
        res = alkyne(noofc, bondpos_chkBond)
    elif (bondorder ==4 ):
        res = cyclic(noofc) # FIXED add support for benzene and children
        return res
    elif bondorder == 5:
        res = ketone(noofc, bondpos_chkBond)
        return res
    elif bondorder == 6:
        res = aldehyde(noofc, bondpos_chkBond)
        return res
    elif bondorder == 7:
        res = carboxylic(noofc, bondpos_chkBond)
        return res
    elif bondorder == 8:
        print("LOG: Alcohol ++++++++++++++")
        res = alcohol(noofc, bondpos_chkBond)
        return res

    else:
        res = ["Your functional group might not be supporte by " + \
        "carbonic core. Create an issue requesting feature, PRs, Bye Bye!"]
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
                    if(lo2Hold[(halogenzip[0])*4:(halogenzip[0]+1)*4].isspace()):
                        useLo = True
                    elif(hi2Hold[(halogenzip[0])*4:(halogenzip[0]+1)*4]).isspace():
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
            lo2Hold = lo2Hold[:(4 * (counter_halo - 1))] + \
                            plugHalogen + lo2Hold[(4 * (counter_halo)):]
            lo1Hold = lo1Hold[:(4 * (counter_halo - 1))] + \
                " ╵  " + lo1Hold[(4 * (counter_halo)):]
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
        try:
            trier = lo1Hold
        except NameError:
            lo1Hold = " "*len(res)
            lo2Hold = " "*len(res)
            lo3Hold = " "*len(res)
        try:
            trier = hi1Hold
        except NameError:
            hi1Hold = " "*len(res)
            hi2Hold = " "*len(res)
            hi3Hold = " "*len(res)

        if(lo1Hold.isspace()):
            lo_contains = False
        else:
            lo_contains = True
        if(hi1Hold.isspace()):
            hi_contains = False
        else:
            hi_contains = True

        if (hi_contains and lo_contains):
            print("WARNING: Lets wait for it")
            if(counterX%2==0):
                print("LOG: neither1")
                # FIXME

                lo1Hold = lo1Hold[:(4 * (i[0] - 1))] + " \  " + lo1Hold[(4 * (i[0])):]
                lo2Hold = lo2Hold[:(4 * (i[0] - 1))] + "  \ " + lo2Hold[(4 * (i[0])):]
                lo3Hold = lo3Hold[:(4 * (i[0] - 1))] + (" "*ceil(len(branchConv)/2))+branchConv + lo3Hold[(4 * (i[0])+(len(branchConv)-4)):]


                pass
            elif(counterX%2==1):

                print("LOG: neither2")
                # FIXME

                hi1Hold = hi1Hold[:(4 * (i[0] - 1))] + "  / " + hi1Hold[(4 * (i[0])):]
                hi2Hold = hi2Hold[:(4 * (i[0] - 1))] + " /  " + hi2Hold[(4 * (i[0])):]
                hi3Hold = hi3Hold[:(4 * (i[0] - 1))] + (" "*ceil(len(branchConv)/2))+branchConv + hi3Hold[(4 * (i[0])+(len(branchConv)-4)):]
                print("HHH", hi1Hold, hi2Hold, hi3Hold)
                hi_contains = True
                pass
        elif hi_contains:
            print("LOG: hi_contains")
            print("LOG: branchCOnv:", branchConv)
            print("LOG: i[0]", i[0])
            # FIXME
            try:
                trier = lo1Hold
            except NameError:
                lo1Hold = " "*len(res)
                lo2Hold = " "*len(res)
                lo3Hold = " "*len(res)
            lo1Hold = lo1Hold[:(4 * (i[0] - 1))] + " \  " + lo1Hold[(4 * (i[0])):]
            lo2Hold = lo2Hold[:(4 * (i[0] - 1))] + "  \ " + lo2Hold[(4 * (i[0])):]
            lo3Hold = lo3Hold[:(4 * (i[0] - 1))] + (" "*ceil(len(branchConv)/2))+branchConv + lo3Hold[(4 * (i[0])+(len(branchConv)-4)):]
            lo_contains = True

            pass
        elif lo_contains:
            print("LOG: lo_contains")
            # FIXME
            try:
                trier = hi1Hold
            except NameError:
                hi1Hold = " "*len(res)
                hi2Hold = " "*len(res)
                hi3Hold = " "*len(res)
            hi1Hold = hi1Hold[:(4 * (i[0] - 1))] + "  / " + hi1Hold[(4 * (i[0])):]
            hi2Hold = hi2Hold[:(4 * (i[0] - 1))] + " /  " + hi2Hold[(4 * (i[0])):]
            hi3Hold = hi3Hold[:(4 * (i[0] - 1))] + "  " + (" "*ceil(len(branchConv)/2))+branchConv + hi3Hold[(4 * (i[0])+(len(branchConv)-4)):]
            hi_contains = True

        else:
            print("LOG: neither_contains")
            if(counterX%2==0):
                print("LOG: neither1")
                # FIXME
                try:
                    trier = lo1Hold
                except NameError:
                    lo1Hold = " "*len(res)
                    lo2Hold = " "*len(res)
                    lo3Hold = " "*len(res)
                lo1Hold = lo1Hold[:(4 * (i[0] - 1))] + " \  " + lo1Hold[(4 * (i[0])):]
                lo2Hold = lo2Hold[:(4 * (i[0] - 1))] + "  \ " + lo2Hold[(4 * (i[0])):]
                lo3Hold = lo3Hold[:(4 * (i[0] - 1))] + (" "*ceil(len(branchConv)/2))+branchConv + lo3Hold[(4 * (i[0])+(len(branchConv)-4)):]

                pass
            elif(counterX%2==1):
                print("LOG: neither2")
                # FIXME
                hi3Hold = hi3Hold[:(4 * (i[0] - 1))] + "  " + (" "*ceil(len(branchConv)/2))+branchConv + hi3Hold[(4 * (i[0])+(len(branchConv)-4)):]
                hi2Hold = hi2Hold[:(4 * (i[0] - 1))] + "  / " + hi2Hold[(4 * (i[0])):]
                hi1Hold = hi1Hold[:(4 * (i[0] - 1))] + " /  " + hi1Hold[(4 * (i[0])):]


                print("HHH", hi1Hold, hi2Hold, hi3Hold)
                pass
            pass

        counterX+=1
        continue
    else:
        try:
            return [res, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold]
        except (NameError, AttributeError):
            return [res]
    try:
        return [res, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold]
    except (NameError, AttributeError):
        return [res]
