# What is Data ? 
# What is DBMS ? 
# What is MYSQL ? 
# Difference between Relational Database or Non-Relational Database ? 

# (1). Data ==> Data is a unit , any kind of length , width , time etc .. 

# (2). Database ==> Database is a collection of information organized for easy to access , management and maintainance .


# Types of Data Models  
# (1). Record Based Logical Model 
# (a). Hierarchical Data Model 
# (b). Network Data Model 
# (c). Relational Data Model 

# (a). Hierarchical Data Model ==> A hierarchical database is a data model in which data is stored in the form of records and organized into a tree like structure . 

# Example ==> 
# Electronic ==> 1. Televisions ==> (Tube , LED , Plasma) 
# 2. Portable Electornics ==> (MP3 PLAYER , CD Players , 2 Way Radios),
# 3. MP3 PLAYER ==> FLASH  


# parent Node ==> Child Node1 ==> Child Node2 ==> Child Node3 ....Child Node N  

# (b). NETWORK DATA MODEL ==>  A network database model is a database model that allows multiple records to be linked to the some owner files . The model can be seen as an upside down tree where branches are the member informarion linked to the owner which is the bottom of the tree . 
# Example ==>
# Store ==> 1. Customers ==> Orders  2 . SalesMan ==> Items 
# Manager  


# (c). Relational Database Model ==> This model represents how  data is stored in Relational Database . A relational database stores data in the form of relation(Tables) . 

# Example ==> 
# Company Amazon ==> Sales Data , Employee Data , Orders  Data 

# Introduction to RDBMS(Relational Database Management System) ==> 
# 1. A relational database refers to a database that stores data into a structured format , using rows and columns .
# 2. This makes it easier to locate and access specific values within the database . 
# 3. It is "relational" because the values within each table are related to each other . 

# Features of RDBMS  : 
# (1). Every piece of information is stored in the form of tables. 
# (2). RDBMS has primary keys for unique identifications of rows . 
# (3). RDBMS  has foreign keys to ensure data integrity . 
# (4). Uses indexes for faster data retrieval .    

# Difference between RDBMS and Traditional Approach ? 
# 1. The key difference is that RDBMS  applications stores data in a tabular form(rows and columns) whereas in traditional aproach applications store data as file . 

# 2.  There can be but there will be no "relation" between the tables , like in a RDBMS . In traditional approaches , data is generally stored in either a hirarchical form/navigational form . This meanss that is a single data unit will have 0,1 or more children nodes and one parent node . 

# DBMS Oerations ===> 
# 1. DBMS  is a software which is used to manage the database . 
# Example => MySQL , Oracle . 

# 2. It provides protection and security to the database .In the case of multiple users , it also maintain data consistencey . 

# Q.1.How to create a Database ? 
# create DataBase NameofDataBase ; 

# Q.2 How to drop a Database ?
# drop database Nameofdatabase ;  

# By default ==> local host = 127.0.0.1  

# Q.3 How to create a table ?
# create table Emp_info(
#     emp_id int  , 
#     emp_name varchar(50),
#     emp_designation varchar(50),
#     salary int 
# );

# select * from Emp_info ;

# Q.4 How to insert a data in a table ?
# insert into emp_info VALUES (1 , "Sam" , "Data Analyst" , 50000);
# select * from emp_info ;  

# Task  
# Library ==> customer ==> checkout , return , book borrow ? 
# Emp Information 

# Monday ==> test 
# (1). NumPy (2). Pandas (3). How to create table in a database ? (4). What are features of RDBMS ? (5). How RDMS is different from traditional approaches ? 



# MySQL Data Types 
# 1. Numeric Types 
# a. TINYINT 
# b. SMALLINT 
# c. MEDIUMINT 
# d. INT 
# e. BIGINT 
# f. FLOAT 
# g. DOUBLE 
# h. DECIMAL 


# 2. Date and Time types 
# a. DATE 
# b. TIME 
# c. DATETIME 
# d. TIMESTAMP 
# e. YEAR 


# 3. String Types 
# a. CHAR 
# b. VARCHAR
# c. TINYTEXT 
# d. TEXT 
# f. MEDIUMTEXT
# g. LONGTEXT 
# h. ENUM
# i. SET  


# 4. Binary Types 
# a. Binary
# b. Varbinary
# c. Tinyblob
# d. Mediumblob
# e. Longblob 
# f. Blob 

# 5. Spatial Types 
# a. Geometry
# b. Point 
# c. Linestring 
# d. Polygon 
# e. Multipoint 
# f. MultilineString 
# g. Multipolygon 
# h. Geometrycollection 

# 1.  Numeric Types 
# (a).TinyInt ==> We use tinyint for small integer values (-128 to 127) and boolean flags (0 or 1). 
# (b). Smallint ==> We use smallint for large integer values (-32 ,768 to 32 ,767).
# (c). INT ==>  we use in for even large integer values (-2 , 147 , 483 , 648 to 2,147,483,647).
# (d).BIGINT ==> we use bigint for large integer values (-9,223,372,,036,854,775,808 to 9,223,372,,036,854,775,807).
# (e). Float ==> we use FLOAT  or Double for floating point numbers . 
# (f). Decimal ==> We use Decimal for extract decimal values that requires precision , such as financial data . 

# Implementation 
# create table find_numeric_dtypes(
#     tiny_int_col TINYINT , 
#     small_int_col SMALLINT , 
#     int_col INT ,
#     big_int_col BIGINT,
#     float_col FLOAT(4),
#     double_col DOUBLE(8 , 2),
#     decimal_col DECIMAL(10,2)
#     );
    
