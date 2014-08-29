"""
We want to open all the .txt files in a directory
Each file has multiple experiments.
We will make each experiment into a dictionary and only operate on
specific groups in the experiments.

"""

# These are the groups the program will look at.10.
groups = ["PR26", "PR15"]

# Open one file. and read all the lines as a list.
with open("!110909.txt", "r") as f:
    whole_file = f.readlines()

# Make the list as a single string.
whole_file = "".join(whole_file)
# Split the string into experiments.
experiments = whole_file.split("\n\n\n\n")

# Convert string into a dictionary.
#testing444
