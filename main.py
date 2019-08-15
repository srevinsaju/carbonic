"""
carbonic on github by @srevinsaju

THIS IS MAIN MODULE FOR GUI INTEGRATION PORT.

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

"""
# imports
from mainui import Ui_Dialog
import os
from math import ceil
import sys
import time
import webbrowser
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


# reusable data
TERMINAL = ["CH₃", "CH₂"]
BOND = ["CH₃-", "CH₂-", "CH₁=", "CH₁-", " C ≡"]
counter2 = 1
answer = ""
k = 0
RESULT = ""
NNNRESULT = ""
NNNNRESULT = ""

# noofc = int(input("Enter number of carbon atoms ---> "))
# bonds = int(input("Enter  1: single bond 2: double bond 3: triple bond  ---> "))
"""
def convertor(inp):
    inp = inp.strip()
    inp = inp.lowercase()
    tmpinp = inp
    
    if(inp.endswith("ane")):
        bond_int = 1
    elif(inp.endswith("ene")):
        bond_int = 2
    elif(inp.endswith("yne")):
        bond_int = 3
    else:
        bond_int = 0
        print("ERROR: INVALID")
    
    """

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
    # initialize bond00 value to prevent NameError
    bond00 = []
    haloIndexConv = []
    haloGroupConv = []
    # check if the given name has halogen names
    halogens = ["bromo", "fluoro", "iodo", "chloro"]
    for halogen in halogens:
        if inp.find(halogen)>-1:
            while inp.find(halogen)>-1:
                print("LOG: detected halogen", halogen)
                haloIndex = inp.find(halogen)
                if inp[haloIndex-1:haloIndex]=="-":
                    print("LOG: Found numeric value")
                    if(inp[0]==","):
                        inp=inp[1:]
                    try:
                        print("LOG: inp[:haloIndex-2] is ", inp[:haloIndex-1])
                        haloIndexConv.append(int(inp[:haloIndex-1]))
                        haloGroupConv.append(halogen)
                        inp = inp[haloIndex+len(halogen):]
                        print("LOG: inp is", inp)
                    except ValueError:
                        print("ERROR: Not a numeric value.")
                else:
                    print("LOG: No halo value found ")
                
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
                bond00.append(inp[0])
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
    
    return noofc0, bond_int, bond00, addOnBranchesNum, addOnBranches, benzeneChildBool
    
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


