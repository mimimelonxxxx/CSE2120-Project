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
        return checkPos(NEWION)

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
        return checkNeg(NEWION)

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
    PROPERTIES1 = ALLPOS.get(NAME1)
    CHARGE1 = PROPERTIES1[1]
    PROPERTIES2 = ALLNEG.get(NAME2)
    CHARGE2 = PROPERTIES2[1]
    # get the greatest common denominator and divide each by that
    GCD = math.gcd(CHARGE1, CHARGE2) 
    COEFFICIENT2 = CHARGE1 / GCD
    COEFFICIENT1 = CHARGE2 / GCD
    return -COEFFICIENT1, COEFFICIENT2

def determineLimiting(MOLES1, COEFFICIENT1, MOLES2, COEFFICIENT2):
    """
    converts the moles of the first reactant to moles of the second reactant and compare the two to find the limiting reagent 
    :param MOLES1: float (moles of first reactant)
    :param MOLES2: float (moles of second reactant)
    :return: LIMITING -> int, MOLES -> float 
    """
    MOLES21 = MOLES2 * COEFFICIENT1 / COEFFICIENT2 
    if MOLES21 > MOLES1: 
        LIMITING = 1
        return LIMITING, MOLES1
    else: 
        LIMITING = 2
        return LIMITING, MOLES2

def calculateSolubility(MOLES, NAME1, NAME2):
    """
    looks through the top row of the solubility table and finds which column to use
    :param MOLES: float (moles of limiting)
    :param NAME1: str (name of first reactant)
    :param NAME2: str (name of second reactant)
    :return: COLUMN -> str, NAME -> str (name of the ion to use)
    """
    global FIRSTFIRST, FIRSTSECOND, FIRSTTHIRD, FIRSTFOURTH, FIRSTFIFTH, FIRSTSIXTH, FIRSTSEVENTH
    # loop?
    PROPERTIES = FIRSTFIRST.get(NAME1) # try each column to see if the element is there, then try the other name 
    PROPERTIES[1] # gets charge of name
    # COLUMN = "SECOND" etc 

def calculatePrecipitate(MOLES, COLUMN, REACTANT1, REACTANT2):
    """
    calculate the precipitate by using the mole ratio
    :param MOLES: float (moles of the limiting reagent)
    :param REACTANT1: str (name of the first reactant)
    :param REACTANT2: str (name of the second reactant)
    :return: float (amount of precipitate)
    """
    global FIRSTFIRST, FIRSTSECOND, FIRSTTHIRD, FIRSTFOURTH, FIRSTFIFTH, FIRSTSIXTH, FIRSTSEVENTH, ALLPOS
    

def molesToMass(MOLES, NAME): 
    """
    converts the moles of a substance to grams 
    :param MOLES: float (the moles of the substance)
    :param NAME: str (name of the substance)
    :return: float (mass of the substance)
    """
    global ALLPOS
    PROPERTIES = ALLPOS.get(NAME)
    MOLARMASS = PROPERTIES[0]
    MASS = MOLES * MOLARMASS 
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

def displayPrecipitate(MASS, PRECIPITATE):
    """
    displays the name and mass of the precipitate 
    :param MASS: float
    :param PRECIPITATE: str
    :return: None
    """
    # if there's no precipitate, need to display BEFORE limiting, cancel limiting
    print(f"The mass of {PRECIPITATE} is {MASS} grams. ")

### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # Inputs # 
    POSITIVE, PVOLUME, PCONCENTRATION = getPositive()
    NEGATIVE, NVOLUME, NCONCENTRATION = getNegative()

    # Processing # 
    PMOLES = calculateMoles(PVOLUME, PCONCENTRATION)
    NMOLES = calculateMoles(NVOLUME, NCONCENTRATION)
    
    PCOEFFICIENT, NCOEFFICIENT = balanceEquation(POSITIVE, NEGATIVE)
    LIMITING, LMOLES = determineLimiting(PMOLES, PCOEFFICIENT, NMOLES, NCOEFFICIENT)
    # Outputs # 
    displayLimiting(LIMITING, POSITIVE, NEGATIVE)
    