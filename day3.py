#========================================OPERATOR======================================
'''
 operator

 arthematic operator
 +,-,*,%./

 //------------> discart value after decimal(just small integer)
 
 **---------->expontial
 a**b--->  a to power b

 conditional statement
 <,>,<=,>=,==,!=

 logical statement
 and=&&,or=||, not=!

# identity operator
 
 is operator
 whether reference belongs to same object

 print(a is b)-->false
 print(a is c)-->true

 indent is used to define body menas space and in same line
 minimum 1 space is required

 it is case sensitive language
'''
#=====================================upper and lower===================================================
'''
upper()---------->alphabet (lower--->upper) if any
lower()---------->alphabet (upper --->lower) if any

'''

#strip()----------->it delete the extra space from front and back from input




#*************************************************************************************************************************************************************************************
#  ==========================================================================if-else statement======================================================================================

'''
WAP  to determine whether a person is eligible to cast vote or not on the basis of followingf criteria
1)age
2)nationality

'''
#=================================================================code=======================================================
'''
age= int(input("enter your age:"))
nation= input("enter your nationality 'indian' or 'others':")

    #indiAn, INDIAn,InDIan
nation=nation.strip()

if age>=18 and nation.lower()=="indian":

      print("yes u r eligible")
      print("please vote for right person")

else:
      print("not eligible")

'''


      



#**********************************************************************************************************************************************************************************
#======================================================================================LOOP==========================================================================================

#for loop                                                                                      #  while loop
'''
1. iteration(cycles)dedpendent                                                    1.   condition dependent
2.  number:presume,known                                                         2.  unknown
3.  when no of cycle known                                                       3. when no of cycle unknown

4. balance-->5000 min bal:0  at once                                             4. we can withdraw 5000 at once,or 50*100 trasaction,while loop works

'''
#===================for loop============
'''
1)iterators(list,tuple,strings.....)
2)range()

syntax:
print(range(9))

for i in range(9)
   or
   for control_variable in range(5):

           body of for loop
'''
#=======RANGE========

#range(a,b,c)-->
#a=start value  b=end value   c=jump(update)       (start value sa start hota hai paar end value ko nahi lata hai vo ussa aak kaan chalta hai)
# in range we only used integer value we donot use any float value in range function and not even typecast that value


#=============================================================code==============================================================================
'''
for i in range(2,10,1):   #2,3,4,5,6,7,8,9
      print("welcome-->",i)

print("_"*20)                                                       #=============CODE========

for i in range(2,10,3):  #2,5,8
      print("welcome-->",i)
      
print("_"*20)

for i in range(10,2,-3):  #10,7,4
      print("welcome-->",i)
      print("done")
print("out of loop")

print("_"*20)

for i in range(-50,-5,-3):  #out of loop ,loop not executed , for it we have to do increment means (+2)instead of(-2)
      print("welcome-->",i)
      print("done")
print("out of loop")

'''



#range(a,b)--->
#a=start value  b=end value   c=jump(default +1)


'''
for i in range(5,10):  #5,6,7,8,9                                     #=============CODE========
      print("welcome-->",i)
      print("done")
print("out of loop")

print("_"*20)

 #range(b)--->
#a=start value(by default 0)       b=end value        c=jump(default +1)
'''
'''
for i in range(5):  #0,1,2,3,4
      print("welcome-->",i)
      print("done")                                                                 #=============CODE========
print("out of loop")
print("_"*20)
'''
#===========ITERATOR==========
'''
#for loop for iterator

s="apple"

for i in s:   #i="a","p","p","l","e"
      print("python")
      print(i)
'''
#==============================================================QUESTIONS==================================================================
  #QUE1:
 #WAP to display 10 natural number start from 1.
 #WAP to display n natural numbers start from 1.
 #add them and display result
 #1+2+3+4+......10=55

'''
for i in range(1,11):  #1,2
      print (i,end=" ")



print("_"*20)

for i in range(1,11):
      print (i,end=" + ")


print("_"*20)

sum=0
for i in range(1,11):
      if i==10:
            print(i,end=" = ")
      else:
            print(i,end=" + ")
      sum=sum+i   # sum=0+1=1,sum=1+2=3 ...
print(sum)

print("_"*20)

n=int(input("enter range:")) #100
sum=0
for i in range(1,n+1):  #1,2...5-99
      
      if i==n:
            print(i,end=" = ")
      elif i<4:
            print(i,end=" + ")
      elif i==4:
            print("..............",end=" + ")
            
      sum=sum+i   # sum=0+1=1,sum=1+2=3 ...
print(sum)     #1+2+3+......10=55
'''
#=================================================    #QUe2 WAP for multiple input i n loop ==============================================
      
