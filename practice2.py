from math import sqrt

m = input('\nEnter the mass of object: ')
m = float(m)

s = input('\n value of distance released the object from height: ')
s = float(s)

g = 10.0

t = sqrt(2*s/g)

print('-----------------------------------------------')
print('\n1.Object taken time to reach on surface of earth = '+str(t) + 'sec')

v = g*t

print('2.Velocity of object on reaching to surface of the earth= '+ str(v) + 'm/s')
