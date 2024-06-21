import math
L = int(input('please enter L'  ))
C = int(input('please enter C'  ))
r = int(input('please enter r'  ))
firstn = (1 / 2*math.pi) * (1 / L*C ) **1/2 
secondn = (r **2/3) / 4*L**2 
fres = firstn - secondn
print(fres)