# select * from find_numeric_dtypes ;
# insert into find_numeric_dtypes VALUES
# (127 , 34567 , 214748957 , 9223344739689465788 , 3.14 , 1234.25 , 56789.45);

# select * from find_numeric_dtypes ; 



# 2. Date and Time types 
# a. DATE ==> We use data for storing dates in the format YYYY-MM-DD . 
# b. TIME ==> We use time for storing tiems in the format HH:MM:SS . 
# c. DATETIME ==> We use DATETIME  for storing dates and times in the format YYYY-MM-DD HH-MM-SS.
# d. TIMESTAMP ==> We use timestamp for storing dates and time in a more compact format (YYYYMMDDHHMMSS).
# e. YEAR  ==> We use YEAR  for storing years in a 2-digit(70-80) or 4-digit(2021-2024). 


# Implementation 
# create table find_date_dtypes(
#     date_col DATE , 
#     time_col TIME , 
#     datetime_col DATETIME , 
#     timestamp_col TIMESTAMP , 
#     year_cool YEAR 
# );

# select * from find_date_dtypes ; 

# insert into find_date_dtypes
# VALUES
# ('2023-09-26' , '08:43:20' , '2023-09-26 08:43:20' , '2023-09-26 08:43:20' , '2023');

# select * from find_date_dtypes; 



# (3). String types 
# (a).  CHAR ==>  we use CHAR  for fixed length-strings , such as postal codes or product codes . 
# (b). VARCHAR ==> we use VARCHAR for variable-length-strings , such as names or address . 
# (c). TEXT ==> we use TEXT for large blocks of text , such as product descriptions or blog post . 
# (d). ENUM ==> we use ENUM or SET  for storing a predefined list of options or categories . 

# Implementation 
# create table find_string_dtype(
#     char_col CHAR(10),
#     varchar_col varchar(255),
#     tinytext_col TINYTEXT , 
#     text_col TEXT , 
#     mediumtext_col MEDIUMTEXT , 
#     longtext_col LONGTEXT , 
#     enum_col ENUM('A' , 'B' , 'C'),
#     set_col SET('A' , 'B' , 'C')
#     );
    
    
# select * from find_string_dtype ; 

# insert into find_string_dtype
# VALUES
# ('example' , 'example string' , 'tiny text' , 'text' , 'medium text' , 'long text' , 'A'  , 'B');

# select * from find_string_dtype ; 


# Null And Not Null in MYSQL  ==> 
# (1). Nullable Column(NULL) ==> When a column allows NULL ,  it means the absence of a value is considered a valid state . 
# Example ==> 
# If we have column "middle_name" in a table for storing customer's names , then we define it as NULL because not all individuals have a middle name . 

# (2). NON-Nullable Column(NOT NULL) ==> These columns enforce the presence of a value . We specify that the column must always contain a valid state/value inserting or updating data . 
# Example ==> 
# A column like "email" in  a user table  could be defined as NOT NULL  because every user is expected to have an email address . 

# Implementation 
# create table Employees(
#     emp_id int ,
#     emp_name varchar(50),
#     email varchar(50) NULL
# );

# select * from Employees ; 

# insert into Employees
# VALUES
# (1 , "RAJ" , NULL);


# NOT NULL Implementation 
# create table orders(
#     emp_id int , 
#     emp_name varchar(50),
#     email varchar(60) NOT NULL);
    
# select  * from orders ; 

# insert into orders(emp_id , name)
# VALUES
# (2 , "kriti") ; 


# What does Default in MYSQL ? 
# In MYSQL , the 'Default' keyword is used to assign a default value to a column when 
#   no explicit value is specified during an INSERT statement . 
# When we define a column with a default value , it means that if no value is provided for that column 
#   while inserting a new row , the default value will be automatically used instead . This is useful when 
#   we want to ensure that a column always has a value , even if it is not explicity provided . 

# Implementation 
# create table Employees(
#     emp_id int , 
#     emp_name varchar(50),
#     emp_date DATE DEFAULT CURRENT_DATE() );
    
    
# select * from Employees ; 

# insert into employees
# (emp_id , emp_name)
# VALUES
# (1 , 'kriti');

# select * from employees ; 

# Example - 2 
# create table studata(
#     id int not null default 0 , 
#     name varchar(50) not null DEFAULT 'unnamed'
#     );
    
# select * from studata ; 

# insert into studata
# (id , name)
# VALUES
# (1 , "Sam");

# select * from studata ; 

# insert into studata () VALUES () ; 
# select * from studata ; 

# Alter ==> Alter is used to delete and create a new column  in table . 
# Implementation 
# alter table studata add column Grade varchar(20);
# alter table table_name add column column_name datatype;

# alter table studata drop column Grade;
# alter table table_name drop column column_name;

# Primary Key ==> The PRIMARY KEY  constraint uniquely identifies each record in a table .
#  Primary keys must contain unique values and cannot contain NULL values . 

# Implementation 
# create table emp_info(
#     emp_id int  NOT NULL  PRIMARY KEY , 
#     Name varchar(40),
#     Age INT , 
#     Department varchar(50)
# );

# select * from emp_info ; 

# insert into emp_info
# VALUES
# (1 , "Sam" , 34 , "Sales"),
# (2 , "Pooja" , 23 , "HR");

# select * from emp_info ; 
# insert into emp_info
# VALUES
# (1 , "kriti" , 36 , "HR");

# select * from emp_info ; 

