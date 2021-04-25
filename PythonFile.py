import re
import string


# Produces a list of all items purchased in a given day along with the number of times each item was purchased.
def DisplayAllItems(): 
    infile = open("CS210_Project_Three_Input_File.txt", "r") # Opens file
    lines = infile.readlines() # Reads file
    infile.close() # Closes file
    words_dict = {} # Creates dictionary
    for x in lines: # Loop to count items
        x = x.strip()
        if x in words_dict:
            words_dict[x] += 1
        else:
            words_dict[x] = 1
    
    for x in words_dict:
        print('{} was purchased {} times'.format(x, words_dict[x]))
        
# Produces a number representing how many times a specific item was purchased in a given day.
def DisplaySpecificItem(item): 
    infile = open("CS210_Project_Three_Input_File.txt", "r")
    lines = infile.readlines()
    infile.close()
    words_dict = {}
    for x in lines:
        x = x.strip()
        if x in words_dict:
            words_dict[x] += 1
        else:
            words_dict[x] = 1
    if item in words_dict:
        print('{} was purchased {} times'.format(item, words_dict[item]))
        return words_dict[item]
    else:
        print('Item does not exist.')
        return 0

# Produces a text-based histogram listing all items purchased in a given day, along with a representation of the number of times each item was purchased.
def DisplayHistogram(): 
    infile = open("CS210_Project_Three_Input_File.txt", "r") # Opens file
    lines = infile.readlines() # Reads file
    infile.close() # Closes file
    words_dict = {} # Creates dictionary
    for x in lines: # Loop to count items
        x = x.strip()
        if x in words_dict:
            words_dict[x] += 1
        else:
            words_dict[x] = 1
    outfile = open("frequency.dat", "w") # Creates new file
    for x in words_dict: # Loop to write items to file
        outfile.write(x + " " + str(words_dict[x] + "\n")) 
    outfile.close()        
    
        
        
        
        
        
