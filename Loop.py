
# Loop
# 1) For Loop  
# 2) while Loop

# 1) For Loop ==>
# index start= 0   ,  Length start= 1

# Method 1 -
# for i in range (1,6):
#     print(i)

# Method 2 -
# for i in range (1, 15, 3):
#     print(i)

# Method 3 -
# a = "SAM"
# for i in a:
#      print(i)

# a = "SAM"
# for i in a:
#      print(i, end = " ")     

# a = "SAM"
# for i in a:
#      print(i, end = " , ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# While Loop ==> 1)Initialization  2)Condition  3)increment/decrement

# Q1) write a program who print 1 to 5 ?
# i =1
# n =5  ==> initialization point
# while(i<=n):  ==> condition
#     print(i)
#     i = i+1   ==> increment

# output ==> 1, 2, 3, 4, 5

# step-1
# i = 1 ,  n = 5
# while(1<=5):  
#      print(1)
#      i = 1+1  = 2

# step-2
# i = 2 ,  n = 5
# while(2<=5):  
#      print(2)
#      i = 2+1  = 3

# step-3
# i = 3 ,  n = 5
# while(3<=5):  
#      print(3)
#      i = 3+1  = 4

# step-4
# i = 4 ,  n = 5
# while(4<=5):  
#      print(4)
#      i = 4+1  = 5

# step-5
# i = 5 ,  n = 5
# while(5<=5):  
#      print(5)
#      i = 5+1  = 6

# step-6
# i = 6 ,  n = 5
# while(6<=5):   # False condition
#     break    

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# write a program who take user according values as like starting value, end value and gap value ?
# i = int(input("Enter First Value:"))
# n = int(input("Enter Last Value:"))
# p = int(input("Enter Gap:"))
# while(i<=n):
#      print(i)
#      i = i+p


# Q1. write a program who print 10 to 1 by while loop
# i =10
# n =0
# while(i>0):
#     print(i)
#     i = i-1

# Q2. write a program who print from 10  to 30 with difference of 6 by for loop
# for i in range (10, 30, 6):
#     print(i)

# Q3. write a program to find sum of square from 1 to n ?
# 1,2,3,4 ==> 1**2+2**2+3**2+4**2 = 1+4+9+16 =30

# i = 1                   # initialization point
# n = int(input("Enter Last Number"))
# sum = 0
# while(i<=n):
#     sum = sum + (i*i)   # condition
#     i = i + 1           # increment
#     print("Addition =" ,sum)

# step-1
# i = 1 
# n = 4 
# sum=0
# while(1<=4):
#     sum = 0 + (1*1) =1
#     i = 1+1 =2

# step-2
# i = 2
# n = 4 
# sum=1
# while(2<=4):
#     sum =1+(2*2) =5
#     i = 2+1 =3

# step-3
# i = 3
# n = 4 
# sum=5
# while(3<=4):
#     sum =5+(3*3) =14
#     i = 3+1 =4

# step-4
# i = 4
# n = 4 
# sum=14
# while(4<=4):
#     sum =14+(4*4) =30        ==> ERROR
#     i = 4+1 =5

# Q4. write a program to print only even numbers 2 to n ?
# i =2
# n =int(input("Enter last number"))
# while(i<=n):
#     print(i)
#     i =i+2

# step-1 
# i =2
# n =15
# while(2<=15):
#     print(2)
#     i =2+2 =4


# step-2 
# i =4
# n =15
# while(4<=15):
#     print(4)
#     i =4+2 =6


# step-3
# i =6
# n =15
# while(6<=15):
#     print(6)
#     i =6+2 =8

# step-4
# i =8
# n =15
# while(8<=15):
#     print(8)
#     i =8+2 =10

# step-5
# i =10
# n =15
# while(10<=15):
#     print(10)
#     i =10+2 =12

# step-6
# i =12
# n =15
# while(12<=15):
#     print(12)
#     i =12+2 =14

# step-7
# i =14
# n =15
# while(14<=15):
#     print(14)
#     i =14+2

# step-8
# i =16
# n =15
# while(16<=15):        ==> ERROR
#     break  


