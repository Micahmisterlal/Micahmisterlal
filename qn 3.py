import math
f = int(input('please enter f,' ))
R = int(input('please enter R,' ))
C = int(input('please enter C,' ))
#log10 is equal to 20 log
firstfx = 20
secondfx = 1 / (2*math.pi * f * R * C ) 
Gain = firstfx * secondfx
print(Gain)