#addition of all
#even addition
#odd addition
'''
n=int(input("enter range:"))
sum=0
for i in range(n):
      num=int(input("enter number:"))
      sum=sum+num



print(sum)

'''
#===================================number,even,odd,total==============================
'''
n=int(input("enter range:"))
sum_all=sum_even=sum_odd=0

for i in range(n):
     num=int(input("enter number"))
     sum_all=sum_all+num    #all
     #sum_all=sum_even+sum_odd

     if num%2==0:
           sum_even=sum_even+num    #even
     else:
           sum_odd=sum_odd+num        #odd

print("sum of even:",sum_even)
print("sum of odd:",sum_odd)
print("sum of all:",sum_all)
'''

#=======================================================while loop=====================================================

#while
'''
control_variable-initialized

while condition:
      #body
      #updation
'''

#============WAP to print numbers in reverse order start from n
      #n,n-1,n-2,n-3..........1
'''
n=int(input("enter upper limit:"))  #20 sa start

while n>0:
      print(n)    # in this we canot use increment decrement instead of it it use shorthand technique
      n-=1  #n=n-1
'''
#=====================================================break,continue,pass======jump statement=========================================================================

 #true-->boolean output
 #break--->loop immediately get terminated
 #continue-->loop get restart over next iteration
 #pass--->it is used to define body later , bypass block
     #ya sirf loop,function,class ko deleare karne ka liya use hota hai,jab huma kisi cheez ko baad me likhna ho




#==break==
'''
for i in "python":   #i='p','y','t'
       if i=='h':
             break
       print(i)

       or

s="python"
for i in range s:
         if i=='h':
              break
         print(i)
'''
#===continue===
'''
for i in "python":   #i='p','y','t'
       if i=='h':
             continue
       print(i)
'''
#==pass====
'''
s="eeeeeeeeeeeeeeeeeeeee"
for i in s:
      pass
def f1():
      pass
class A :
      pass

for i in range(10):
      if i%2==0:
            pass
      else:
            print(i)
            '''

#===true====


#==========================================================code========================================================================================================================
'''
for i in range(ord('a'),ord('z')+1):
      print (chr(i),end=" ")

'''
#three keywoord which start with capital letter are  (True,False,None)  except them all are in small letter
#==============que=================
#WAP to remove " from string s

'''
s='apple is "good" for health'    #string can be denoted by ''  if we use "" in string then we cannot enclosed it in "" we have to use ''

for i in s:
       if i=='"':
              continue
       print(i,end="")

'''
#WAP to remove all vowels from string s.
'''
s='apple is "good" for health'
v='AEIOUaeiou'

for i in s:
       if i in v:              # 'in' used to search,delete,or modify value inside string or number
              continue
       print(i,end=" ")

'''
#================que2=====
'''
while True:
       num1=int(input("enter first number"))
       num2=int(input("enter second number"))
       print("addition",num1+num2)

       ch=input("do you want to continue 'y' or 'n':")

       if ch=='y':
                continue
       elif ch=='n':
              print("thank you")
              break


'''
#=============que3========
'''
cp=cn=cz=0
while True:
       num=int(input("enter number"))
     
       c=0
       if num>0:
              print("positive")
              
              
       elif num<0:
              print("negative")
              
              
       elif num==0:
              print("zero")'''
       
'''  
       if num>0:
              cp=cp+1
       elif num<0:
              cn=cn+1
       else:
              cz=cz+1

       ch=input("do you want to continue 'y' or 'n':")

       if ch=='y':
                continue
       elif ch=='n':
              print("thank you")
              break
print("positive:",cp)
print("negative:",cn)
print("zero:",cz) 

'''
#============================nested loop=============================
'''
for i in range(3):
       print("outer loop-------------------------->",i)
       
       for j in range(5):
              print("inner loop---->",j)
'''

# for every iteration of outer loop ,inner loop get completely executed.



#armstrong:100 to 9000,plandrome:100 to 9000,table:20 to 30,prime