class MyAppv(Ui_Dialog):
    def __init__(self, Dialog):
        super(MyAppv, self).__init__()
        Ui_Dialog.__init__(self)
        self.setupUi(Dialog)
        print(self)
        # self.bondui.sliderChange.connect()
        self.pushButton.pressed.connect(self.compute)
        self.pushButton_2.pressed.connect(self.quitme)
        self.abt.pressed.connect(self.openme)
        self.abt_2.pressed.connect(self.opengit)
        self.placer.sliderMoved.connect(self.sliderValueChange)
        self.placer.sliderReleased.connect(self.sliderValueChange)
        self.radioButton.pressed.connect(self.radio1)
        self.radioButton_2.pressed.connect(self.radio2)
        self.bondui.sliderMoved.connect(self.bondSliderValueChange)
        self.bondui.sliderReleased.connect(self.bondSliderValueChange)
        self.placertxt.setText(str(self.placer.value()))
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.pressed.connect(self.bondchk)
        self.pushButton_4.pressed.connect(self.transalate)

    def openme(self):
        webbrowser.open("https://srevinsaju.wixsite.com/srevinsaju")
    def opengit(self):
        webbrowser.open("https://srevinsaju.github.io/carbonic/")
    def transalate(self):
        # clear all text boxes to prevent confilict
        self.output.setText("")
        self.output_lo2.setText("")
        self.output_hi2.setText("")
        self.output_hi1.setText("")
        self.output_lo1.setText("")
        self.output_hi3.setText("")
        self.output_lo3.setText("")
        self.output_lo2_2.setText("")
        self.output_hi2_2.setText("")
        self.output_hi1_2.setText("")
        self.output_lo1_2.setText("")
        
        inpu = self.textEdit.text()
        noofc, bondo, bond01, numbranch, branch, benzylBool = convertor(inpu)
        self.compute(noofc, bondo, bond01, numbranch, branch, benzylBool)
        

    def radio1(self):
        self.textEdit.setEnabled(False)
        self.radioButton_2.setChecked(False)
        self.radioButton.setChecked(True)
        self.nooc.setEnabled(True)
        self.bondui.setEnabled(True)
        self.placer.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_4.setEnabled(False)
        
    def radio2(self):
        self.textEdit.setEnabled(True)
        self.radioButton_2.setChecked(True)
        self.radioButton.setChecked(False)
        self.nooc.setEnabled(False)
        self.bondui.setEnabled(False)
        self.placer.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        
    def switchoff(self):
        print(self.radioButton.isChecked())
        print(self.radioButton_2.isChecked())
        if(self.radioButton.isChecked()):
            self.textEdit.setEnabled(False)
            self.radioButton_2.setChecked(False)
            self.radioButton.setChecked(True)
            self.nooc.setEnabled(True)
            self.bondui.setEnabled(True)
            self.placer.setEnabled(True)
            
        elif(self.radioButton_2.isChecked()):
            self.textEdit.setEnabled(True)
            self.radioButton_2.setChecked(True)
            self.radioButton.setChecked(False)
            self.nooc.setEnabled(False)
            self.bondui.setEnabled(False)
            self.placer.setEnabled(False)
            
            
    def quitme(self):
        sys.exit(0)

    def bondSliderValueChange(self):
        if(self.bondui.value()==1):
            smCarbon = "ALKANE"
        elif(self.bondui.value()==2):
            smCarbon = "ALKENE"
        elif(self.bondui.value() == 3):
            smCarbon = "ALKYNE"
        else:
            smCarbon = "NONE"
        self.bondtxt.setText(str(smCarbon))
    
    def sliderValueChange(self):
        self.placertxt.setText(str(self.placer.value()))
    def bondchk(self):
        print("CHECKING BOND")
        if(self.bondui.value()==2):
            self.alkenebond()
        elif(self.bondui.value()==3):
            self.alkynebond()
        else:
            print("ERR")

    def alkenebond(self):
        counter = self.placer.value()
        answer = self.output.text()
        print(answer+"ANS")
        answer = answer[:(4 * (counter - 1))] + \
                            BOND[2] + answer[(4 * (counter)):]
        answer = answer.replace("=CH₂-", "=CH₁-")
        answer = answer.replace("=CH₁=", "= C =")
        print(answer)
        noofcc = answer.count("C")
        self.output.setText(answer)
        self.placer.setMinimum(int(counter)+1)
        self.placer.setValue(int(counter)+1)
        self.placertxt.setText(str(counter+1))
        if(counter+1>noofcc - 2):
            print("Disabling Slider")
            self.placer.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        else:
            self.placer.setMaximum(noofcc - 2)

    def alkynebond(self):
        counter = self.placer.value()
        answer = self.output.text()
        print(answer+"ANS")

        # -------------------------------------
        answer = answer[:(4 * (counter - 1))] + \
                            BOND[4] + answer[(4 * (counter)):]
        answer = answer.replace("≡CH₂-", "≡ C -")

        if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH₂-"):
            print("≡")
            answer = answer[:(4 * (counter - 1) + 3)] + \
                "≡ C -" + answer[(4 * (counter - 1) + 8):]

        print(answer)
        # -------------------------------------
        noofcc = answer.count("C")
        self.output.setText(answer)

        self.placer.setMinimum(int(counter)+2)
        self.placer.setValue(int(counter)+2)
        self.placertxt.setText(str(counter+2))
        if(counter+2>noofcc - 2):
            print("Disabling Slider")
            self.placer.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        else:
            self.placer.setMaximum(noofcc - 2)

    def compute(self, noc=None, boc=None, bond00=None, numbranch=[], branch=[], benzylBool=False):
        if(noc ==None):
            noofc = self.nooc.value()
        else:
            noofc = noc
        if(boc == None):
            bonds = self.bondui.value()
        else:
            bonds=boc
            
        print("LOG: noofc=", noofc)
        print("LOG: bonds=", bonds)
        print("LOG: bond00=", bond00)
        restxt = self.chkBond(bonds, noofc, bond00, numbranch, branch, benzylBool)
        print("LOG: restext placeholder:", restxt)
        leng = len(restxt)
        if(leng>=50):

            self.output.setFont(QtGui.QFont('Consolas', 10, weight=QtGui.QFont.Bold))
        else:
            self.output.setFont(QtGui.QFont('Consolas', 14, weight=QtGui.QFont.Bold))
        self.output.setText(restxt)

    def alkane(self, noofc):
        self.pushButton_3.setEnabled(False)
        if (noofc == 1):

            answer = "CH₄"
        else:

            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
        print(answer)
        return answer
    
    def ketone(self, noofc, bond00):
        if(bond00 == []):
            bond00 =[2]
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
            for i in bond00:
                    
                counter = int(i)
                print("LOG:", counter, '=', noofc)
                if((counter==noofc)or(counter==1)):
                    answer = "Error! Ketone functional group cannot be placed at the terminal ends of a carbon structure."
                    break
                
                answer = answer[:(4 * (counter - 1))] + \
                                "CO -" + answer[(4 * (counter)):]

                answer = answer.replace("=CH₂-", "=CH₁-")
                answer = answer.replace("=CH₁=", "= C =")
                print(answer)
            
            self.placer.setMinimum(2)
            self.placer.setMaximum(noofc - 2)
            self.placer.setEnabled(True)
            self.pushButton_3.setEnabled(True)
        return answer
    
    def aldehyde(self, noofc, bond00):
        if not bond00:
            bond00 = [noofc-1]
            ans = self.alkane(noofc-1)
        else:
             
            ans = self.alkene(noofc-1, bond00, True)
            
        
        
        branchConv_aldehyde = "CHO"
        spac = " "
        rndcnt = 1
        self.output_lo2_2.setText(len(ans)*spac)
        self.output_lo1_2.setText(len(ans)*spac)
        self.output_hi2_2.setText(len(ans)*spac)
        self.output_hi1_2.setText(len(ans)*spac)
        for i in bond00:
            nooc00 = noofc-1
            counter = int(i)
            print("LOG: nooc00", nooc00)
           
            print(counter, '=', noofc)
            if(counter==1):
                ans = "CHO-CH₂-"+ans[4:]
                self.output_lo2_2.setText(len(ans)*spac)
                self.output_lo1_2.setText(len(ans)*spac)
                self.output_hi2_2.setText(len(ans)*spac)
                self.output_hi1_2.setText(len(ans)*spac)
                continue
            elif (counter==noofc-1):
                ans = ans[:-3]+"CH₂-CHO"
                self.output_lo2_2.setText(len(ans)*spac)
                self.output_lo1_2.setText(len(ans)*spac)
                self.output_hi2_2.setText(len(ans)*spac)
                self.output_hi1_2.setText(len(ans)*spac)
                continue
            
            if((counter%2==0)and (1<counter<noofc-1)):
                print("LOG: using lo")
                self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (counter - 1))] + \
                                "CHO " + self.output_lo2_2.text()[(4 * (counter)):])
                self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (counter - 1))] + \
                    " ╵  " + self.output_lo1_2.text()[(4 * (counter)):])
            elif((counter%2==1)and (1<counter<noofc-1)):
                print("LOG: using hi")
                self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (counter - 1))] + \
                            "CHO " + self.output_hi2_2.text()[(4 * (counter)):])
                self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (counter - 1))] + \
                    " ╷  " + self.output_hi1_2.text()[(4 * (counter)):])
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
    
    
    def carboxylic(self, noofc, bond00):
        if not bond00:
            bond00 = [1]
            ans = self.alkane(noofc)
        else:
             
            ans = self.alkene(noofc, bond00, True)
        
        spac = " "
        rndcnt = 1
        self.output_lo2_2.setText(len(ans)*spac)
        self.output_lo1_2.setText(len(ans)*spac)
        self.output_hi2_2.setText(len(ans)*spac)
        self.output_hi1_2.setText(len(ans)*spac)
        print("WARNING: for Caarboxylic, only one -COOH functional group is added per structure")
        nooc00 = noofc
        counter = int(bond00[0])
        print("LOG: nooc00", nooc00)
        
        print(counter, '=', noofc)
        if((counter==1)or(counter==noofc)):
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
                
        elif((counter%2==0)and (1<counter<noofc)):
            print("LOG: using lo")
            self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (counter - 1))] + \
                            "COOH" + self.output_lo2_2.text()[(4 * (counter)):])
            self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (counter - 1))] + \
                " ╵  " + self.output_lo1_2.text()[(4 * (counter)):])
        elif((counter%2==1)and (1<counter<noofc)):
            print("LOG: using hi")
            self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (counter - 1))] + \
                        "COOH" + self.output_hi2_2.text()[(4 * (counter)):])
            self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (counter - 1))] + \
                " ╷  " + self.output_hi1_2.text()[(4 * (counter)):])
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
    
    
    def alcohol(self, noofc, bond00):
        if not bond00:
            bond00 = [1]
            ans = self.alkane(noofc)
        else:
             
            ans = self.alkene(noofc, bond00, True)
        
        spac = " "
        rndcnt = 1
        self.output_lo2_2.setText(len(ans)*spac)
        self.output_lo1_2.setText(len(ans)*spac)
        self.output_hi2_2.setText(len(ans)*spac)
        self.output_hi1_2.setText(len(ans)*spac)
        print("WARNING: for Alcohol, only one -OH functional group is added per structure")
        nooc00 = noofc
        counter = int(bond00[0])
        print("LOG: nooc00", nooc00)
        
        print(counter, '=', noofc)
        if((counter==1)or(counter==noofc)):
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
                
        elif((counter%2==0)and (1<counter<noofc)):
            print("LOG: using lo")
            self.output_lo2_2.setText(self.output_lo2_2.text()[:(4 * (counter - 1))] + \
                            " OH " + self.output_lo2_2.text()[(4 * (counter)):])
            self.output_lo1_2.setText(self.output_lo1_2.text()[:(4 * (counter - 1))] + \
                " ╵  " + self.output_lo1_2.text()[(4 * (counter)):])
        elif((counter%2==1)and (1<counter<noofc)):
            print("LOG: using hi")
            self.output_hi2_2.setText(self.output_hi2_2.text()[:(4 * (counter - 1))] + \
                        " OH " + self.output_hi2_2.text()[(4 * (counter)):])
            self.output_hi1_2.setText(self.output_hi1_2.text()[:(4 * (counter - 1))] + \
                " ╷  " + self.output_hi1_2.text()[(4 * (counter)):])
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
    
    
    def alkene(self, noofc, bond00, normallity=False):
        if(bond00 == []):
            bond00 =[2]
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
                for i in bond00:
                        
                    counter = int(i)
                    print(counter, '=', noofc)
                    if((counter==noofc)or(counter==1)):
                        answer = "Error! Double bonds cannot be placed at terminal ends"
                        break
                    
                    answer = answer[:(4 * (counter - 1))] + \
                                    BOND[2] + answer[(4 * (counter)):]

                    answer = answer.replace("=CH₂-", "=CH₁-")
                    answer = answer.replace("=CH₁=", "= C =")
                    print(answer)
                
                self.placer.setMinimum(2)
                self.placer.setMaximum(noofc - 2)
                self.placer.setEnabled(True)
                self.pushButton_3.setEnabled(True)
        else:
            k = 1
            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
            print("LOG: Non-alkanised answer 001 :", answer)
            for i in bond00:
                        
                counter = int(i)
                print(counter, '=', noofc)
                
                
                answer = answer[:(4 * (counter - 1))] + \
                                BOND[2] + answer[(4 * (counter)):]
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

                counter = int(input(
                    "Enter the postion of the bond (from least to greatest or left to right) --> "))

                if (counter == 0):
                    k = 0
                elif (counter == 1):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0

                elif (counter == noofc):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0
                elif (counter == noofc - 1):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0
                else:

                    if (counter3 > counter):
                        print("Enter in ascending order")
                        k = 0
                    else:
                        answer = answer[:(4 * (counter - 1))] + \
                            BOND[2] + answer[(4 * (counter)):]

                        answer = answer.replace("=CH₂-", "=CH₁-")
                        answer = answer.replace("=CH₁=", "= C =")
                        print(answer)
                        counter3 = counter
            """
        return answer


    def alkyne(self, noofc, bond00=None):
        if(bond00 == []):
            bond00 =[2]
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
            for i in bond00:

                counter = int(i)
                if(counter-tmp_i==1):
                    print("Triple bonds cannot be placed near by because of Carbon tetravalency")
                    answer = "Triple bonds cannot be placed near by because of Carbon tetravalency"
                    break
                else:
                    tmp_i = counter
                print(counter, '=', noofc)
                if((counter==noofc)or(counter==1)):
                    answer = "Error! Triple bonds cannot be placed at terminal ends"
                    break

                answer = answer[:(4 * (counter - 1))] + \
                            BOND[4] + answer[(4 * (counter)):]
                answer = answer.replace("≡CH₂-", "≡ C -")

                if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH₂-"):
                    print("≡")
                    answer = answer[:(4 * (counter - 1) + 3)] + \
                        "≡ C -" + answer[(4 * (counter - 1) + 8):]


            counter3 = 0
            self.placer.setMinimum(2)
            self.placer.setMaximum(noofc - 2)
            self.placer.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            """
            while (k == 1):

                counter = int(input(
                    "Enter the postion of the bond (from least to greatest or left to right) --> "))

                if (counter == 0):
                    k = 0
                elif (counter == 1):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0

                elif (counter == noofc):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0
                elif (counter == noofc - 1):
                    print("Double bonds on terminal carbon atoms are invalid")
                    k = 0

                else:

                    if (counter3 > counter):
                        print("Enter in ascending order")
                        k = 0
                    elif (counter == counter3 + 1):
                        print("Valency of Carbon is 4")
                        k = 0
                    else:
                        answer = answer[:(4 * (counter - 1))] + \
                            BOND[4] + answer[(4 * (counter)):]
                        answer = answer.replace("≡CH₂-", "≡ C -")

                        if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH₂-"):
                            print("≡")
                            answer = answer[:(4 * (counter - 1) + 3)] + \
                                "≡ C -" + answer[(4 * (counter - 1) + 8):]

                        print(answer)
                        counter3 = counter
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


    def chkBond(self, bonds, noofc, bond00, numbranch=[], branch=[], benzylBool=False):
        branchesList = ["CH₃ ", "CH₂-CH₃ ", "CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₃ ", "CH₂-CH₂-CH₂-CH₂-CH₃ "]
        counterX = 1
        if(benzylBool):
            res = self.cyclic(6)
            noofc = 6
            n = (noofc-2)//2
            holder = TERMINAL[1]+((n-1)*"-CH₂")  # random holder variable
            self.output_hi2_2.setText(holder) # text box 1
            self.output_hi1_2.setText("╔"+" "*len(holder)+"╗") # text box 2
            self.output_lo1_2.setText("\\"+" "*len(holder)+"/") # text box 3
            self.output_lo2_2.setText(holder.replace("-", "=")) # text box 4
            return res
        
        if (bonds == 1):
            res = self.alkane(noofc)
        elif (bonds == 2):
            res = self.alkene(noofc, bond00)
            
        elif (bonds == 3):
            res = self.alkyne(noofc, bond00)
        elif (bonds ==4 ):
            res = self.cyclic(noofc) #TODO add support for benzene and children
            return res
        elif bonds == 5:
            res = self.ketone(noofc, bond00)
        elif bonds == 6:
            res = self.aldehyde(noofc, bond00)
        elif bonds == 7:
            res = self.carboxylic(noofc, bond00)
        elif bonds == 8:
            print("LOG: Alcohol ++++++++++++++")
            res = self.alcohol(noofc, bond00)
        
        else:
            res = "Bye Bye!"
            print(res)
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
            lo1Hold = self.output_lo1.text()
            hi1Hold = self.output_hi1.text()
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
                    
                    self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
                            " \  " + self.output_lo1.text()[(4 * (i[0])):])
                    self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
                            "  \ " + self.output_lo2.text()[(4 * (i[0])):])
                    self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + \
                        (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
                
                    
                    pass
                elif(counterX%2==1):
                    print("LOG: neither2")
                   
                    self.output_hi2.setText(self.output_hi2.text()[:(4 * (i[0] - 1))] + \
                            "  / " + self.output_hi2.text()[(4 * (i[0])):])
                    self.output_hi1.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + \
                            " /  " + self.output_hi1.text()[(4 * (i[0])):])
                    self.output_hi3.setText(self.output_hi3.text()[:(4 * (i[0] - 1))] + \
                        (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
                    pass
            elif hi_contains:
                print("LOG: hi_contains")
                print("LOG: branchCOnv:", branchConv)
                print("LOG: i[0]", i[0])
                self.output_lo1.setText(" "*len(res))
                self.output_lo2.setText(" "*len(res))
                self.output_lo3.setText(" "*len(res))
                
                self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
                        " \  " + self.output_lo1.text()[(4 * (i[0])):])
                self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
                        "  \ " + self.output_lo2.text()[(4 * (i[0])):])
                self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + " " +\
                        (" "*(len(branchConv)//2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
                
                
                pass
            elif lo_contains:
                print("LOG: lo_contains")
                self.output_hi1.setText(" "*len(res))
                self.output_hi2.setText(" "*len(res))
                self.output_hi3.setText(" "*len(res))
                self.output_hi2.setText(self.output_hi2.text()[:(4 * (i[0] - 1))] + \
                        "  / " + self.output_hi2.text()[(4 * (i[0])):])
                self.output_hi1.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + \
                        " /  " + self.output_hi1.text()[(4 * (i[0])):])
                self.output_hi3.setText(self.output_hi1.text()[:(4 * (i[0] - 1))] + "  " +\
                        (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
            else:
                print("LOG: neither_contains")
                if(counterX%2==0):
                    print("LOG: neither1")
                    self.output_lo1.setText(" "*len(res))
                    self.output_lo2.setText(" "*len(res))
                    self.output_lo3.setText(" "*len(res))
                    self.output_lo1.setText(self.output_lo1.text()[:(4 * (i[0] - 1))] + \
                            " \  " + self.output_lo1.text()[(4 * (i[0])):])
                    self.output_lo2.setText(self.output_lo2.text()[:(4 * (i[0] - 1))] + \
                            "  \ " + self.output_lo2.text()[(4 * (i[0])):])
                    self.output_lo3.setText(self.output_lo3.text()[:(4 * (i[0] - 1))] + \
                        (" "*ceil(len(branchConv)/2))+branchConv + self.output_hi1.text()[(4 * (i[0])+(len(branchConv)-4)):])
                
                    
                    pass
                elif(counterX%2==1):
                    print("LOG: neither2")
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



if __name__ == "__main__":
    appo = QtWidgets.QApplication(sys.argv)
    
    # Create and display the splash screen
    splash_pix = QPixmap(':res/carbonic-branding.png')
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    appo.processEvents()

    # Simulate something that takes time
    time.sleep(2)
    # app.aboutToQuit().connect(app.deleteLater)
    window = QtWidgets.QMainWindow()
    progg = MyAppv(window)
    window.show()
    sys.exit(appo.exec_())
