# Bash Restaurant Milestone 6 

# Management Systems

## EmployeeManagemenetSystem
- Holds a record database on employees
- is able to add and remove users 
- 

## MenuManagement
- Holds the price avaiable of menu items

## OrderManagement
- Assigning order number to a certain table
- Holds the status of each order
- 

## restrauntManagement
- Holds the status of tables
- allows for adding, releasing, and reserving tables

## roleManagement 
- Holds the roles for every type of role 
- Also assigns roles to different users 

## tableManagement
- Holds table infomation
- Allows table status to be changed
- Allows for number of people on table to be assigned
- assigns staff member to table

# Role System
## basicClass
- Basic outline for all the different roles
- Other roles will be inheriated from this class

## busBuy
- Has specical access to table status

## chefClass
- has special access to order management and menu managment 
- can change the status order and menu items

## hostClass
- has special access to table status
- can change/ assign party size to a table

## ManagerClass
- Has special access to database and employee infomation 
- Can view data
- Can change employee roles
- Can add or remove users 

## waiterClass
- Special access to payment
- special acess to table management
- Can modify table status