# What does Auto_Increment in MYSQL ? 
# Auto Increment allows a unique number to be generated automatically when a new record is inserted into a table . 
# Implementation 
# create table emp_info(
#     emp_id int not null primary key AUTO_INCREMENT , 
#     Name varchar(40),
#     Department varchar(50),
#     Salary int 
# );
# select * from emp_info ; 

# insert into emp_info
# (Name , Department , Salary)
# VALUES
# ('Sam' , 'HR' , 30000),
# ('Pooja' , 'IT' , 45000);

# select * from emp_info ;

# CRUD Operation
# C ==> Create 
# R ==> Read 
# U ==> Update 
# D ==> Delete   

# (1). create 
# create table table_name (column1 datatype , column2 datatype .....)

# (2). Read 
# insert into table_name VALUES (column1_entry , column2_entry...)

# (3). update 
# Example 
# update emp_info set Name = "Rashmi" where emp_id = 2 ; 

# (4). Delete 
# Example 
# delete from emp_info  where Name = "Rashmi" ; 

# MYSQL ORDER BY KEYWORD ==> 
# The order by keyword is used to sort the result-set in ascending or descending order . 
# select Salary from emp_info order by Salary ; 
# select distinct Name from emp_info order by Name ; 
# select distinct Salary from emp_info order by Salary desc ; 


# Limit ==> it is used to specify the No.of records to Return.
# select Name from emp_info order by Name limit 2;

# MYSQL Aggregation Functions(AVG() , SUM() , MIN() , MAX() , COUNT())
# 1. Count() ==> The count() returns the number of rows that matches a specified criteria . 
# 2. AVG() ==> The avg() returns the average value of a numeric column . 
# 3. SUM() ==> The sum() returns the total sum of numeric column . 
# 4. MIN() ==> The min() returns the minimum value of a column . 
# 5. MAX() ==> The max() returns the maximum value of a column . 

# Implementation 
# select max(Salary) from emp_info ; 
# select min(Salary) from emp_info ; 
# select sum(Salary) from emp_info ; 
# select avg(Salary) from emp_info ; 
# select count(Salary) from emp_info ; 

# MYSQL LOGICAL OPERATIONS ==> The logical operators are those that are true or false . 
# They return a True or False values to combine one or more True or False values . 
# SELECT * FROM `emp_info` where salary = 40000 ; 
# SELECT * FROM `emp_info` where salary != 40000 ; 
# SELECT * FROM `emp_info` where salary <30000 OR salary >= 40000 ;
# SELECT * FROM `emp_info` where salary <30000 || salary >= 40000 ; 
# SELECT * FROM `emp_info` where salary <30000 OR salary >= 40000 ; 
# SELECT * FROM `emp_info` where salary <30000 && salary >= 40000 ; 
# SELECT * from emp_info where Department = "HR" or Department = "IT" ; 
# SELECT * from emp_info where Salary BETWEEN 20000 and 40000 ; 
# SELECT * from emp_info where Salary NOT BETWEEN 20000 and 40000 ; 
# SELECT * from emp_info where Name in ('Sam' , 'Gorav' , 'Mohit');

# MYSQL  STRING FUNCTIONS 
# (1). concat() ==> This function adds two or more expressions together . 
# select concat('Mohit' , ' ' , 'Sharma')as FullName ; 
# select concat(Name , " " , Department) from emp_info as FULLNAME ;

# (2). Reverse() ==> This function reverses a string and returns the result . 
# SELECT reverse(Name) from emp_info as ReverseName ; 

# (3). CHAR_LENGTH() ==>  This function returns the length of a string (in characters). 
# select char_length(Name) from emp_info ; 

# (4). LOWER() ==>  This function converts a string to a lower case . 
# select lower(Name) from emp_info ; 

# (5). UPPER() ==> This function converts a strng to upper-case . 
# select lower(Name) from emp_info ; 

# MYSQL DATETIME 
# (1). CURDATE() ==> curdate() returns the current date : 'yyyy-mm-dd'
# (2). NOW() ==> NOW()  returuns both  current date and time : 'yyyy-mm-dd hh:mm:ss'
# (3). CURTIME() ==> curtime() returns current time : 'hh:mm:ss' 

# create table dateemp(
#     Name varchar(50),
#     DOB Date , 
#     BirthTime DATETIME 
# );

# select * from dateemp ; 

# insert into dateemp
# VALUES
# ("Sam" , "1991-03-15" , "1991-03-15 05:17:21"),
# ("Ritik" , curdate() , now());

# select * from dateemp ; 


# Foreign key Constraint ==> 
# A foreign key is a key used to link two tables together .
# A foreign key is a field(or collection of fields) in one table that refers to the primary key in another table . 

# create table customers
# ( cid int not null AUTO_INCREMENT  PRIMARY KEY , 
#  cname varchar(40),
#  email varchar(100)
#  );
 
# select * from customers ; 

# create table orders (oid int not null AUTO_INCREMENT PRIMARY KEY , 
#                      orderdate date , 
#                      cid int , 
#                      foreign key(cid) REFERENCES customers(cid));
                     
# select * from orders ; 

# insert into customers (cname , email) VALUES 
# ("Sam" , "Sam@gmail.com"), 
# ("Garvit" , "Garvit@gmail.com"),
# ("Preeti" , "Preeti@gmail.com");

# insert into orders
# (orderdate , cid)
# VALUES
# ("2023-08-15" , 1),
# ("2023-09-19" , 2),
# ("2023-10-01" , 3);

# SELECT * FROM orders ; 



# MYSQL JOINS ==>
 
