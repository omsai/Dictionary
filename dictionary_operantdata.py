"""
We want to open all the .txt files in a directory
Each file has multiple experiments.
We will make each experiment into a dictionary and only operate on
specific groups in the experiments.

"""

# Directory where data will be pull.
import os
os.chdir (r'C:\Users\Héctor Contreras\Google Drive\PhD. Behavioral Neuroscience\Python\My programs\Dictionary\Dictionary_test\Dictionary\DATA')

# These are the groups the program will look at
groups = ["PR26", "PR15"]

# Open one file. and read all the lines as a list.
with open("!110909.txt", "r") as f:
    whole_file = f.readlines()

# Make the list as a single string.

whole_file = "".join(whole_file)

# Split the string into experiments.

experiments = whole_file.split("\n\n\n\n")
    
#Variables
A = 1
B = 2

# Convert string into a dictionary.
PR26 = {'LP':A , 'RT':B}
value = PR26['RT']
print (value)



          



