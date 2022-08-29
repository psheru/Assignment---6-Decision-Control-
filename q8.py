#Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots.

a=int(input('Enter cofficient of a square:-'))
b=int(input('Enter cofficient of a:-'))

c=int(input('Enter constant term:-'))
D=b**b-4*a*c
if D>0:
    print('real and distinct roots')
elif D==0:
    print('real and equal roots')
else:
    print('imaginary roots')



