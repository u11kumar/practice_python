# Create a Python function that takes an integer ( n ) as input and generates a dictionary containing pairs ( (i, i^2) ) for all integers ( i ) from 1 to ( n ) (inclusive). The function should then return this dictionary.


def generate_square_dict(n):
    square_dict={}
    for i in range(1,n+1):
        square_dict[i]=i**2
    return square_dict

my_dict=generate_square_dict(8)
print(my_dict)