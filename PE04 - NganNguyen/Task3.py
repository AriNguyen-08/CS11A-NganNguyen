numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]  #Create a list containing duplicate numbers
output_list = []   #Create an empty list to store duplicate numbers
for i in numbers:  #Use a loop to go through each number in the list
    if numbers.count(i) > 1 and i not in output_list:    #Check if the number appears more than one time and is not already in the new list
        output_list.append(i)    #Add the duplicate number in the new list
print("output_list =", output_list)
