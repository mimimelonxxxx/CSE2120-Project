# First row, First column
FIRSTFIRST = {
    "H2": (2.02, 1), 
    "Li": (6.94, 1),  
    "Na": (22.99, 1), 
    "K": (39.10, 1), 
    "Rb": (85.47, 1), 
    "Cs": (132.91, 1), 
    "Fr": (223, 1),
    "NH4": (18.05, 1),
    "NO3": (62.01, -1),
    "ClO3": (83.45, -1),
    "CH3COO": (59.05, -1)
}

# First row, Second column 
FIRSTSECOND = {
    "F": (19.00, -1)
}

# First row, Third column 
FIRSTTHIRD = {
    ("Cl2", 70.90, -1), 
    ("Br", 79.90, -1), 
    ("I2", 126.90, -1)
}

# First row, Fourth column 

FIRSTFOURTH = {
    ("SO4", 96.07, -2)
}

# First row, Fifth column 
FIRSTFIFTH = {
    ("CO3", 60.01, -2), 
    ("PO4", 94.97, -3), 
    ("SO3", 80.07, -2)
}

# First row, Sixth column 
FIRSTSIXTH = {
    ("IO3", 174.90, -1), 
    ("OOCCOO", 88.02, -2), 
}

# First row, Seventh column 
FIRSTSEVENTH = {
    ("OH", 17.01, -1)
}

# Second row, Fifth column 
SECONDFIFTH = {
    ("H2", 2.02, 1), 
    ("Li", 6.94, 1),  
    ("Na", 22.99, 1), 
    ("K", 39.10, 1), 
    ("Rb", 85.47, 1), 
    ("Cs", 132.91, 1), 
    ("Fr", 223, 1),
    ("NH4", 18.05, 1)
}

# Second row, Sixth column 
SECONDSIXTH = {
    ("H2", 2.02, 1), 
    ("Li", 6.94, 1),  
    ("Na", 22.99, 1), 
    ("K", 39.10, 1), 
    ("Rb", 85.47, 1), 
    ("Cs", 132.91, 1), 
    ("Fr", 223, 1),
    ("NH4", 18.05, 1),
    ("Co", 58.93, 2), # remember to check if the other reactant is IO3 otherwise forms a precipitate
    ("Fe", 55.85, 3) # check if it's OOCCOO
}

# Second row, Seventh column 
SECONDSEVENTH = {
    ("H2", 2.02, 1), 
    ("Li", 6.94, 1),  
    ("Na", 22.99, 1), 
    ("K", 39.10, 1), 
    ("Rb", 85.47, 1), 
    ("Cs", 132.91, 1), 
    ("Fr", 223, 1),
    ("NH4", 18.05, 1)
}

# Third row, First column 
THIRDFIRST = {
    ("Rb", 85.47, 1), # Check for RbClO4 
    ("Cs", 132.91, 1), # CsClO4
    ("Ag", 107.87, 1), # AgCH3COO
    ("Hg2", 401.18, 2) #Hg2(CH3COO)2
}

# Third row, Second column 

THIRDSECOND = {
    ("Li", 6.94, 1), 
    ("Mg", 48.62, 2), 
    ("Ca", 40.08, 2), 
    ("Sr", 87.62, 2), 
    ("Ba", 137.33, 2), 
    ("Fe", 55.85, 2), 
    ("Hg2", 401.18, 2), 
    ("Pb", 207.2, 2)
}

# Third row, Third column 

THIRDTHIRD = {
    ("Cu", 63.55, 1), 
    ("Ag", 107.87, 1), 
    ("Hg2", 401.18, 2), 
    ("Pb", 207.2, 2), 
    ("Tl", 204.38, 1)
}

# Third row, Fourth column 

THIRDFOURTH = {
    ("Ca", 40.08, 2), 
    ("Sr", 87.62, 2), 
    ("Ba", 137.33, 2), 
    ("Ag", 107.87, 1), 
    ("Hg2", 401.18, 2), 
    ("Pb", 207.2, 2), 
    ("Ra", 226, 2)
}

# Third row, right side 

ALLELEMENTS = {

}
# use a dictionary, name: (mass, charge)
# only need to get the ones that produce charges (not the higher element ones)