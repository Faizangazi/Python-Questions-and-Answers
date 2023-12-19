# String ==>

# (1). Identification = '' , " " , ''' ''' 
# (2). Idexing start from 0 and length start from 1 . 
# (3). Immutable Data type ==> We cannot change or update at a run time . 
# (4). Forward Indexing is start from 0 and Reverse(Backward) indexing is start from -1 . 
# Example 
# a = "sam" 
# print(a[0])   #fist element 
# print(a[1])   #second element 
# print(a[2])   #third element 

# print(a[-1]) # last element 
# print(a[-2]) #second last element 
# print(a[-3]) #third last element 

# slicing ==> [start_index : last_index+1]
# a = 'Good Morning'
# print(a[0:6])  # index ==> 0,1,2,3 ==>G,o,o,d 
# print(a[-1::-1])  #Reverse Indexing 
# print(a[5:])   #Morning  
# print(a[:4])   #Good 
# print(a[:])    #Good morning 

# methods - 
# (1). Concatenation 
# a = "Good" + "Morning" 
# a = "s" + "a" + "m" 
# print(a)

# (2). Replication 
# a = "123"*4 
# a = "sam"*4 
# print(a) 

# (3). lower() 
# a = "SAM" 
# n = a.lower() 
# print(n) 

# (4). Upper() 
# a = "sam" 
# p = a.upper() 
# print(p) 

# (5). replace() 
# a = "Hello Rohit" 
# b = a.replace("Rohit" , "Priya") 
# print(b) 

# (6). split() 
# a = "I love my India" 
# print(a) 
# b = a.split() 
# print(b) 

# (7). Find() .
# a = "sam krish" 
# b = "k" 
# print(a.find(b , 0 , len(a)-1)) 

# (8). len() 
# a = "sam" 
# print(len(a))  

# (9). isalnum()  ===> alphabat + number 
# a = "sam123"
# a = " "
# print(a.isalnum())  


# (10). isdigit() 
# a = "123" 
# a = "sam123"
# a = " "
# print(a.isdigit())

# a = "sam" 
# for i in a : 
#     print(i)

# method - 2  
# for i in a : 
#     print(i , end = ",")  

# # method - 3 
# for i in range(len(a)) : 
#     print(a[i])  

# String Formatting 
# name = "Rahul"
# age = 30 
# a = f"My name is {name} and I am {age} years old."
# print(a)

# Escape Sequence 
# a = "I love physics.\nThis is a great book."     #(\n we can change our line)
# print(a) 
# a = "I love physics.\tThis is a great book."     #(\t we can see space in new line)
# print(a) 

# LIST ==>

# Example :
# a = ['sam', 67 , 'Rahul', 89.45]
# print(a)
# print(type(a))
# print(a[0])   ==>First Element
# print(a[1])   ==>Second Element
# print(a[2])   ==>Third Element
# print(a[3])   ==>Fourth Element

# Slicing [start : last + 1]
# print(a[1:3])  # 67, 'Rahul'
# print(a[1:3])     # 'Rahul' , 89.45
# print(a[1:3])     # 'sam' , 67
# print(a[1:3])     # Extract all Elements

# Mutable Data Type ==>
# a = ['sam', 67 , 'Rahul', 89.45]
# print(a[2])
# a[2]='kriti'
# print(a)

# a = "sam"
# a[1]= 

#  Loops in list ==>
# a = ['sam', 67 , 'Rahul', 89.45]
# # Method-1
# for i in a:
#     print(i)

# # Method-2
# for i in range(len(a)):
#     print(i)

# Pre-Defined Function  ==>
# 1) Max - this function is used to find maximum number present in the list
# a = [1,2,3,4]
# print("max number is=" , max(a))

# 2) Min - this function is used to find minimum number present in the list
# a = [1,2,3,4]
# print("min number is=" , min(a))

# 3) append - this function is used to add an element in the last indexing of container.
# syntax - list.append(object)
# Example-
# a = ['sam', 67 , 'Rahul', 89.45]
# print(a)
# a.append('gourav')
# print(a)

