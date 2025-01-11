# Create a Python program that identifies all numbers between 100 and 300 (inclusive) that are divisible by 7 but not multiples of 5. The identified numbers should be displayed in a single line, separated by commas.
num1=100
num2=200

def find_numbers(num1,num2):
    for i in range(num1,num2+1):
        if i%7==0 and i%5 != 0:
                print(i,end=',')
            

find_numbers(num1,num2)