# A join is used to combine the rows from two or more tables based on a related column between them . 
# Types of joins ==> 
# (1). Inner join  ==> The INNER JOIN keyword selects the records that have matching values in both tables . 
# select * from customers , orders 
# where customers.cid = orders.cid ;

# (2). MYSQL LEFT(OUTER JOIN) ==> The left join returns all the records from the left table(table1) and 
# match records from the right table(table2) . The result is null for the right side ,if there is no match . 

# select cname , email from customers left join orders on customers.cid = orders.cid;
# select * from customers left join orders on customers.cid = orders.cid;

# (3). MYSQL RIGHT(OUTER) JOIN ==> The Right join returns all records from the right table (table2) and 
# the match records from the right table (table2) . The result is Null from the left side , if there is no match . 

# select * from customers right join orders on customers.cid = orders.cid;

# Windows Functions ==> 
# In Mysql , Windows functions are used to perform calculations across a set of tables rows related to the current row . These function can be very useful for tasks like ranking , and creating moving averages etc . 
# In MYSQL ,  windows functions are typically used in conjuction with the over() clause to define the window or partition over which the function shuld operate . 

# create table products (
#     ProductID int AUTO_INCREMENT PRIMARY KEY , 
#     ProductName varchar(255) not null , 
#     Price Decimal(10,2) not null , 
#     Category varchar(50) not null
# ); 

# select * from products ;


# insert into products
# (ProductName , Price , Category)
# VALUES
# ('Product A' , 25.99 , 'Electronics'),
# ('Product B' , 19.78 , 'Clothing'),
# ('Product C' , 10.56 , 'Home & Garden'),
# ('Product D' , 12.90 , 'Electronics'),
# ('Product E' , 13.65 , 'Clothing'),
# ('Product F' , 15.87 , 'Home & Garden'),
# ('Product G' , 76.45 , 'Electronics'),
# ('Product H' , 34.90 , 'Clothing');

# select * from products ; 

# (1). ROW_NUMBER() ==> It assigns a unique  number to each row within the result set . 
# select ProductName , Price  , ROW_NUMBER()  OVER (ORDER BY Price) AS  RowNum  from products ;  

# (2). NTILE(n) ==> This function divides the result set into 'n' roughly rqual parts and assign a group number to each row . 
# select ProductName , Price , NTILE(4)  over (ORDER BY Price) AS PriceQuartile ; 

# (3). LAG(column , offset) ==> This function retrieves the value of a specified column from the row that is "offset" rows before the current row . 
# select ProductName , Price , LAG(Price , 1) OVER (ORDER BY Price) AS PreviousPrice from products ; 

# (4). LEAD(Column , offset) ==> This function retrives the value of a specified column from the row that is "offset" rows after the current row . 
# select ProductName , Price , LEAD(Price , 1) OVER (Order by Price) AS NextPrice as products; 

# (5). SUM(column)OVER (Partition  by ... order by ..) ==> Calculate the running total of a column within a specified window . 
# select ProductName , Price , SUM(Price) OVER(PARTITION BY Category order by  Price) AS CategoryTotal from products; 

# (6). AVG(Column) OVER (Partition by ... order by ...) ==> Calculate the moving average of a column within a specified window . 

# (7). Ranking Function ==> 
# The ranking function  in mysql are used to rank each row of a partition . 
# These function are always used with over() clause . 
# The ranking function always assign rank on basis of order by clause . 
# The rank is assigned to rows in a sequential manner . 
# The assignment of rank to rows always start with 1 for every new partition . 

# Types of Ranking Function ==>
# (a). dense_rank() ==> This function will assign rank to each row within a partition without gaps . Basically , the ranks are assigned in a consecutive manner . and if there is a tie between values then they will be assigned the same rank , and next rank value will be one greter than the previous rank assigned . 

# (b). rank() ==> This function will assign rank to each row within a partition with gaps and here ranks are assigned in non-consicutive number and if there is a tie between values they will be assigned  same rank  and next rank value will be (previous rank � number of duplicates).

# (c). Percent_rank() ==> It returns the percentile rank of a row within a partition that ranges from 0 to 1 . It tells the percentage of partition values less than the value in the current row , excluding the highest value .


# Q.1 Write a query to retrieve products with ranking by price within each category ? 
# select ProductID , ProductName , Price , Category , DENSE_RANK() OVER (PARTITION BY Category ORDER BY Price) AS 
# PriceRank  from products  order by Category , PriceRank ; 

# select ProductID , ProductName , Price , Category , 
# Rank() OVER (PARTITION BY Category order by Price ) AS PriceRank ,
# PERCENT_RANK() OVER (PARTITION BY Category ORDER BY Price) AS PercentPriceRank 
# from products 
# order by Category , PriceRank ; 


# Q.2  What is user privilieges and permissions ?
# User privileges and  permissions refer to the level of access that user has to mysql database or its objects , such as tables , views , procedures and functions . 
# In other words , user privilieges determines that what a user can and cannot do within a MYSQL Database . 
# MYSQL provides a variety of privileges and permissions that can be assigned to users . Some of the common privileges include :
# (1). select ==> it is used to view data in a table or view / it is used to select data from database. 
# (2). Insert ==> it is used to add new data to a table / it is used to insert new record in a table.
# (3). DELETE ==> it is used to delete the data from a table / it is used to delete existing records in a table.
# (4). UPDATE ==> it is used to modify existing data in a table . 
# (5). DROP   ==> it is used remove databases or tables .
# (6). CREATE ==> it is used to create new databases or tables . 
# (7). Grant and revoke ==> it is used to grant  or revoke privileges from the other users . 
# (8). Index  ==> it is used to create or drop the indexes. 