# 4) Count - this method is used to count the frequency of the given object.
# syntax - list.count(object)
# Example-
# a = ['sam', 67 , 'Rahul', 67 ,'priya', 67]
# x = a.count(67)
# print("total frequency is=" ,x)

# 5) index - this function is used to find the index of the object/element.
# this function returns the first index of the object if it is found otherwise it returns an exceptions
# showing that the element is not present
# syntax - list.index(object)
# Example
# a = ['sam', 67 , 'Rahul', 67 ,'priya', 67]
# x = a.index('Rahul')
# print(x)

# 6) insert (index ,object) - this function is used to insert an object at a given indexing.
# syntax - list.insert(index ,object)
# Example
# a = ['sam', 67 , 'Rahul', 67 ,'priya', 67]
# print(a)
# a.insert(2,'Faizan')
# print(a)

# 7) Remove () - this method is used to delete an object from the given list.
# syntax - list.remove(object)
# Example
# a = ['sam', 67 , 'Rahul', 67 ,'priya', 67]
# print(a)
# a.remove(67)
# print(a)

# 8) Reverse ()-  this function is used to reverse an element present in the list.
# syntax - list.Reverse()
# Example
# a= [4 , 'Faizan' , 'Latur']
# print(a)
# a.reverse()
# print(a)

# 9) Pop () - this function is used to delete the last element from the list.
# syntax - list.pop()
# Example
# a = ['MERN' , 'Data Science' , 'Developer' , 'Google']
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)

# Q.1 ==> create a user defined list ?
# a = []
# size = int(input("Enter size:"))
# for i in range(size):
#     val = input("Enter item:")
#     a.append(val)
# print(a) 
   

# Tuple ==>

# Example -
# a = (45 , 'sam' , 89.45)
# print(type(a))
# a[1] = 'kriti'
# print(a)

# step -1 (convert your data into list)
# b = list(a)
# print("second step =" ,b)

# step-2 (assign your value)
# b[1] ='kriti'

# step -3 (convert your data into touple)
# c = tuple(b)
# print("third step = " ,c)

# creating tuple from existing sequences
# a = tuple("world")
# print(a)

# Traversing tuple
# a = (1 , 'Mahima' , 'pallavi' , 'aniket')

# method-1
# for i in a:
#     print(i)

# method-2
# for i in range(len(a)):
#     print(a[i]) 

# joining tuple
# a = (1,2,3,4)       
# b = (5,6,7)
# c = a + b
# print(c)

# Repeating or Replicating tuple
# a = (1,2,3)
# b = a*3
# print(b)

# slicing in tuple -
# a = (10,20,30,40,50,60)
# b = a[3:5]
# print(b)

# Example -
# 1) Length -
# a = ('sam' , 'rohan', 300 , 67.89)
# b = len(a)
# print("total length is=" , b)

# 2) Max() - this function returns max value of tuple
# syntax : max(tuple)
# a = (1,2,3,4,5,6,7)
# b = max(a)
# print("Max no is =" , b)

# 3)Min-
# b = Min(a)
# print("Min no is =" , b)

# 4) index - 
# syntax : tuple.index(obj)
# a = (10,20,30,40)
# b = a.index(30)
# print(b)

# Q.1) create a user defined tuple ?
# a = []
# size = int(input("Enter size:"))
# for i in range (size):
#     val = input("Enter item:")
#     a.append(val)
# b = tuple(a)    
# print(b)    

# 5) Count () - this function returns the frequency of a given element .
# Syntax : tuple.count(obj)
# Example-
# a = (10,20,30,10,40,10,20,50)
# b = a.count(10)
# print(b)

# creating tuple from keys of a dictionary
# a = tuple({1:"p" , 2:"q"})   # Extract all keys
# print(a)