#======================planindrome=======================================
'''
for i in range(100,901):   #outer loop
          num=i
          sum=0
          while num>0:         #inner loop
                 last=num%10
                 sum=sum*10+last
                 num=num//10
          if i==sum:
                 print(i)
       
'''
#==================================pattern=========================================
'''
for i in range(4):   # i-->show row
       for j in range(8):  #j--->show column
              print("*",end=" ")
       print()

'''
#====hollow rectangle===
'''
for i in range(5):
       for j in range(8):
              if i==0 or i==4 or j==0 or j==7:
                     print("*",end=" ")
              else:
                     print(" ",end=" ")

       print()

'''

#==========================================LISTS=======================================

#list is one of the most important primitive datatype,ordered datatype
#in this we store multiple elements
#in this indexing is(zero based) or (negative as well)
#it is mutable datatype (in which changes occur), it allow duplication
#it is slower than tuple
#doneted by []
'''
#      0   1    2      3
list=[23,4.5,"shop",[1,2,3]]
#     -4  -3    -2       -1

print(type(list))
print(list)

print(list[2])
print(list[-2])
print(list[-1])
#     0    1       2        3      4
lis=[103,"viti","jabalpur",99.9,[98,99,98,99]]
print(lis)

lis[2]="bhopal"
print(lis)

print(lis[4])
print(lis)

print(lis[4][3])
print(lis)

lis[4][3]=89
print(lis)

'''

#-------slice--------  slicing is like a loop

#     0  1  2    3     4 5  6   7   8   9   10
'''
lis=[11,22,34,"hello",4,-5,44,"hi",567,455,33]
#  -11,-10
print(lis)

print(lis[3:8]) #run 1 less than indexing

a=lis[3:7]  # datatype of a is list
print(a)

b=lis[3:]  #if we have to print till last theen we can skip last indexing
print(b)
#  start,till,decrement
c=lis[7:2:-1]  # for reverse printing , for reverse order jump value should be negative
print(c)

c=lis[7:2:-2]  # for reverse printing
print(c)

rev=lis[::-1]
print(rev)

lis2=lis[:4]+lis[7:]  #two lis concatenate
print(lis2)
'''



#================================LIST FUNCTION================================

#============
#append()   ---->add on  -->only contain single value or list and add value from last  ,   it return no value(none)
#the value which return none ,call directly , it donot need any reference
#append cannot concartinate
'''
lis=[2,3,4,5]
print(lis)

a=lis.append(90)
print(lis)

lis.append(["shop","home"])
print(lis)

print(a)
lis=[2,3,4,5]
lis.append([22,45,65])  #it take list as an one index  [2, 3, 4, 5, [22, 45, 65]]
print(lis)
'''

#===============
#Extend (iterable) --->return none
#extend(list/tuple)
#extend cocatinate two list,it donot add list with value
'''
lis=[2,3,4,5]
lis.extend([22,45,65])  #it take individual value as index  [2, 3, 4, 5, 22, 45, 65]
print(lis)

lis=[2,3,4]+[34,45,56]
print(lis)
'''
#======
#WAP to create a list of element.
#also create a separate list for even and odd too.
'''
lis=[]

n=int(input("enter range:"))

for i in range(n):
       num=int(input("enter number:"))
       lis.append(num)
print(lis)


for i in range(n):
       num=int(input("enter number:")
even=odd=[]
if num%2==0:
            even.append(num)
print(even)

'''
#==================
#index(value)  --->return index number
#index(value,start,end)
'''
lis=[2,3,4,5,6,7,8,5,3,4,5]

a=lis.index(5)  #4
print(a)

b=lis.index(5)  #4
print(b)

c=lis.index(5,a+1)  #7
print(c)
'''

#===================
#count(value)  --->frequency return

#   WAP to find out the index number of element 5 , coming in list lis.(using loop)
'''
lis=[2,3,4,5,6,7,8,5,3,4,5,5]

#a=lis.count(5)
#print(a)

c=lis.count(5)#3
b=0

for i in range(c):
    a=lis.index(5,b)  #lis.index(5,0),lis.index(5,7)
    b=a+1 #3+1
    print(a)
'''
#========================
#max(),min(),sum(),len()

'''
lis=[2,3,4,5,6,7,8,5,3,4,5,5]

length=len(lis)
print(length)

mx=max(lis)
print(mx)

mn=min(lis)
print(mn)

s=sum(lis)
print(s)
'''
#------------------------------------------------------------
#sort()-->to sort list in ascending and desending
#it is inplace function---->inplace()----->None return--------> means no new object is formed,created nor destroyed -->, only position changed
'''
lis=[23,-8,56,6,7,-67]

lis.sort()    #by default in ascending
print(lis)  

lis.sort(reverse=True)   #for desending order
print(lis)
'''

