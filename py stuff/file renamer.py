#! /bin/env python3

import os
import sys
import re

base = "/mnt/Files/Work/School Stuff/Class 11/Textbooks/Mathematics/"
# Base Path for files (textbook pdfs)

# Dictionary for Math pdfs in following associations: ("filename": "chaptername")
math = {
    'Math01.pdf': 'Sets',
    'Math02.pdf': 'Relations & Functions',
    'Math03.pdf': 'Trigonometric Functions',
    'Math04.pdf': 'Complex Numbers and Quadratic Equations',
    'Math05.pdf': 'Linear Inequalities',
    'Math06.pdf': 'Permutations and Combinations',
    'Math07.pdf': 'Binomial Theorem',
    'Math08.pdf': 'Sequence and Series',
    'Math09.pdf': 'Straight Lines',
    'Math10.pdf': 'Conic Sections',
    'Math11.pdf': 'Introduction to Three-dimensional Geometry',
    'Math12.pdf': 'Limits and Derivatives',
    'Math13.pdf': 'Statistics',
    'Math14.pdf': 'Probability'
}

# For Chem
Chemistry = {
"chem1": {
    'Chem101.pdf': 'Some Basic Concepts of Chemistry',
    'Chem102.pdf': 'Structure of The Atom',
    'Chem103.pdf': 'Classification of Elements and Periodicity in Properties',
    'Chem104.pdf': 'Chemical Bonding and Molecular Structure',
    'Chem105.pdf': 'Thermodynamics',
    'Chem106.pdf': 'Equilibrium',
},

"chem2": {        
    'Chem201.pdf': 'Redox Reactions',
    'Chem202.pdf': 'Organic Chemistry: Some Basic Principles and Techniques',
    'Chem203.pdf': 'Hydrocarbons',
}
}

# For Physics
Physics = {
"phy1": {
    'Phy101.pdf': 'Units and Measurements',
    'Phy102.pdf': 'Motion in a Straight Line',
    'Phy103.pdf': 'Motion in a Plane',
    'Phy104.pdf': 'Laws of Motion',
    'Phy105.pdf': 'Work, Energy and Power',
    'Phy106.pdf': 'System of Particles and Rotational Motion',
    'Phy107.pdf': 'Gravitation',
},

"phy2": {
    'Phy201.pdf': 'Mechanical Properties of Solids',
    'Phy202.pdf': 'Mechanical Properties of Fluids',
    'Phy203.pdf': 'Thermal Properties of Matter',
    'Phy204.pdf': 'Thermodynamics',
    'Phy205.pdf': 'Kinetic Theory',
    'Phy206.pdf': 'Oscillations',
    'Phy207.pdf': 'Waves'
}
}

# Provision for "other" files such as appendices and prelims

# others = {
#     ".*ps\.pdf$": "Prelims",
#     ".*an\.pdf$": "Answers",
#     ".*a1\.pdf$": "Appendices"
# }

def rename(file, chapter_name):
    # Main function for renaming

    old = base + file
    new = base + chapter_name + ".pdf"

    os.rename(old, new)
    


for key in math.keys():
    # looping through the dictionary keys for subject
    for n in glob.glob(base + "*.pdf"):
        # looping through files in base directory with .pdf extension
        
        file = os.path.basename(n) # gets the base name like "Math01.pdf" 

        # other_key = re.search(others.keys()) -> provision

        if file == key: # if base name = key from dictionary
            chapter_name = math.get(key) # get chapter name from dictionary
            
            rename(file, chapter_name)
            
            # For Debug:
            # print(f"{file}: {chapter_name}")
        
        # elif file == other_key: -> provision
            # pdf_name = others.get(other_key)
            # print(f"{file}: {pdf_name}")


