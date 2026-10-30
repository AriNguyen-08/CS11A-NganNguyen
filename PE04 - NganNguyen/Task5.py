def second(n):        #Define a function to get the second element of the tuple
    return n[1]       #Return the second element at index 1

def sort_list(tuples): #Define a function to sort a list of tuples
    return sorted(tuples, key=second)   #Sort the tuple based on the second element

numbers = [('425',10), ('256',5), ('100',20), ('135',15)]   #Create a list containing four tuples
print(sort_list(numbers))     #Print the sorted list of tuples
