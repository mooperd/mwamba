import math

numbers = [2,3,5,7,11,13] # Define our list

def calc_sin(input): # Define our function
    output = math.sin(input)
    return output
     
output_list = [] # Create an empty output list

for number in numbers: # Iterate through our list
    product = calc_sin(number) # Run our function on the item from the list
    output_list.append(product) # Add the output to our output list

print(output_list) # print the output 
