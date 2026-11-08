dict1 = {1:10, 2:20} #Create the first dictionary with two key-value pairs
dict2 = {3:30, 4:40} #Create the second dictionary with two key-value pairs
dict3 = {5:50, 6:60} #Create the third dictionary with two key-value pairs

new_dict = {}          #Create a new empty dictionary to store all the value
new_dict.update(dict1) #Add all the key-value pairs from dict1 to new dictionary
new_dict.update(dict2) #Add all the key-value pairs from dict2 to new dictionary
new_dict.update(dict3) #Add all the key-value pairs from dict3 to new dictionary
print(new_dict)        #Display the new dictionary
