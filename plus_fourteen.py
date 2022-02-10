
numbers = [2,3,5,7,11,13]

def plus_fourteen(input) :
    output = input+14
    return output
     
output_list = []

for number in numbers:
    product = plus_fourteen(number)
    output_list.append(product)

print(output_list) 





