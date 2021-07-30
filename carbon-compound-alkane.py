print('-----------------------------------')
print('    Alkane component detector')
print('-----------------------------------')

n = input('Enter the numbers of carbon atoms: ')
n = int(n)
c = n*2+2
print('-----------------------------------')

if n == 1:
    print('name:- Methane')
elif n == 2:
    print('Name:- Ethane')
elif n == 3:
    print('Name:- Propane')
elif n == 4:
    print('Name:- Butane')
elif n == 5:
    print('Name:- Pentane')
elif n == 6:
    print('Name:- Hexane')
elif n == 7:
    print('Name:- Heptane')
elif n == 8:
    print('Name:- Octane')
elif n == 9:
    print('Name:- Nonane')
elif n == 10:
    print('Name:- Decane')

print('molecular formula:-'+'C'+str(n)+'H'+str(c))
