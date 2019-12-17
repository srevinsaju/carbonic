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
from mainui import Ui_Dialog
import os
from math import ceil
import sys
import time
import webbrowser
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from ccore import convertor, chkBond, displax

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
        self.pushButton_4.pressed.connect(self.compute)

    def openme(self):
        webbrowser.open("https://srevinsaju.wixsite.com/srevinsaju")
    def opengit(self):
        webbrowser.open("https://srevinsaju.github.io/carbonic/")
    def compute(self):
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
        x = convertor(inpu)
        y = chkBond(x)
        
        # REFERNCE : res, lo1Hold, lo2Hold, lo3Hold, hi1Hold, hi2Hold, hi3Hold
        if len(y)==1:
            self.output.setText(y[0])
        else:
            self.output.setText(y[0])
            self.output_lo1.setText(y[1])
            self.output_lo2.setText(y[2])
            self.output_lo3.setText(y[3])
            self.output_hi1.setText(y[4])
            self.output_hi2.setText(y[5])
            self.output_hi3.setText(y[6])
        


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
        print("DEPRECATED, use IUPAC Text field")

    def sliderValueChange(self):
        self.placertxt.setText(str(self.placer.value()))
        print("DEPRECATED, use IUPAC Text field")
    def bondchk(self):
        print("DEPRECATED, use IUPAC Text field")

    

    



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
    window.show(); splash.hide()
    sys.exit(appo.exec_())