# Q.3  What does Grant , Revoke and Transaction in MYSQL ? 
# In mysql , grant and revoke are used to manage user privileges and permissions while Transactions are used to ensure the integrity of data when making multiple changes to a database . 

# (1). Grant : Grant is used to give a user or multiple users certain privileges , such as the ability to create or delete tables, insert data or executes certain commands . The "grant" command can be used to specify the level of access the user has to specific databases , tables or columns . 
# SYNTAX :  GRANT SELECT ON DataBaseName.tablename TO 'user'@'portnumber' ; 
# Example : GRANT SELECT ON AmitData.products TO 'testuser'@'localhost' ; 


# (2). Revoke : Revoke is used to remove the privileges that were priviously granted to a user. This command can be used to revoke a specific privileges or all privileges . 
# SYNTAX :  REVOKE SELECT ON DataBaseName.tableName FROM 'user'@'portnumber' ;
# EXAMPLE : REVOKE SELECT ON AmitData.products FROM 'testuser'@'localhost' ; 

# (3). Transaction : Transactions are used to ensure the integrity of data when making multiple changes to a database . Transactions allow a group of SQL statements to be executed as a single unit of work , ensuring that either all of the changes are made or none of then are . This help to prevent data inconsistencies that could occur if only some of the changes were made . Transactions are started using the 'BEGIN' command and can be either commited or rolled back using the COMMIT or ROLLBACK commands respectively . 

# If any operation within a transaction fails , the entire transaction is rolled back , meaning that all the changes made by the operations in the transactions are undone . 

# Transactions  can be useful in a variety of scenarious such as transferring funds between bank accounts , updating inventory levels in e-commerce system , or making changes to a customer's order. 

# table -1 
# create table accounts (
#     id int primary key , 
#     Name varchar(50),
#     Balance decimal(10,2)
# )

# table -2 
# create table transactions(
#     id int primary key AUTO_INCREMENT , 
#     account_id int , 
#     account Decimal(10,2),
#     type ENUM('Credit' , 'Debit'),
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
#     FOREIGN KEY(id) REFERENCES accounts(id)) ; 



# insert into accounts
# VALUES
# (1 , "Sam" , 5000),
# (2 , "Rahul" , 6000),
# (3 , "Manish" , 7000),
# (4 , "Ayush" , 8000);


# insert into transactions (id , account_id , account , type) 
# VALUES 
# (1 , 2 , 10000 , "Credit"), 
# (2 , 3 , 15000 , "Debit"), 
# (3 , 4 , 5000 , "Debit"), 
# (4 , 5 , 20000 , "Credit");

# select * from transactions 


# #Begin Transaction 
# START TRANSACTION ; 

# #step-1 : update balance of accounts with id=1 
# update accounts SET balance = balance - 2000 where id = 1 ; 

# #step-2 : Insert into record of debit transactions for account with id = 2 
# INSERT INTO transactions(id,account_id , account , type) VALUES (5,101 ,78000 , 'Debit');

# #step-3 : Update balance of account with id = 2 
# update accounts SET  balance = balance � 1000 WHERE id = 2 ; 

# #Commit transaction if all steps completed successfully ...
# COMMIT ; 

# Q.3  What is ACID  properties in MYSQL ? 
# ACID  is an acrnoym for Atomicity , Consistency , Isoloation and Durability . 
# These are 4 properties that ensure reliability and consistency of database transactions . 
# 1. Atomicity ==> 
# Atomicity refers to all-or-nothing property of a transaction . A transaction is atomic if it is executed as a single , indivisible unit of work , which means that either all of the database operation in the transaction are completed successfully or none of them are . If any operation with in  a transaction fails , the entire transaction is rolled back . meaning that all the changes made by the operations in the transaction are undone . 

# Implementation 
# create table bank_accounts(
#     id int primary key AUTO_INCREMENT , 
#     account_number varchar(20) not null ,
#     balance decimal (10,2) not null
#     );
    
#  select * from bank_accounts ; 

# table-2 
# create table transactions(
#     id int primary key AUTO_INCREMENT , 
#     account_id int not null ,
#     amount decimal (10,2) not null ,
#     transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
#     FOREIGN KEY(account_id) REFERENCES bank_accounts(id)
#     );
# select * from transactions; 


# START TRANSACTION ; 

# update bank_accounts 
# SET balance = balance - 100.00 
# WHERE id = 1 ; 

# update bank_accounts 
# SET balance = balance + 100.00 
# WHERE id = 2 ; 



# COMMIT ; 


# (2). Consistency ==> 
# In MYSQL , ensuring consistencey involves maintaining the integerity and validity of data with in database .
# This includes enforcing data constraints , such as primary keys , unique constraints and check constraints . 
# Additionally , consistencey can be achieved through the use of transactions to group related operations and maintain data integrity . 

# table-1 
# create table users(
#     id int primary key auto_increment , 
#     name varchar(40) not null , 
#     gmail varchar(40)
# );

# table - 2 
# create table orders(
#     id int primary key auto_increment , 
#     user_id int not null , 
#     amount decimal(10,2) not null , 
#     order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
#     FOREIGN KEY (user_id) REFERENCES users(id) 
# );


# START TRANSACTION ; 

# insert into users(name , gmail)
# VALUES
# ('Kriti' , 'kriti@gmail.com');

# #Retrieve the ID  of the newly inserted user 
# SET @user_id := LAST_INSERT_ID() ;

