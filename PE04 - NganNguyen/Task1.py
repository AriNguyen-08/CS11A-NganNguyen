guests = ['Anna', 'John', 'David', 'Emma']   #Create a list of 4 guests to invite to dinner
print("My dinner guests list:", guests)      #Print the original guests list

guests[1] = 'Sophia'                         #Replace John with Sohia because John cannot join
print("Guest list after replacement:", guests) #Print the updated guest list

guests.insert(0,'Michael')                    #Insert Michael at the beginning of the list
guests.insert(3,'Olivia')                     #Insert Olivia in the middile of the list
guests.append('James')                        #Appened James at the end of the list
print("My new guest list:", guests)           #Print the updated guest list

while len(guests) > 2:                        #Remove guests one at a time until only two remain
    removed_guest = guests.pop()              #Remove the last guest from the list
    print(f"Hi {removed_guest}, I am sorry I won't be able to have you over for dinner this time.")  #Print a message to the guest who was removed
print("My final dinner guest list:", guests)  #Print the two remaining guests

