show databases;
create database db1;
use db1;
create table emp(Emp_No int,Emp_Name varchar(10),Salary int,Place varchar(20));
insert into emp values(1,"Kaviya",50000,"Thirukkadaiyur");
insert into emp values(2,"Abi",50000,"Akkur");
insert into emp values(3,"Devika",50000,"Mayiladuthurai");
insert into emp values(4,"Swetha",50000,"Poraiyar");
select * from emp;
insert into emp(Emp_No,Emp_Name,Salary,place) values(5,"swa",60000,"KCY");
