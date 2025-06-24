import math

def calc(n):
    print('Square root:', math.sqrt(n))
    print('Logarithm:', math.log(n))
    print('Sine:',math.sin(n))

num = int(input("Enter a number : "))
calc(num)