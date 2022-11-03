"""
title: Solubility Table 
author: Michelle Jiang 
date-created: 2022-10-20
"""

from periodic_table import * 
import math

### SUBROUTINES ### 

# Inputs # 
def checkFloat(VALUE):
    """
    validates whether a value is a float
    :param VALUE: str
    :return: float
    """
    try: 
        float(VALUE)
        return float(VALUE)
    except ValueError:
        print("Please enter a valid number! ")
        NEW_NUM = input("> ")
        return checkFloat(NEW_NUM)

def checkPos(ION):
    """
    Checks if the ion is in the positive table 
    :param ION: str 
    :return: str 
    """
    global ALLPOS
    if not ALLPOS.get(ION) == None:
        return ION
    else:
        print("Please enter a valid positive ion!")
        NEWION = input("> ")
        return checkPos(NEWION.lower())

def checkNeg(ION):
    """
    Checks if the ion is in the negative table 
    :param ION: str 
    :return: str 
    """
    global ALLNEG
    if not ALLNEG.get(ION) == None:
        return ION
    else:
        print("Please enter a valid negative ion!")
        NEWION = input("> ")
        return checkNeg(NEWION.lower())

def startScreen():
    """
    prints starting text
    :return: None
    """
    print("Calculate the mass of a precipitate from two ions! ")

def getPositive(): 
    """
    gets the information for the positive ion 
    :return: str, float, float
    """
    ION = input("What's the name of the positive reacting ion? (no charges) ")
    ION = ION.lower()
    ION = checkPos(ION)
    VOLUME = input("What's the volume of the positive solution? (L) ")
    VOLUME = checkFloat(VOLUME)
    CONCENTRATION = input("What's the concentration of the positive solution? (mol/L) ")
    CONCENTRATION = checkFloat(CONCENTRATION)
    return ION, VOLUME, CONCENTRATION 

def getNegative(): 
    """
    gets the information for the negative ion 
    :return: str, float, float
    """
    ION = input("What's the name of the negative reacting ion? (no charges) ")
    ION = ION.lower()
    ION = checkNeg(ION)
    VOLUME = input("What's the volume of the negative solution? (L) ")
    VOLUME = checkFloat(VOLUME)
    CONCENTRATION = input("What's the concentration of the negative solution? (mol/L) ")
    CONCENTRATION = checkFloat(CONCENTRATION)
    return ION, VOLUME, CONCENTRATION 

# Processing # 
def calculateMoles(VOLUME, CONCENTRATION): 
    """
    convert the volume and concentration of the reactant to moles
    :param VOLUME: float 
    :param CONCENTRATION: float 
    :return: MOLES -> float 
    """
    MOLES = VOLUME * CONCENTRATION
    return MOLES 

def balanceEquation(NAME1, NAME2):
    """
    balances the equation by 
    1. getting the charges of each reactant
    2. comparing the charges 
    3. tries to make the charges equal (multiply by each other?) 
    :param NAME1: str
    :param NAME2: str 
    :return: coefficients (int)
    """
    global ALLPOS, ALLNEG
    # need to balance charges
    # diatomic atoms 
    PROPERTIES1 = ALLPOS.get(NAME1)
    CHARGE1 = PROPERTIES1[1]
    PROPERTIES2 = ALLNEG.get(NAME2)
    CHARGE2 = PROPERTIES2[1]
    # get the greatest common denominator and divide each by that
    GCD = math.gcd(CHARGE1, CHARGE2) 
    COEFFICIENT2 = CHARGE1 / GCD
    COEFFICIENT1 = CHARGE2 / GCD
    COEFFICIENT1 = int(COEFFICIENT1)
    COEFFICIENT2 = int(COEFFICIENT2)
    return -COEFFICIENT1, COEFFICIENT2

def determineLimiting(MOLES1, COEFFICIENT1, MOLES2, COEFFICIENT2):
    """
    converts the moles of the first reactant to moles of the second reactant and compare the two to find the limiting reagent 
    :param MOLES1: float (moles of first reactant)
    :param MOLES2: float (moles of second reactant)
    :return: LIMITING -> int, MOLES -> float 
    """
    MOLES21 = MOLES2 * COEFFICIENT1 / COEFFICIENT2 # convert moles 2 to moles 1 
    if MOLES21 > MOLES1: # test which one is greater 
        LIMITING = 1 
        return LIMITING, MOLES1 
    else: 
        LIMITING = 2
        return LIMITING, MOLES2