#reverse()  --->used to reverse list--->inplace function
'''
lis=[23,-8,56,6,7,-67]
print(lis)
lis.reverse()
print(lis)
'''


#---------------------
#insert(index,value)
'''
lis=[23,-8,56,6,7,-67]
print(lis)
lis.insert(2,5000)
print(lis)
'''

#-------------------------------------------------------------------------------
#delete element  -->methods

#pop()  --->delete last element by default   ---->it also return deleted value
'''
lis=[23,-8,56,6,7,-67]
print(lis)
lis.pop()
print(lis)
deleted_value=lis.pop()
print(deleted_value)
'''
#pop(index)  --->delete value from middle
'''
lis.pop(2)
print(lis)
deleted_value=lis.pop(2)
print(deleted_value)
print(lis)
'''
#remove(value)  ---->return none
'''
lis=[23,-8,56,6,7,-67]
print(lis)
lis.remove(56)
print(lis)
'''
#clear()---->delete all
'''
lis=[4,5,6,7,8]
lis.clear()
print(lis)
'''

#delete statement  or del statement
'''
lis=-[4,5,6,7]

del lis   #it destroy data + reference --->permanently
print(lis)
'''
#===========================================================
#   WAP to create a list with a original list


'''
names=["ajay","sourabh","sumit","atul","aman"]

names2=[]

for i in names:  #i="ajay"
    
    if i[0]=='a':
        names2.append(i)
print(names2)
 '''       
        
#=================imp=================
'''
lis=[22,3,4,55,22,55,22,66,22]

lis1=[]

for i in lis:     # i=22  
    if i not in lis1:       #lis1=[22,3,4,55,66]
        lis1.append(i)
print(lis1)
'''
#==========que=============
#WAP to create a list of list
#[["1","ajay","bhopal"],["2","sohan","ujaana"],["3","sumit","bhopal"]]
'''
n=int(input("how many records do you want to insert"))
lis=[]              #parent list
for i in range(n):
    

     lis2=[rollno,name,address]
     lis.append(lis2)
print(lis)
     
'''
#==========================
#WAP to  create a list
#names=["ajay","sourabh","sumit"]
#addreses=["bhopal","indore","balaghat"]
#salary=["2000","30000","6000"]

'''
n=int(input("how many records do you want to insert"))
lis=[[],[],[]]

for i in range(n):
     
     name=input("enter name")
     address=input("enter addres")
     salary=int(input("enter salary"))

     lis[0].append(name)
     lis[1].append(address)
     lis[2].append(salary)
     
print(lis)     

m=max(lis[2])
print(m)
c=lis[2].count(m)
print(c,"record found")
b=0
for i in range(c):
    a=lis[2].index(m,b)
    print("name",lis[0][a])
    print("address",lis[1][a])
    print("salary",lis[2][a])
    print("="*23)
    b=b+1
'''
#==========================
#WAP for highest salary---->name address display  (2 person same salary whole detail) (max,count,index used)


#==================================

#WAP  con concatinate two list the coontent of two list  without zip
'''
names=["ved","raj","viti","avi","vansh"]
address=["bhopal","indore","ujjain","jabalpur","balaghat"]

lis=list(zip(names,address))
print(list(zip(names,address))) # it take one one element fron both list and zip them
'''



#==========================================================================================================================================================================
#==========================================TUPLES==========================================================================================================================
#TUPLE--->

#it is immutable and faster than list
#ordered, duplacation allowed
#no changes occur in tuple like list
#indexing negative as well
#denoted as ()

#stack ma variable or reference and heap ma object --> no new object is made if object is duplicate and their address are same
#we donot get access of stack memory only heap gave  accesss of memory


#index(),count(),max(),min(),len(),sum()
#if single element is in tuple than we have to use comma , after that,tuple is also reoresented by comma
'''
t=(23,)
print(type(t))
t1=9,34,45
print(type(t1))
'''
#name--->raj
'''
t=("sonam","ajay","rahul","karan")
t=t+("raj",)
print(t)

lis=list(t)
print(lis)
lis.insert(2,"raj")
print(lis)
t=tuple(lis)
print(t)
'''
#sorted()
t=("sonam","ajay","rahul","karan")
'''
lis=sorted(t)
print(lis)
t=tuple(lis)
print(t)

#any()-->boolean
#single element ->true  ,no element->false

t=()
print(any(t))

t1=(4,5,6)
print(any(t1))

'''

