from libs import *

# Define global variables here

# End of global variables


# Import data from input files into global variables
def import_input(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            elements = line.replace('\n', "").split(" ")
            print(elements)
