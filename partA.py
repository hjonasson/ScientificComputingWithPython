#Part A, Python as a calculator

import numpy as np

#1

f11 = lambda x: np.sin(x)/x
print 'sin(x)/x for 3.3, 1.2 and .1 are -> ' + str(f11(3.3)) +' '+ str(f11(1.2)) +' '+ str(f11(.1))

print 'Trying to evaluate it at x=0 gives syntax error'
print 'The modulus of a complex number in python is found with the regular abs() function. The modulus of 3.5 + 5j is ' + str(abs(3.5+5j))


