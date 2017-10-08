#!/usr/bin/env/Python3

# hash tag

import sys

print(sys.maxsize)   # python2 limit for int

print(type(sys.maxsize+1))   # python2 long

e = 2.718   # float
print(type(e))

z = 3 + 5.7j   # complex numbers i=j
print(type(z))
print(z.real)
print(z.imag)

print(" 'ass' ")
print(' "ass" ')
print(""" "ass" 'ass' """)

# arithmetic

# convert int to float OK
x = 28
y = 28.0
yy = x/1.0
yyy = float(x)
print(yy, yyy)

# float to int NO
print(int(3.14)) # first rounded
# ints are narrower than floats
# floats are wider than ints

# float to complex number OK
x = 1.732
y = x + 0j
yy = complex(x)
print(y, yy)

# complex to float NO
# float(y)
# floats are narrower than complex numbers
# complex numbers are wider than floats


# Operations: +addition -substraction *multiplication /division

# Rule: Narrower numbers are converted to wider, than python performs the operation