def formsPrecipitate(NAME1, NAME2):
    """
    looks through the top row of the solubility table and checks if it forms a precipitate
    :param MOLES: float (moles of limiting)
    :param NAME1: str (name of first reactant)
    :param NAME2: str (name of second reactant)
    :return: COLUMN -> int (if COLUMN == 0 then it does not form a precipitate)
    """
    global FIRSTFIRST, FIRSTSECOND, FIRSTTHIRD, FIRSTFOURTH, FIRSTFIFTH, FIRSTSIXTH, FIRSTSEVENTH
    # look if negative is in the chart first
    # loop that changes what COLUMN equals every time 
    # COLUMN = FIRSTFIRST 
    # conditional statements as last resort 
    if NAME2 in FIRSTFIRST: # try each column to see if the element is there, then try the other name 
        COLUMN = 1
    elif NAME2 in FIRSTSECOND: 
        COLUMN = 2
    elif NAME2 in FIRSTTHIRD: 
        COLUMN = 3
    elif NAME2 in FIRSTFOURTH: 
        COLUMN = 4
    elif NAME2 in FIRSTFIFTH: 
        COLUMN = 5
    elif NAME2 in FIRSTSIXTH: 
        COLUMN = 6
    elif NAME2 in FIRSTSEVENTH: 
        COLUMN = 7
    elif NAME1 in FIRSTFIRST: 
        COLUMN = 1 # checks if it is a group 1 ion or nh4
    else: 
        COLUMN = 0 # does not form a precipitate 
    # this is a whole lot of spaghetti code 
    return COLUMN
    

def calculatePrecipitate(MOLES, COLUMN, LIMITING, POSITIVE, NEGATIVE, PCOEFFICIENT, NCOEFFICIENT):
    """
    calculate the precipitate by using the mole ratio
    :param MOLES: float (moles of the limiting reagent)
    :param COLUMN: int
    :param LIMITING: int (whether pos or neg is the limiting)
    :param POSITIVE: str (name of pos)
    :param NEGATIVE: str (name of neg)
    :param PCOEFFICIENT: int 
    :param NCOEFFICIENT: int 
    :return: float (amount of precipitate)
    """
    global FIRSTFIRST, FIRSTSECOND, FIRSTTHIRD, FIRSTFOURTH, FIRSTFIFTH, FIRSTSIXTH, FIRSTSEVENTH, ALLPOS
    # i need to write this properly 
    """
    There must be a function that does all of the following:
        Add a value to an array
        Modify a value from an array
        OPTIONAL: delete or remove a value from an array
    """
    PRECIPITATE = False 
    
    

def precipitateMass(MOLES, NAME1, NAME2, COEFFICIENT1, COEFFICIENT2): 
    """
    converts the moles of a precipitate to grams 
    :param MOLES: float (the moles of the precipitate)
    :param NAME1: str (name of pos reactant)
    :param NAME2: str (name of neg reactant)
    :param COEFFICIENT1: int (coefficient of pos)
    :param COEFFICIENT2: int (coefficient of neg)
    :return: float (mass of the substance)
    """
    global ALLPOS, ALLNEG
    PROPERTIES1 = ALLPOS.get(NAME1)
    MOLARMASS1 = PROPERTIES1[0]
    PROPERTIES2 = ALLNEG.get(NAME2)
    MOLARMASS2 = PROPERTIES2[0]
    MASS = MOLES * (MOLARMASS1 * COEFFICIENT1 + MOLARMASS2 * COEFFICIENT2)
    MASS = round(MASS, 2)
    return MASS
    

# Outputs # 
def displayLimiting(LIMITING, NAME1, NAME2): 
    """
    displays the name of the limiting reagent 
    :param LIMITING: int (which one is limiting)
    :NAME1: str 
    :NAME2: str 
    :return: None 
    """
    if LIMITING == 1: 
        print(f"The limiting reagent is {NAME1.title()}. ")
    else: 
        print(f"The limiting reagent is {NAME2.title()}. ")

