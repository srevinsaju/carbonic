"""
CARBONCOMPUNDS on github by @srevinsaju

THIS IS MAIN MODULE FOR GUI INTEGRATION PORT.

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

"""

from mainui import Ui_Dialog
import os
from math import ceil
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, uic, QtWidgets
TERMINAL = ["CH3", "CH2"]
BOND = ["CH3-", "CH2-", "CH1=", "CH1-", " C ≡"]
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
    
    addOnBranches = []
    addOnBranchesNum = []
    listOfAdditionalStuff = ["methyl", "ethyl", "propyl", "butyl", "pentyl", "hexyl"]
    count = 1
    print(inp.find("["), " is INDEX")
    if((inp.find("["))!=-1):
        
        for i in listOfAdditionalStuff:
            if(inp.find(i)==-1):
                print("pass")
                count+=1
                continue
            else:
                print("found ", i)
                indic = inp.find(i)
                addOnNum = int(inp[inp.find("[")+1:indic-1])
                print("LOG : AddOnNum is ", addOnNum)
                addOnBranchesNum.append(addOnNum)
                addOnBranches.append(i)
                inp=inp[(indic+len(i)+1):]
                
                count+=1
                
    else:
        print("HOHO")
    print(inp)
    print("LOG: addOnBranchesNum = ", addOnBranchesNum)
    print("LOG: addOnBranches = ", addOnBranches)
    tmpinp = inp
    bond00 = []
    
    for i in tmpinp:
        if(inp[0].isalpha()):
            print("alpha")
            break
        try:
            if(inp[0].isnumeric):
                bond00.append(inp[0])
                inp = inp[1:]
            else:
                print("No",i)
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
       
    
    if(inp.endswith("ane")):
        bond_int = 1
        print("alkan")
        restOfInp = inp.partition("ane")
    elif(inp.endswith("ene")):
        print("alken")
        bond_int = 2
        restOfInp = inp.partition("ene")
        
    elif(inp.endswith("yne")):
        bond_int = 3
        print("alkyn")
        restOfInp = inp.partition("yne")
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
    
    return noofc0, bond_int, bond00, addOnBranchesNum, addOnBranches
    
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
                tempterminal = tempterminal.replace("CH3", "CH2")
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
        inpu = self.textEdit.toPlainText()
        noofc, bondo, bond01, numbranch, branch = convertor(inpu)
        self.compute(noofc, bondo, bond01, numbranch, branch)
        

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
        answer = answer.replace("=CH2-", "=CH1-")
        answer = answer.replace("=CH1=", "= C =")
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
        answer = answer.replace("≡CH2-", "≡ C -")

        if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH2-"):
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

    def compute(self, noc=None, boc=None, bond00=None, numbranch=[], branch=[]):
        if(noc ==None):
            noofc = self.nooc.value()
        else:
            noofc = noc
        if(boc == None):
            bonds = self.bondui.value()
        else:
            bonds=boc
            
        print(noofc)
        print(bonds)
        print(bond00)
        restxt = self.chkBond(bonds, noofc, bond00, numbranch, branch)
        print(restxt + "jj")
        leng = len(restxt)
        if(leng>=50):

            self.output.setFont(QtGui.QFont('Courier New', 10, weight=QtGui.QFont.Bold))
        else:
            self.output.setFont(QtGui.QFont('Courier New', 14, weight=QtGui.QFont.Bold))
        self.output.setText(restxt)

    def alkane(self, noofc):
        self.pushButton_3.setEnabled(False)
        if (noofc == 1):

            answer = "CH4"
        else:

            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
        print(answer)
        return answer


    def alkene(self, noofc, bond00):
        if (noofc == 1):

            answer = "Not possible"
            print(answer)
        elif (noofc == 2):
            answer = "CH2=CH2"
            print(answer)
        else:
            k = 1
            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
            for i in bond00:
                    
                counter = int(i)
                print(counter, '=', noofc)
                if((counter==noofc)or(counter==(noofc-1))or(counter==1)):
                    answer = "Error! Double bonds cannot be placed at terminal ends"
                    break
                
                answer = answer[:(4 * (counter - 1))] + \
                                BOND[2] + answer[(4 * (counter)):]

                answer = answer.replace("=CH2-", "=CH1-")
                answer = answer.replace("=CH1=", "= C =")
                print(answer)
            
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

                        answer = answer.replace("=CH2-", "=CH1-")
                        answer = answer.replace("=CH1=", "= C =")
                        print(answer)
                        counter3 = counter
            """
        return answer


    def alkyne(self, noofc, bond00=None):
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
                if((counter==noofc)or(counter==(noofc-1))or(counter==1)):
                    answer = "Error! Triple bonds cannot be placed at terminal ends"
                    break

                answer = answer[:(4 * (counter - 1))] + \
                            BOND[4] + answer[(4 * (counter)):]
                answer = answer.replace("≡CH2-", "≡ C -")

                if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH2-"):
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
                        answer = answer.replace("≡CH2-", "≡ C -")

                        if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH2-"):
                            print("≡")
                            answer = answer[:(4 * (counter - 1) + 3)] + \
                                "≡ C -" + answer[(4 * (counter - 1) + 8):]

                        print(answer)
                        counter3 = counter
            """
        return answer


    def chkBond(self, bonds, noofc, bond00, numbranch=[], branch=[]):
        branchesList = ["CH3", "CH2-CH3", "CH2-CH2-CH3", "CH2-CH2-CH2-CH3", "CH2-CH2-CH2-CH2-CH3"]
        counterX =1
        if (bonds == 1):
            res = self.alkane(noofc)
            
            

        elif (bonds == 2):
            res = self.alkene(noofc, bond00)
            
        elif (bonds == 3):
            res = self.alkyne(noofc, bond00)
            
        else:
            res = "Bye Bye!"
            print(res)
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
                    
                    theAlterer = theAlterer[:2]+str(int(theAlterer[2])-1)+theAlterer[3:]
                    theAlterer  = theAlterer.replace("CH0"," C ")
                else:
                    print(msg)
                    res = msg
                    return res
            res = res[:(branchPos-4)]+theAlterer+res[branchPos:]    
            if(counterX%2 == 1):
                if(i[0] == int(ceil((nooc00/2) ))):
                    
                    print("LOG : DIVIDER IS CENTERED ")
                    self.output_6.setText("\\")
                    self.output_2.setText(" "+ spac*(len(branchConv)) +branchConv)
                
                elif(i[0] > int(ceil((nooc00/2) ))):
                    self.output_2.setText(spac + spac*(len(branchConv)) +spac*(8*(i[0]-int(ceil((nooc00/2)))))+branchConv)
                    self.output_6.setText(spac*8*(i[0]-int(ceil((nooc00/2))))+"\\")
                elif(i[0] < int(ceil((nooc00/2) ))):
                    self.output_2.setText(spac + spac*(len(branchConv)) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-i[0])))
                    self.output_6.setText("\\" + spac*(8*(int(ceil((nooc00/2)))-i[0])))
            elif(counterX%2==0):
                if(i[0] == int(ceil((nooc00/2) ))):
                    
                    print("LOG : DIVIDER IS CENTERED ")
                    self.output_4.setText("/")
                    self.output_3.setText(" "+ spac*(len(branchConv)) +branchConv)
                
                elif(i[0] > int(ceil((nooc00/2) ))):
                    self.output_3.setText(spac + spac*(len(branchConv)) +spac*(8*(i[0]-int(ceil((nooc00/2)))))+branchConv)
                    self.output_4.setText(spac*8*(i[0]-int(ceil((nooc00/2))))+"/")
                elif(i[0] < int(ceil((nooc00/2) ))):
                    self.output_3.setText(spac + spac*(len(branchConv)) + branchConv+ spac*(8*(int(ceil((nooc00/2)))-i[0])))
                    self.output_4.setText("/" + spac*(8*(int(ceil((nooc00/2)))-i[0])))

            counterX+=1
        return res



if __name__ == "__main__":
    appo = QtWidgets.QApplication(sys.argv)
    # app.aboutToQuit().connect(app.deleteLater)
    window = QtWidgets.QMainWindow()
    progg = MyAppv(window)
    window.show()
    sys.exit(appo.exec_())
