"""
We want to open all the .txt files in a directory
Each file has multiple experiments.
We will make each experiment into a dictionary and only operate on
specific groups in the experiments.

"""

# These are the groups the program will look at.
groups = ["PR26", "PR15"]

# Open one file. and read all the lines as a list.
with open("!110909.txt", "r") as f:
    whole_file = f.readlines()

# Make the list as a single string.
whole_file = "".join(whole_file)
# Split the string into a list.
experiments = whole_file.split("\n\n")

data = []

# Convert each string into a dictionary.
for experiment in experiments:
    dic = {}
    for line in experiment.splitlines():
        key, value = line.split(":", maxsplit=1)
        # Remove spaces from the key and value strings.
        key = key.strip()
        value = value.strip()
        # Add to the dictionary.
        dic[key] = value
    data.append(dic)

# The very first entry is not an experiment, but the original file name.
# Save the filename and remove it from the experiments list.
orig_filename = experiments.pop(0)

print("Read", len(data), "experiments from", f.name)

# Now that we have the data we can read things about it.
#
# For example, this finds how many of the groups we are interested in.
for group in groups:
    counter = 0
    experiment_h = []
    print("Finding experiments that match group", group, "...")
    for i in range(len(data)):
        # Not all datasets have a group!
        if data[i].get("Group") != None:
            if data[i]["Group"] == group:
                counter += 1
                experiment_h.append(float(data[i]["H"]))
    print("...found", counter, group, "groups.")
    # Print additional info about experiments that match the group.
    if experiment_h != []:
        print("The", group, "groups have H values of:")
        print(experiment_h)