# #INSERT AN ORDER FOR THE USER 
# Insert into orders(user_id , amount , order_date)
# VALUES
# (@user_id , 100.00 , CURDATE());

# COMMIT ; 


# Note ==> 
# SET @user_id := LAST_INSERT_ID() ; ==> "Take the most recent auto-incremented ID  that was generated in a table and store it in the @user_id variable . "


# (3). Isolation ==> Isolation refers to the ability of a transaction to operate independently of other transactions that may be executing concurrently . Each transaction must be executed in isloation , meaning that the changes made by one transaction must be invisible to other transaction untill the transaction is completed . 

# Implementation 
# create table bank_accounts(
#     id int primary key AUTO_INCREMENT , 
#     account_number varchar(20) not null ,
#     balance decimal (10,2) not null
#     );
    
#  select * from bank_accounts ; 

# table-2 
# create table transactions(
#     id int primary key AUTO_INCREMENT , 
#     account_id int not null ,
#     amount decimal (10,2) not null ,
#     transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
#     FOREIGN KEY(account_id) REFERENCES bank_accounts(id)
#     );
# select * from transactions; 


# #START THE TRANSACTION 
# START TRANSACTION ; 
# #UPDATE THE BALANCE OF THE ACCOUNT WITH ID = 1 BY 200 
# update bank_accounts SET  balance = balance - 200 WHERE id = 1 ; 
# #Wait for a few seconds 
# select SLEEP(4) ; 
# #Commit the transaction 
# COMMIT ; 
# #START A SECOND TRANSACTION 
# START TRANSACTION ; 
# #UPDATE THE BALANCE OF ACCOUNT WITH ID = 1 BY 100
# update bank_accounts SET balance = balance - 100 WHERE id = 1 ; 
# #Commit the transaction 
# COMMIT ; 


# (4). Durability ==> The durability property of acid requires that once a transaction is commited , its changes should be persist even in the face of a system failure , such as power outage  , hardware failure or software crash . 
# In MYSQL ,  the durability property is ensured by writing changes to disk before considering then commited .This means that even of the server crashes or losses power , the changes will be available when the server restarts . 

# table-1 
# create table users(
#     id int primary key auto_increment , 
#     name varchar(40) not null , 
#     gmail varchar(40)
# );

# table - 2 
# create table orders(
#     id int primary key auto_increment , 
#     user_id int not null , 
#     amount decimal(10,2) not null , 
#     order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
#     FOREIGN KEY (user_id) REFERENCES users(id) 
# );

# START TRANSACTION ;
# INSERT INTO orders(user_id , amount)VALUES(1 , 450);
# COMMIT ; 
# SELECT * FROM ORDERS ; 







# Q.1 What is indexes in MYSQL ? 
# In MYSQL , .an index is a data structure that provides efficient and fast access to data in a table based on the values of one or more columns . An index is essentially a pointer to a specific row or a set of rows in a table , and it helps to speed up data retrieval  by allowing the database engine to quickly find the relevent rows without having scan the entire table . 
# When  we create an index in MYSQL , the database engine creates a separate structure that store the index data , which is optimized for fast lookups . When we executes a query that includes a WHERE  clause or a join statement , the database engine can use the index to quickly locate the relevent rows in the table and return the results . 


# Indexes are perticularly useful in large tables where quaries can be slow and time-consuming without them . However , creating too many indexes can also slow down database performance , as the engine has to maintain the indexes as data is inserted , updated  or deleted from the table . 

# The most  commonly used types in MYSQL are : 
# (1). B-tree index ==> The B-tree (balance tree) index is most common  type of index in MYSQL . It stores index values in a tree-like structure  , allowing for fast retrieval of data based on the values of one or more columns . 

# (2). Hash index ==> The hash index is a type of index that stores index values as hashes whichi are generated using am algorithm . Hash indexes are perticularly useful for equality searches(example - searching for exact matches) , but they are less effective for range searches (example - searching for values within a range).

# (3). Full-text index ==> The full-text index is a type of index that is designed for text-based searches . It allows us to search for words or phrases with in a large block of text and it can be particularly useful for applications that involves search functionality . 

# (4). Spatial Index ==> The Spatial index is a type of index that is designed for spatial data such as geographical coordinates . It allows for fast retrieval of data based on the spatial relationship between objects . 

# (5). R-tree index ==> The R-tree index is a type of index that is similar to the spatial index , but it is optimized for storing and searching for data in two or three dimensions . 


# Triggers ==> 
# In MYSQL , a trigger is a database object that defines  a set of actions that are automatically executed , when a specific event occurs in the database . These events can include insert , update , delete and other data manipulation operations on a table . Triggers are used to enforce data integrity , audit changes and automate complex business logic within the database . 

# Trigger Structure ==> 
# A trigger can consist of 3 main parts : 
# (1). Event : This defines when the trigger should activate , such as BEFORE INSERT , AFTER UPDATE etc . 

# (2). Table : The table to which the trigger is associated . 

# (3). Action : The set of SQL  statements that should be executed when the trigger is activated . 


# Types of Triggers ==> 
# (1). BEFORE Triggers ==> 

# These  triggers fire before the triggering event(Ex. Before Insert). They can be used to modify data before it is inserted , updated or deleted . 

# (2). AFTER Triggers ==> 

# These  triggers fire after the triggering event(Ex. After DELETE). They can be used to log changes , send notifications or perform other actions after the data has been modified . 

# Example ==> 
# Let's consider that we have a database for an online bookstore . We want to enforce a rule that prevents the insertion of book records with a price lower than $5. 