#=====================================================================================================\
#mutable-->list,set,dictionary
#immutable--->tuple,string,int,float
#=========================================================================================================/
#===========================================string==========================================================
#STRING
#it is immutable datatype
#two types to make empty string
'''
s=""
s1=str()
print(s)
print(s1)

s1="python"
print(s1[2],s1[-4])

s2="python is bad language"
s4=s2[:10]+"good"+s2[13:] 
print(s4)

'''
#upper(),lower(),capatilize()
#isalpha(),isdigit(),isupper(),islower()  --->boolean
'''
p="python is bad language"
print(p.upper())
s="python is bad language"
a=s.capitalize()
print(a)

'''

#=================================================================
#split()  --->by default split from space 

#join()
'''
s="have to learn python"
#a=s.split()
#print(a)

b="have to learn python.have learn.learn python"
m=b.split('learn')
print(m)

#rev=s[::-1]
#print(rev)

s1="have to learn python"
s1=s.split()   #['we','learn','python']
print(s1)

l=[]
for i in s1:
    #print(i[::-1])
    
   l.append(i[::-1])
print(l)                   #['ew','nrael','nohtyp']


# " ".join (iterable)

a='/'.join(l)
print(a)
'''
#========================================================================
#   WAP to manipulate a string as
'''
s="referesh"
#output: s="r$fr$sh"
#without using builtin function

s1=""

for i in s:  #i="r"
        if i=='e':
            s1=s1+'$'  #s1='r'+'$'="r$"
        else:
          s1=s1+i      #s1=""+'r'="r"
print(s1)
'''
#==========================================================================================================================================================
#==============================================================DICTIONARY================================================================================

#dictionary

#it is mutable datatype
#used mapping
#work on key-value/values pair

#key should be unique and made up of immutable datatype
#string,int,float,tuple.
#value can be anything-->it may be duplicate

#represented by {}
'''
d={}
r={1:"mon",2:"tue"}
c={1:"mon",2:"tue",1:"jan"}
s={2,4}

#if key are duplicate then it take latest value ,it overwrite previouse value
print(type(d))  #dic
print(type(s))   #set
print(type(r))    #dic

#key should be immutable.

print(c)
print(len(c))


l={1:"mon",2:"tue",3:"wed"}
print(l[2])
print(l)
l[2]="tuesday"  #mutation
print(l)

l[4]="thus"
l[5]="fri"      #extention
print(l)
'''
#Nested dictionary=========================
'''
d={"weeks":{1:"mon",2:"tue",3:"wed"},"months":{1:"jan",2:"feb",3:"mar"} }
print(len(d))

w=d["weeks"]
print(w)

print(d["months"][2]) #feb

d["weeks"][2]="tuesday"
print(d)


d["months"][3]="april"
print(d)
'''
#=======================================================
#keys(),values(),items()  -------->
'''
d={1:"mon",2:"tue",3:"wed"}

k=d.keys()
v=d.values()
i=d.items()

print(k)  #1,2,3
print(v)   #mon,tue,wed
print(i)

print(type(k))  #keys
print(type(v))  #values
print(type(i))   #iteams

#indirectly list function implement ---->list() typecast
s=sorted(k)  #in key we use tuple function,list
print(s)


for i in d:   #i is keys  d[i]=values
    print(i,d[i])

for i in k:
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)
    

for i,j in d.items():
    print(i,j)

'''

#packing ands unpacking
'''
lis=[[1,2,3],[4,5,6],[7,8,9]]

for i,j,k in lis:     # consistency should be maintened
     print(i,j,k)

'''
#get(),pop( key ),
#popitem()--->last element delete-->return deleted element
'''
d={1:"mon",2:"tue",3:"wed"}

v=d.get(2)#none
print(v)
v1=d[2]  #error
print(v1)

a=d.popitem()  #popitem
print(d)
print(a)

     
b=d.pop(2)  #in pop we have to pass key
print(d)
print(b)
'''

#update(dic)-->pass dictionary  ------>update,add,modify
'''
d={1:"mon",2:"tue",3:"wed"}
d.update({4:"THUS"})  #extend
print(d)
d.update({2:"tuesday"}) #mutation
print(d)
'''
#setdefault(key,value)  --->pass key,value --------->return value

