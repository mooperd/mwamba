
numbers = [2,3,5,7,11,13]

def plus_thirteen(input) :
    output = input+13
    return output
     
output_list = []

for number in numbers:
    product = plus_thirteen(number)
    output_list.append(product)

print(output_list) 