# solution ==> 
# step-1(Create a table) ==> 
# create table books(
#     book_id int AUTO_INCREMENT PRIMARY KEY , 
#     title varchar(255),
#     author varchar(255),
#     price DECIMAL(8,2)
#     );
 
# select * from books ; 

# step-2 (Create the trigger)
# DELIMITER // 
# CREATE TRIGGER before_book_insert
# BEFORE INSERT  ON books
# FOR EACH ROW 
# BEGIN 
#    IF NEW.price < 5.00 THEN
#       SIGNAL SQLSTATE '45000' 
#       SET MESSAGE_TEXT = 'Price must be at least $5';
#    END IF;
# END;
# //
# DELIMITER ;


# step-3 (Inserting Records) ==> 
# insert into books
# (title , author , price)
# VALUES
# ('Physics' , 'Author1' , 4.53),     # shows error 
# ('Maths' , 'Author2' , 9.98) ;     # Execute code 


# Q.2 How to create and schdule job in MYSQL ? 
# In mysql , we can create and schdule jobs using the MYSQL Event Schedular . The Event Schedular allows us to automate tasks , such as running SQL statements or stored procedure at specific times or intervals . 

# (1). ENABLE THE EVENT SCHDULAR ==> 
# Before  we can create and schdule jobs , ensure that the MYSQL , Event Schdular is enabled . We can enable it by running the command : 

# SET GLOBAL event_scheduler = ON ;

# If we want to make this setting permanant , we can add this line : 

# event_schedular = ON  


# (2). Create an Event ==> 

# To create an event , we wil use the CREATE EVENT STATEMENT . 

# DELIMITER // 
# CREATE EVENT my_event 
# ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR 
# DO 
# BEGIN 
#      UPDATE my_table SET some_column  = some_column + 1  ; 
# END ; 
# //
# DELIMITER ; 

# ALTER EVENT my_event ENABLE ; 

# SHOW EVENTS ; 




# Q.1 Write a SQL query to retrieve the second highest salary from Employee Table ?
# select max(salary) from emp_info where Salary < (select max(salary) from emp_info) ; 

# Q.2 Write a SQL  query to count the number of the employees in each department ?
# select Department , COUNT(*) as employeecount from emp_info group by Department ; 

# Q.3 Write a SQL  query to find the employees who have the same salary ?
# select Salary , count(*) as employeecount from emp_info group by Salary HAVING count(*)>1 ; 

# Q.4. Write a SQL  query to calculate the average salary of employee in each department ?
# select Department , AVG(Salary) as AverageSalary from emp_info GROUP BY Department ; 


# Q.5  Write a SQL  query to find duplicates row in a table ?
# select * from emp_info group by emp_name , Department , Salary HAVING COUNT(*) > 1 ; 

# Q.6 Write a SQL  query to find the employees whose name start with 'N' and end with 'i' ?
# select emp_name from emp_info where emp_name LIKE 'N%i' ; 


# Q.7 Write a SQL  query to calculate the total salary of all employees ?
# select sum(Salary) as TotalSalary from emp_info ; 

# Q.8 Write a SQL query to find top 3 highest-paid employees ?
# select * from emp_info ORDER BY Salary DESC LIMIT 3 ;   


# Table(emp_info) ==> emp_id , emp_name , Department , Salary 


# Stored Procedure ==> 
# (1). A stored Procedure is a database object . 
# (2). A store Procedure is a series of declarative SQL statements . 
# (3). A store procedure can be stored in a database and can be reused over and over again . 
# (4). Parameters can be passed to a store procedure , so that the store procedure can act based on the parameter value . 
# (5). SQL Server creates an execution plan and stores it in the cache . 

# Example ==> 
# create table employees(
#     employee_id int PRIMARY KEY , 
#     employee_name varchar(255),
#     department_id int , 
#     salary decimal(10,2)
#     );
    
# insert into employees
# VALUES
# (1 , "Mohit" , 1 , 60000.00),
# (2 , "Kriti" , 2 , 55000.00),
# (3 , "Pooja" , 1 , 62000.00),
# (4 , "Raj" , 2 , 58000.00),
# (5 , "Alisha" , 1 , 63000.00);

# select * from employees ; 


# step-2  (create a store procedure to calculate the average salary for a given department)
# DELIMITER // 

# CREATE PROCEDURE CalculateAverageSalary(IN departmentId int , OUT avgSalary DECIMAL (10,2))
# BEGIN 
#    SELECT AVG(SALARY) INTO avgSalary 
#    FROM employees 
#    WHERE department_id = departmentId ; 
# END ; 
# //

# DELIMITER ; 


# step-3 (call the store procedure) 

# CALL CalculateAverageSalary(1 , @departmentAvgSalary);

# SELECT @departmentAvgSalary ; 


# Sub-Queries ==> Sub-Query is a sub-select or inner query , is a  SQL  query nested within another SQL query .
#  It is a way to retrieve data from one or more tables based on the result of another query .
#  Subqueries can be used in various parts of SQL  statements , such as SELECT , FROM  , WHERE etc . 

# Example ==> 
# step-1 
# create table customers(
#     customer_id int primary key , 
#     customer_name varchar(255),
#     city varchar(255)
#     );
    
    
# insert into customers
# VALUES
# (1 , "Mohit" , "Delhi"),
# (2 , "Preeti" , "Jaipur"),
# (3 , "Sam" , "Delhi"),
# (4 , "Raj" , "Gurgaon");

# select * from customers ; 

