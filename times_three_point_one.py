
numbers = [2,3,5,7,11,13]

def times_three_point_one(input) :
    output = input*3.1
    return output
     
output_list = []

for number in numbers:
    product = times_three_point_one(number)
    output_list.append(product)

print(output_list) 




