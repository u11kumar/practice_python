# Create a Python function that takes a sequence of comma-separated numbers as input and generates both a list and a tuple containing those numbers.

def convert_input_to_list_and_tuple(n):
    n=n.split(',')
    n=[int(i) for i in n]
    print((n,tuple(n)))


convert_input_to_list_and_tuple("3,6,5,3,2,8")
