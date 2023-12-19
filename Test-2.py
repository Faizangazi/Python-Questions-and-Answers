#  Q.1 Difference between Numpy and pandas ?
# Q.2.Difference between pivot and pivot table ?
# Q.3 Difference between Descrete data vs continuous data ?
# Q.4 what is DBMS ? How RDBMS  is different from traditional approaches ?
# Q.5 Provide name of data types that are use in mysql ?
# Q.6 how  can we create or delete a table ? 
# Q.7 how can we add or delete a column name in mysql ?
# Q.8 what is primary key and auto_incremet  constraint?


#  Q.1 Difference between Numpy and pandas ?
# Ans ==> 
#  1. Numpy module works with numerical data and Pandas module works with the tabular data.
#  2. Numpy has a better performance for 50K rows or less and Pandas has a better performance for 500K 
#     rows or more.
#  3. Numpy consumes less memory as compared to Pandas and Pandas consume large memory as compared to Numpy.
#  4. Numpy provides a multi-dimensional array and Pandas provides 2d table object called DataFrame.


# Q.2.Difference between pivot and pivot table ?
#  Ans ==> 
#  1. One major difference between the pivot and pivot_table methods is that pivot_table allows for 
#     aggregation of the data, whereas pivot does not.
#  2. pivot_table can be used to calculate statistics such as sum, mean, or count, while 
#     pivot can only reshape the data without performing any calculations.
#  3. pivot_table can handle duplicate values in the index and columns arguments, while pivot cannot.
#  4. pivot_table accepts a multi-level index and columns, while pivot only accepts single-level index 
#     and columns.

# Q.3 Difference between Descrete data vs continuous data ?
# Ans ==>
# 1. Values are Countable and finite in descrete data and in continuous data Any measured value 
#    within a specific range
# 2. Descrete data is Nondivisible whereas continuous data is Subdivisible
# 3. Nature remains constant over a specific time interval in descrete data whereas in continuous data
#    Nature varies over time and can have separate values ​​at any given point



# Q.4 what is DBMS ? How RDBMS  is different from traditional approaches ?
# Ans ==>
#  Database Management Systems (DBMS) are software systems used to store, retrieve, and run queries on data.
#  DBMS  is a software which is used to manage the database . 
#  Example => MySQL , Oracle . 

#  An RDBMS includes functions that maintain the security, accuracy, integrity and consistency of the data. 
#  This is different than the file storage used in a DBMS.
#  Advantages of the RDBMS include==>
#  1. Flexibility -- updating data is more efficient since the changes only need to be made in one place.
#  2. Maintenance -- database administrators can easily maintain, control and update data in the database.
#     Backups also become easier since automation tools included in the RDBMS automate these tasks.
#  3. Data structure -- the table format used in RDBMSes is easy to understand and provides an organized and
#     structural manner through which entries are matched by firing queries.



# Q.5 Provide name of data types that are use in mysql ?
# Ans ==>
#  Following are MySQL Data Types 
# 1. Numeric DataTypes ==>
# (a). TinyInt ==> We use tinyint for small integer values (-128 to 127) and boolean flags (0 or 1). 
# (b). Smallint ==> We use smallint for large integer values (-32 ,768 to 32 ,767).
# (c). INT ==>  we use in for even large integer values (-2 , 147 , 483 , 648 to 2,147,483,647).
# (d). BIGINT ==> we use bigint for large integer values (-9,223,372,,036,854,775,808 to 9,223,372,,036,854,775,807).
# (e). Float ==> we use FLOAT  or Double for floating point numbers . 
# (f). Decimal ==> We use Decimal for extract decimal values that requires precision , such as financial data .

# 2. Date and Time Datatypes ==>
# a. DATE ==> We use data for storing dates in the format YYYY-MM-DD . 
# b. TIME ==> We use time for storing tiems in the format HH:MM:SS . 
# c. DATETIME ==> We use DATETIME  for storing dates and times in the format YYYY-MM-DD HH-MM-SS.
# d. TIMESTAMP ==> We use timestamp for storing dates and time in a more compact format (YYYYMMDDHHMMSS).
# e. YEAR  ==> We use YEAR  for storing years in a 2-digit(70-80) or 4-digit(2021-2024). 

# 3. String Datatypes ==>
# (a).  CHAR ==>  we use CHAR  for fixed length-strings , such as postal codes or product codes . 
# (b). VARCHAR ==> we use VARCHAR for variable-length-strings , such as names or address . 
# (c). TEXT ==> we use TEXT for large blocks of text , such as product descriptions or blog post . 
# (d). ENUM ==> we use ENUM or SET  for storing a predefined list of options or categories . 

# 4. Binary DataTypes ==>  
# Binary, Varbinary, Tinyblob, Mediumblob, Longblob, Blob are the Binary datatypes.

# 5. Spatial DataTypes ==> 
# Geometry, Point, Linestring, Polygon, Multipoint, MultilineString, Multipolygon, Geometrycollection 



# Q.6 How can we create or delete a table ? 
# Ans ==>
# CREATE TABLE ==>
# create table Employees(
#     emp_id int , 
#     emp_name varchar(50),
#     emp_state varchar(50) );

# DELETE TABLE ==>
#  Drop table Employees ;



# Q.7 How can we add or delete a column name in mysql ?
# Ans ==>
# Alter is used to delete and create a new column in table . 
# Add column name  ==> alter table studata add column Grade varchar(20);
# delete column name ==> alter table studata drop column Grade;


# Q.8 what is primary key and auto_incremet constraint ?
#  Ans ==>
#  Primary Key  ==>  The PRIMARY KEY  constraint uniquely identifies each record in a table . 
#                    Primary keys must contain unique values and cannot contain NULL values . 
#  Auto Increment ==> it allows a unique number to be generated automatically when a new record is inserted
#                    into a table . 