#key already present -------------->no change---->return value
'''
d={1:"mon",2:"tue",3:"wed"}

r=d.setdefault(2,"fgg")
print(d)
print(r)

#key not present  ---->changes --------->return value

d={1:"mon",2:"tue",3:"wed"}

r=d.setdefault(22,"fgg")
print(d)
print(r)
'''

#==================QUESTION============================
#QUE3,2
'''
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}

d=d1.update(d2)
print(d1)
d2.update(d3)
print(d2)



d1={1:10,2:20}
d2={2:30,4:40}

d1.update(d2)
print(d1)
'''
#if we give any dic for iteration we donot latest update it aur add element in it
'''
d1={1:"mon",2:"tue",3:"wed",6:"sat",7:"sun"}
d={4:"thus",5:"fri"}

d2={}

for i in d1:  #i=1,2,3
    d2[i]=d1[i]   #d2={1:"mon",2:"tue",3:"wed"...update d}
    if i==3:
        d2.update(d)
print(d2)
'''
#====================
#wap to crate a dictionary d from a list lis such that element of list become key,corressponding frequency become value
'''
lis=[2,3,4,2,2,3,55,6,3,3,4]
#d={2:3,3:4,4:2,55:1,6:1}

d={}

for i in lis:
    d[i]=lis.count(i)
print(d)
'''    
#_________o_______________
'''
d1={}
for i in lis:
    if i in d1: #2
        d1[i]=d1[i]+1  #d1[2]=1+1=2
    else:
        d1[i]=1  #d1{2:1,3:1,4:1..}
print(d1)
'''
#=============================================================================================================================

#============================according to key
'''
d = {22: "vijay", -3: "raj", 2: "ajay"}

sort_d = dict(sorted(d.items()))

print(sort_d)
   
  #            OR
r=d.items()
n=sorted(r)
l=dict(n)
print(l)
#              OR

a=sorted(d.keys())
d1={}

for i in a:
     d1[i]=d[i]
print(d1)
'''
#======================according into value
'''
a=sorted(d.values())
d1={}

for i in a:  #i=aman
     for j,k in d.items():  #j=22,k=vijay
          if i==k:
               d1[j]=k
               break
print(d1)



'''
#================================================FUNCTION==========================================

#user defined function

#parameters
'''
1)parameter,returntype
1)parameter,no returntype
1)no parameter,returntype
1)no parameter,no returntype
'''
#=====1.)parameter,returntype================
'''
def add(a,b,c):
                    #body define
     result=a+b+c
                    #print(result)
     return result

add(4,5,6)  #value only return

print(add(2,34,5))  #direct display

r=add(2,3,4)  #by taking variable
print(r)

#add(34,5,6)  reuseable  ,but have to print every time

r1=add(266,300,4)  #by taking variable
print(r1)
r2=add(20,673,4)  #by taking variable
print(r2)
'''
#==================2)no parameter,no returntype========================


#=======multiple value return=================
'''
def arthematic(a,b):
     return a+b,a-b,a*b,a/b

r=arthematic(4,2)
print(r)    #result in tuple form
print("add:",r[0])
print("sub:",r[1])
print("mul:",r[2])
print("div:",r[3])
'''

#=============================================================================================================================================
#================que1=========================================
'''
#num=789000000887
num=int(input())
length=len(str(num))

#num=8280
sum=0
temp=num

while num>0:     #153=1*3+5*3+3*3
     last=num%10
     #sum=sum+(last**4)
     sum=sum+(last**length)
     
     num=num//10

if temp==sum:
     print("armstrong")
else:
     print("not a armstrong")

'''
#=========================from function================
'''
def armstrong(num):
        length=len(str(num))    
        sum=0
        temp=num  #preserve

        while num>0:                               #153=1*3+5*3+3*3
            last=num%10
                                                 #sum=sum+(last**4)
            sum=sum+(last**length)
            num=num//10

        if temp==sum:
               return "yes"
        else:
            return"no"

n=int(input("enter number:"))
r=armstrong(n)
print(r)
 '''             
 #=============armstrong between range===============
