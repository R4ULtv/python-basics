# BASIC OPERATIONS AND INPUT/OUTPUT

print('Hello World!!! ')            # PRINT FUNCTION
input('Write here --> ')            # INPUT FUNCTION

x = 4                               # CHECK variables.py
y = 2

addition = x + y                    # 6       
subtraction = x - y                 # 2
multiplication = x * y              # 8
division = x / y                    # 2.0   {the division operation return always a float type}
exponential = x ** y                # 16
floor_division = x // y             # 2
mod = x % y                         # 0     {the mod operation return the remainder of the division}

print(addition, subtraction, multiplication, division, exponential, floor_division, mod)

x = input('Insert a number: ')
y = input('Insert another number: ')
print(x+y)                          # {we entered 2 numbers, added them and then printed them}