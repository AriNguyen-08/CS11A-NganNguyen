n = int(input("Enter a number: "))    #Ask the user to enter a number
numbers = {}                 #Create an empty dictionary
for x in range(1, n + 1):    #Use a loop to go through numbers from 1 to n
    numbers[x] = x ** 2      #Add each number as a key and its square as its value
print(numbers)               #Print the dictionary

