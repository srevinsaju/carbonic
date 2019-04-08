TERMINAL = ["CH3", "CH2"]
BOND = ["CH3-", "CH2-", "CH1=", "CH1-", " C ≡"]
counter2 = 1
answer=""
k = 0
RESULT = ""
NNNRESULT = ""
NNNNRESULT = ""

noofc = int(input("Enter number of carbon atoms ---> "))

bonds = int(input("Enter  1: single bond 2: double bond 3: triple bond  ---> "))


def addfunctionalgrp():
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
            if(halocounter==1):
                tempterminal = answer[-4:]
                tempterminal = tempterminal.replace("CH3", "CH2")
                answer=answer[:-5]+tempterminal




def alkane():
    if (noofc == 1):

        answer = "CH4"
    else:

        answer = BOND[0] + BOND[1] * (noofc - 2) + TERMINAL[0]
    print(answer)


def alkene():
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
        while (k == 1):

            counter = int(input("Enter the postion of the bond (from least to greatest or left to right) --> "))

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
                    answer = answer[:(4 * (counter - 1))] + BOND[2] + answer[(4 * (counter)):]

                    answer = answer.replace("=CH2-", "=CH1-")
                    answer = answer.replace("=CH1=", "= C =")
                    print(answer)
                    counter3 = counter


def alkyne():
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
        while (k == 1):

            counter = int(input("Enter the postion of the bond (from least to greatest or left to right) --> "))

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
                    answer = answer[:(4 * (counter - 1))] + BOND[4] + answer[(4 * (counter)):]
                    answer = answer.replace("≡CH2-", "≡ C -")

                    if (answer[(4 * (counter - 1) + 3):(4 * (counter - 1) + 8)] == "≡CH2-"):
                        print("≡")
                        answer = answer[:(4 * (counter - 1) + 3)] + "≡ C -" + answer[(4 * (counter - 1) + 8):]

                    print(answer)
                    counter3 = counter


if (bonds == 1):
    alkane()
elif (bonds == 2):
    alkene()
elif (bonds == 3):
    alkyne()
else:
    print("Bye Bye!")