'''
def armstrong(l,u):
     for i in range(l,u+1):  #200,201,202,203....
        num=i #200
        length=len(str(num))    
        sum=0
  
        while num>0:                               #153=1*3+5*3+3*3
            last=num%10
            sum=sum+(last**length)
            num=num//10

        if i==sum:
               print(i)

lower=int(input("enter upper limit:"))  #200
upper=int(input("enter upper limit:"))   #2000
armstrong(lower,upper)
'''

#============default parameter=============
#scope of variable

# isma pehle non default value dena hota aur phir uska baad default value
'''
def add(a,b,c,d=0):
     print(a+b+c+d)
     
def add(a=0,b=0,c=0,d=0):
     print(a+b+c+d)

add(3,4,5,6)
add(2,3,4)
add(4,5)
'''
#====================================================PROJECT=========================================================


#function based project  , function calling inside function body

#create a console based small project,employee management system.
#insert(),display(), search(), filter(),etc


#============================================================================================================================================================
#====================================================IMP==============================================

#lamda,filter,map,decorator,generator,reduce.

# ->lambda--->anonymous function,function without name


'''
f=lambda a,b,c:a+b+c
print(f(3,45,5))


f=lambda a,b : a if a>b else b
print(f(23,45))

f=lambda a,b : "yes" if a<b else "no"
print(f(23,45))

f=lambda a,b : "yes" if a<b else "no"
a=int(input())
b=int(input())
print(f(a,b))

'''

#syntax
#map(function,iterable)
#filter(function,iterable)
#reduce(function,iterable)

#========================================
#map()------->output------->iterator---->container(list,tuple,loop) can be used
'''
def cube(a):
     return a*a*a

print(cube(5))   #cube of 5


def cube(a):
     return a*a*a

lis=[1,2,3,4,5]
a=map(cube,lis)    #give addresss
print(a)

a=list(map(cube,lis))    #type cast by list to act as container to get cube of all element of lis
print(a)

for i in map(cube,lis):   #using loop
     print(i)
     


r=list(map(lambda a: a*a*a,lis))   #using lambda
print(r)
'''
#-------------------------------------------------------------------------------------------------

#map is a special function which has two argument 1st is function second is iterable ,it take element from iterable ,pass it to function and then function processed and store value as output

#map takes every single value from iterable,and send it to function , to perform operations,and holds results.

#lambda is a one line,anonymous function ,it work with map,filter,etc.it has two part one for define it and second for condition

#map function work with normal function as well as with lambda function.

#-----------------------------------------------------------------------------------------------------

#filter()


# it take value from list one by one to perform operation
'''
lis=[1,2,3,54,67,88]
def even (a):
     if a%2==0:
       return True
print(list(filter(even,lis)))
'''
'''
li=[["viti",24000],["ti",6000],["vi",77000]]

def salary(a):
     if a[1]>23000:
        return True
     
print(list(filter(salary,li)))
'''
#******************IMP*******************************************
#generator()
'''
def produce():
     return"done"

print(produce())
'''
#yield---------->control goes again to function to take accsess of next iterator--->produce
'''
def produce():
       yield "intro"
       yield "to"
       yield "genetator"

a=0

print(produce())



def range1 (n):  #iterator=9
     i=0
     while i<n:
            yield i #1
            i=i+1

for i in range1(9):
       print(i)

'''


#=======================================decorator function===============================================================================
#
#it is also known as wrapper function
#it enhance the functionality of a eixsting function
#we define function inside function
#special symbol used '@'
'''
def wrapper(f):   #  f->add
    def modify(a,b):
        f(a,b)
        print("sub",a-b)
        print("mut",a*b)
        print("div:",a/b)
    return modify

@wrapper
def add(a,b):
    print("add",a+b)

add(3,4)
'''

#WAP to define a f() named square,which can find the square of number use decorator f(), to modify behaviour also perform the cube of that n0.


def wrapper(f):   #  f->add
    def modify(a):
        f(a)
        print("cube",a*a*a)
       
    return modify

@wrapper
def square(a):
    print("sq",a*a)

square(3)


#wap to define a function create_list(empty list),use decoretor function find max,min,sort


def wrapper(f):   #  f->add
    def modify(a):
          f(lis)
          #mix,min,sort
          
          print( max(lis))
          print(min(lis))
          lis.sort()
          print(lis)
    return modify

@wrapper
def create_list(lis):
    #list create -->n-->loop--->list
    n=int(input("enter range:"))

    for i in range(n):
        num=int(input("enter number:"))
      
    print(num)

a=[]
create_list(a)


#============reduce function===================


































    
