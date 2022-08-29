#12. Write a python script to accept one complex number from the user and display the
#greater number between real part and imaginary part.

x=complex(input("Enter number:-"))
y=x.real
z=x.imag
if y>z:
    print(y)
else:
    print(z)

