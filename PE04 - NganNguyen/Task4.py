foods = ['Pizza', 'Chicken', 'Rice', 'Salad', 'Pasta']    #Create a tuple containing five foods
print("Original menu:")            #Print the original menu
for food in foods:                 #Use a loop to print each food
    print(food)                    

food[0] = 'Burger'                 #Try to replace Pizza with Burger

foods = ['Burger', 'Chicken', 'Rice', 'Salad', 'Soup']   #Create a new tuple replacing Pizza and Pasta with Burger and Soup
print("Revised Menu:")             #Print the updated menu
for food in foods:                 #Use a loop to go print each food in the new menu
    print(food)