# create table orders(
#     order_id int primary key , 
#     order_date DATE ,
#     customer_id INT 
#     );
    
# insert into orders
# VALUES
# (101 , "2023-10-01" , 1),
# (102 , "2023-10-02" , 2),
# (103 , "2023-10-03" , 1),
# (104 , "2023-10-04" , 3),
# (105 , "2023-10-05" , 4);

# select * from orders ; 

# Task-1 Find the orders placed by customers from Delhi ? 
# select order_id , order_date from orders 
# where customer_id in (SELECT customer_id FROM customers WHERE city = "Delhi");

# Task-2 Retrieve a list of customers along with the total number of orders they have placed ? 
# select customer_id , customer_name , 
#     (select count(*) from orders where orders.customer_id = customers.customer_id) AS total_orders from customers ; 

# Example - 2 (Employee Average Salary Calculation) 
# step-1 
# create table salaries(
#     department_id int , 
#     average_salary DECIMAL(10,2)
#     );
    
# insert into salaries
# VALUES
# (1 , 61500.00),
# (2 , 56000.00);

# create table employees(
#     employee_id int PRIMARY KEY , 
#     employee_name varchar(255),
#     department_id int , 
#     salary decimal(10,2)
#     );
    
# insert into employees
# VALUES
# (1 , "Mohit" , 1 , 60000.00),
# (2 , "Kriti" , 2 , 55000.00),
# (3 , "Pooja" , 1 , 62000.00),
# (4 , "Raj" , 2 , 58000.00),
# (5 , "Alisha" , 1 , 63000.00);

# select * from employees ; 

# select employee_id , employee_name , department_id , salary 
# from employees 
# where salary > (SELECT average_salary from salaries where salaries.department_id = employees.department_id);

# Interview Questions ==> 

# create table Orders(
#     OrderID INT , 
#     CustomerID INT ,
#     Date DATE , 
#     Amount DECIMAL(10,2),
#     Category VARCHAR(50),
#     Product VARCHAR(50)
#     );
    
# select * from Orders ; 

# insert into Orders
# VALUES
# (1 , 1 , "20203-01-01" , 100.50 , 'Electronics' , 'TV'),
# (2 , 2 , "2023-02-15" , 75.20 , 'Clothing' , 'Shirt'),
# (3 , 3 , "2023-03-20" , 50.00 , 'Electronics' , 'Headphones'),
# (4, 1 , "2023-04-05" , 120.80 , 'Clothing' , 'Pants'),
# (5, 2,  "2023-05-14" , 200.00 , 'Electronics' , 'Phone'),
# (6, 3, "2023-06-17" , 90.60 , 'Clothing' , 'Dress'),
# (7,1 , "2023-07-13" , 150.30 , 'Electronics' , 'Laptop'),
# (8,2 , "2023-08-18" , 80.00 , 'Clothing' , 'Shoes'),
# (9,3,  "2023-09-03" , 70.40 , 'Electronics' , 'Camera'),
# (10,1 , '2023-10-19' , 180.90 , 'Clothing' , 'Jacket');

# select * from Orders ; 

# Q.1 Write a query to calculate the total revenue generated by each customer from the "Orders" table and display the results in descending order ? 

# SELECT CustomerID , SUM(Amount) AS TotalRevenue FROM orders GROUP BY CustomerID ORDER BY TotalRevenue DESC ; 

# Q.2  How can you find the top 3 customers with the highest total revenue from the 'Orders' table ? 
# SELECT CustomerID , SUM(Amount) AS TotalRevenue FROM orders GROUP BY CustomerID ORDER BY TotalRevenue DESC LIMIT 3 ; 


# Q.3 Write a query to calculate the average revenue per order for each month from the "Orders" table ? 
# SELECT MONTH(Date) AS MONTH , AVG(Amount) AS AverageRevenue FROM Orders GROUP BY MONTH ; 

# Q.4 How can you find the customers who have made orders in all months  of a given year ? 
# SELECT CustomerID from orders 
# WHERE YEAR(Date) = 2023 

# GROUP BY CustomerID 
# HAVING COUNT(DISTINCT MONTH(Date)) = 12 ; 


# Q.5 Write a query to calculate the cumulative revenue for each customer over time from the "Orders" table ? 
# SELECT CustomerID , Date , SUM(Amount) OVER (PARTITION BY CustomerID ORDER BY DATE) AS CumulativeRevenue  FROM Orders ;

# Q.6 How can you calculate the percentage contribution of each product category to the total revenue from the "Orders" table ? 
# SELECT Category , SUM(Amount) / (SELECT SUM(Amount) FROM orders) * 100 AS PercentageContribution FROM Orders GROUP BY Category ; 


# Q.7 Write a query to identify thr customers who have made the highest number of repeat orders from the "Orders" table ? 
# SELECT CustomerID , COUNT(OrderID) AS RepeatOrders
# FROM Orders 
# GROUP BY CustomerID
# HAVING COUNT(OrderID) >1 
# ORDER BY RepeatOrders DESC ; 


# Q.8 How can you find the dates with the highest total revenue from the "Orders" table? 
# SELECT Date , SUM(Amount) AS TotalRevenue  FROM  orders GROUP BY Date ORDER BY TotalRevenue DESC LIMIT 1 ; 

# Q.9 How can you find the customers who have not placed any orders in the past three months from the "Orders" table ? 
# SELECT DISTINCT CustomerID  FROM orders WHERE CustomerID NOT IN (SELECT DISTINCT CustomerID FROM orders WHERE DATE >- DATE_SUB(CURDATE() , INTERVAL 3 MONTH ));
