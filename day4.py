#WAP to print a natural number from 1 to n

'''
n=int(input("enter any number:"))
for i in range(1,n+1):
             print(i,end=" ")
    
'''
#WAP to print a natural number in reverse
'''
n=int(input("enter natural number:"))

for i in range(1,n+1):
      if n>0:
          print(n,end=" ")
          n=n-1
'''

#WAP to print tables
'''
n=int(input("enter natural number:"))

for i in range(1,11):
    if(i<=10):
        s=n*i
        print(s,end=" ")
'''

#WAP yo print table in reverse
n=int(input("enter natural number:"))

for i in range(1,11):
    if(i>=0):
        s=n*i
        print(s,end=" ")
        s=s-1
