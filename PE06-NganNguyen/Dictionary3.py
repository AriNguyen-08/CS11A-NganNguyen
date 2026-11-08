d1 = {'a': 100, 'b': 200, 'c':300}     #Create the first dictionary with 3 key-value pairs
d2 = {'a': 300, 'b': 200, 'd': 400}    #Create the second dictionary with 3 key-value pairs
result = {}      #Create an empty dictionary to store the result
for key, value in d1.items():           #Copy all key-value pairs from d1 to result
    result[key] = value
for key, value in d2.items():           #Loop through each key-value pair in d2
    result[key] = result.get(key, 0) + value #Add the value to the existing value, or start from 0
print(result)     #Print the combined dictionary