#5. Write a python script to print two given words in dictionary order.
a=input('enter first word:-')
b=input('enter second word:-')

if a>b:
    print(b,a,sep='\n')

else:
    print(a,b,sep='\n')
