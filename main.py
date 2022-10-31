"""
title: Solubility Table 
author: Michelle Jiang 
date-created: 2022-10-20
"""

from periodic_table import * 

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

def getPositive(): 
    """
    gets the information for the positive ion 
    :return: str, float, float
    """
    ION = input("What's the name of the positive reacting ion? (no charges) ")
    ION = ION.lower()
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
    :param NAME1: str
    :param NAME2: str 
    :return: list (int)
    """
    global ALLPOS 
    # need to find and use molar ratio
    # need to balance charges
    PROPERTIES1 = ALLPOS.get(NAME1)
    CHARGE1 = PROPERTIES1[1]
    PROPERTIES2 = ALLPOS.get(NAME2)
    CHARGE2 = PROPERTIES2[1]
    # multiply the moles of the substance to balance the charges 
    # somehow make charge1 = charge2
    while not CHARGE2 == CHARGE1: 
        # try to balance charges 
        pass
    return CHARGE1, CHARGE2

def determineLimiting(MOLES1, NAME1, MOLES2, NAME2):
    """
    converts the moles of the first reactant to moles of the second reactant and compare the two to find the limiting reagent 
    :param MOLES1: float (moles of first reactant)
    :param MOLES2: float (moles of second reactant)
    :return: LIMITING -> int (whether reactant 1 or 2 is the limiting), LMOLES -> float 
    """


def calculateSolubility(MOLES, NAME1, NAME2):
    """
    looks through the top row of the solubility table and finds which column to use
    :param MOLES: float (moles of limiting)
    :param NAME1: str (name of first reactant)
    :param NAME2: str (name of second reactant)
    :return: COLUMN -> int, NAME -> str (name of the ion to use)
    """
    global FIRSTFIRST, FIRSTSECOND, FIRSTTHIRD, FIRSTFOURTH, FIRSTFIFTH, FIRSTSIXTH, FIRSTSEVENTH
    try: 
        PROPERTIES = FIRSTFIRST.get(NAME1) # try each column to see if the element is there, then try the other name 
        PROPERTIES[1] # gets charge of name
    except: 
        PROPERTIES

def calculatePrecipitate(MOLES, REACTANT1, REACTANT2):
    """
    calculate the precipitate by using the mole ratio
    :param MOLES: float (moles of the limiting reagent)
    :param REACTANT1: str (name of the first reactant)
    :param REACTANT2: str (name of the second reactant)
    :return: int (amount of precipitate)
    """
    global FIRSTFIRST

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
        print(f"The limiting reagent is {NAME1}. ")
    else: 
        print(f"The limiting reagent is {NAME2}. ")



### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # Inputs # 
    POSITIVE, PVOLUME, PCONCENTRATION = getPositive()
    NEGATIVE, NVOLUME, NCONCENTRATION = getNegative()

    # Processing # 
    PMOLES = calculateMoles(PVOLUME, PCONCENTRATION)
    NMOLES = calculateMoles(NVOLUME, NCONCENTRATION)
    
    # Outputs # 