def displayPrecipitate(MASS, PNAME, NNAME, PCOEFFICIENT, NCOEFFICIENT):
    """
    displays the name and mass of the precipitate 
    :param MASS: float
    :param PNAME: str
    :param NNAME: str
    :param PCOEFFICIENT: int
    :param NCOEFFICIENT: int 
    :return: None
    """
    # time to write some more spaghetti code
    if MASS == 0: 
        print("The two ions will not create a precipitate. ")
    elif PCOEFFICIENT == 1 and NCOEFFICIENT != 1:
        if len(NEGATIVE) > 2:
            if NEGATIVE == "clo3":
                print(f"The mass of {PNAME.title()}(ClO3){NCOEFFICIENT} is {MASS} grams. ")
            elif NEGATIVE == "clo4":
                print(f"The mass of {PNAME.title()}(ClO4){NCOEFFICIENT} is {MASS} grams. ")
            else:
                print(f"The mass of {PNAME.title()}({NNAME.upper()}){NCOEFFICIENT} is {MASS} grams. ")
        else:
            print(f"The mass of {PNAME.title()}{NNAME.title()}{NCOEFFICIENT} is {MASS} grams. ")
    elif PCOEFFICIENT != 1 and NCOEFFICIENT == 1:
        if len(POSITIVE) > 2:
            print(f"The mass of ({PNAME.upper()}){PCOEFFICIENT}{NNAME.title()} is {MASS} grams. ")
        else:
            print(f"The mass of {PNAME.title()}{PCOEFFICIENT}{NNAME.title()} is {MASS} grams. ")
    elif PCOEFFICIENT == 1 and NCOEFFICIENT == 1: 
        print(f"The mass of {PNAME.title()}{NNAME.title()} is {MASS} grams. ")
    else:
        if len(POSITIVE) > 2: 
            print(f"The mass of ({PNAME.upper()}){PCOEFFICIENT}{NNAME.title()}{NCOEFFICIENT} is {MASS} grams. ")
        elif len(NEGATIVE) > 2:
            if NEGATIVE == "clo3":
                print(f"The mass of {PNAME.title()}{PCOEFFICIENT}(ClO3){NCOEFFICIENT} is {MASS} grams. ")
            elif NEGATIVE == "clo4":
                print(f"The mass of {PNAME.title()}{PCOEFFICIENT}(ClO4){NCOEFFICIENT} is {MASS} grams. ")
            else:
                print(f"The mass of {PNAME.title()}{PCOEFFICIENT}({NNAME.upper()}){NCOEFFICIENT} is {MASS} grams. ")
        else:
            print(f"The mass of {PNAME.title()}{PCOEFFICIENT}{NNAME.title()}{NCOEFFICIENT} is {MASS} grams. ")

### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # Inputs # 
    startScreen()
    POSITIVE, PVOLUME, PCONCENTRATION = getPositive()
    NEGATIVE, NVOLUME, NCONCENTRATION = getNegative()

    # Processing # 
    PMOLES = calculateMoles(PVOLUME, PCONCENTRATION)
    NMOLES = calculateMoles(NVOLUME, NCONCENTRATION)

    PCOEFFICIENT, NCOEFFICIENT = balanceEquation(POSITIVE, NEGATIVE)
    LIMITING, LMOLES = determineLimiting(PMOLES, PCOEFFICIENT, NMOLES, NCOEFFICIENT)
    COLUMN = formsPrecipitate(POSITIVE, NEGATIVE)
    PRECIPITATE = calculatePrecipitate(LMOLES, COLUMN, LIMITING, POSITIVE, NEGATIVE, PCOEFFICIENT, NCOEFFICIENT)
    
    PMASS = precipitateMass(PRECIPITATE, POSITIVE, NEGATIVE, PCOEFFICIENT, NCOEFFICIENT)
    # Outputs # 
    if PRECIPITATE != 0:
        displayLimiting(LIMITING, POSITIVE, NEGATIVE)
    displayPrecipitate(PMASS, POSITIVE, NEGATIVE, PCOEFFICIENT, NCOEFFICIENT)