# Tuple Manipulation-
# a = ('sam', 'rohan', 'rahul' ,'kriti')
# if 'sam' in a :
#     print("yes, this element is present in tuple...")
# else :
#     print("No, this element is  Not present in tuple...")

# 6) Delete tuple Element -
# a =('sam', 'rohan', 'rahul' ,'kriti')
# print(a)
# del(a)
# print(a)

# DICTIONARY ==>
# Example-
# a = {'brand':'kia','model':'celtos', 'year':2023}
# print(a)
# print(type(a))

# a = {'brand':'kia','model':'celtos', 'year':2023}
# b = a['brand']
# print(b)

# get() - 
# b= a.get("model")
# print(b)

# Loop in dictionary -
# a = {'brand':'kia','model':'celtos', 'year':2023}
# for i in a:               # Extract all keys
#     print(i)

# for i in a.keys():        # Extract all keys
#     print(i)

# for i in a.values():      # Extract all values
#     print(i)

# for x,y in a.items():      # Extract all keys & values
#     print(x,y)    

# Checking wheather a key exists in the dictionary or not -
# a = {'brand':'kia','model':'celtos', 'year':2023}
# if 'model' in a :
#     print('yes,this item is present...')
# else:
#     print('No,this item is present...')

# Adding a new element in dictionary -
# a = {'brand':'kia','model':'celtos', 'year':2023}
# a['km_driven'] = 50000
# print(a)

# Pre-defined functions
# 1) pop()-
# a = {'brand':'kia','model':'celtos', 'year':2023}
# print(a)
# a.pop('year')
# print(a)

# 2) popitem()-
# a = {'brand':'kia','model':'celtos', 'year':2023}
# print(a)
# a.popitem()
# print(a)
# a.popitem()
# print(a)

# 3) del-
# a = {'brand':'kia','model':'celtos', 'year':2023}
# del a['brand']
# print(a)

# 4) setdefault -
# a = {'brand':'kia','model':'celtos', 'year':2023}
# x = a.setdefault("color","white")
# print(a)

# 5) update -
# a = {'brand':'kia','model':'celtos', 'year':2023}
# x = a.update({"color":"black"})
# print(a)


# 4) SET ==>

# identification - { }
# Example -
# a = {'Good' , 'Bad' , 'High'}
# print(type(a))

# Type Casting to set -
# a = set (['mohit', 'karan' , 'deepak'])
# print(a)

# Adding Element to Set -
# a = {'Good' , 'Bad' , 'High'}
# print(a)
# a.add('Faizan')
# print(a)
# print(type(a))


# Difference between Normal set & Frozen Set
# Normal set -
# a = set (['a' , 'b' , 'c'])
# a.add('d')
# print(a)

# Frozen set -
# a = frozenset (['a' , 'b' , 'c'])
# a.add('d')
# print(a)

# Union of two SET -
# a = {'sam' , 'Pooja' , 'Aniket'}
# b = {'Aniket' , 'Manish'}
# c = a.union(b)
# print(c)

# Method -2
# c = a | b
# print(c)

# Intersection - (common element in sets)
# a = {'sam' , 'Pooja' , 'Aniket'}
# b = {'Aniket' , 'Manish'}
# c = a.intersection(b)
# print(c)

# Method-2
# c = a & b
# print (c)

# Difference of two Sets -
# a = {'sam' , 'Pooja' , 'Aniket'}
# b = {'Aniket' , 'Manish'}
# a-b ==> present in a but not present in b 
# c = a.difference(b)
# print(c)

# b-a ==> present in b but not present in a 
# c = b.difference(a)
# print(c)

# a.clear()  ==> for clear SET
# print(a)


# EXCEPTION HANDLING ==>

# while(True):
#     print("press q to Exit")
#     a = input("Enter Number:")
#     if (a =='q'):
#         break
#     try :
#         print("ok , continue....")
#         a = int(a)
#         if(a>7):
#             print("your Entered number is greater than 7 ...")
#     except Exception as e :
#         print("please enter a valid number..")
# print("Thanks for playing this game....")                






