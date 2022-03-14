import fibonacci as f
from struct import *

def generate_key(key_start):
    #blowfish has a variable key range of 32-448 bits, we will be using 32 bit keys for convenince 
    
    fibo_number = f.Fibonacci(key_start)
    print(fibo_number)
    #to make sure that the value of the key is 32 bit,by taking the module of the largest 32 bit number
    fibo_number = fibo_number%9999
    key = pack('I',fibo_number)
    return key



