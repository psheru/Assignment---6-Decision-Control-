#10. Write a python script to print greater among three numbers. Print number only once
#even if the numbers are the same.

n1=int(input("Enter the first number:-"))
n2=int(input("Enter the second number:-"))
n3=int(input("Enter the third number:-"))
if n1>n2:
   print(n1)
elif n1<n2>n3:
    print(n2)
else:
    print(n3)
