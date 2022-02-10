
numbers = [2,3,5,7,11,13]

def plus_fifteen(input) :
    output = input+15
    return output
     
output_list = []

for number in numbers:
    product = plus_fifteen(number)
    output_list.append(product)

print(output_list) 





