"""
CARBONCOMPUNDS on github by @srevinsaju

THIS IS MAIN MODULE FOR GUI INTEGRATION PORT.

ALL CODE IS LICENSED UNDER GNU-GPL LICENSE. READ LICENSE FOR MORE INFORMATION

"""

from mainui import Ui_Dialog
import os
import sys
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
        self.placer.sliderMoved.connect(self.sliderValueChange)
        self.placer.sliderReleased.connect(self.sliderValueChange)
        self.placertxt.setText(str(self.placer.value()))
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.pressed.connect(self.bondchk)

    def quitme(self):
        sys.exit(0)

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

    def compute(self):
        noofc = self.nooc.value()
        bonds = self.bondui.value()
        print(noofc)
        print(bonds)
        restxt = self.chkBond(bonds, noofc)
        print(restxt + "jj")
        leng = len(restxt)
        if(leng>=32):
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


    def alkene(self, noofc):
        if (noofc == 1):

            answer = "Not possible"
            print(answer)
        elif (noofc == 2):
            answer = "CH2=CH2"
            print(answer)
        else:
            k = 1

            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
            counter3 = 0
            self.placer.setMinimum(2)
            self.placer.setMaximum(noofc - 2)
            self.placer.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            """.
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


    def alkyne(self, noofc):
        if (noofc == 1):

            answer = "Not possible"
            print(answer)
        elif (noofc == 2):
            answer = "CH1≡CH1"
            print(answer)
        else:
            k = 1

            answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
            counter3 = 0
            
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
    

    def chkBond(self, bonds, noofc):

        if (bonds == 1):
            res = self.alkane(noofc)
            return res

        elif (bonds == 2):
            res = self.alkene(noofc)
            return res
        elif (bonds == 3):
            
            res = self.alkyne(noofc)
            return res
        else:
            res = "Bye Bye!"
            print(res)
            return res



if __name__ == "__main__":
    appo = QtWidgets.QApplication(sys.argv)
    # app.aboutToQuit().connect(app.deleteLater)
    window = QtWidgets.QMainWindow()
    progg = MyAppv(window)
    window.show()
    sys.exit(appo.exec_())
