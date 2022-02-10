
numbers = [2,3,5,7,11,13] # Define our list

def plus_one(input): # Define our function
    output = input+1
    return output
     
output_list = [] # Create an empty output list

for number in numbers: # Iterate through our list
    product = plus_one(number) # Run our function on the item from the list
    output_list.append(product) # Add the output to our output list

print(output_list) # print the output list





