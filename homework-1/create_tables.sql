-- SQL-команды для создания таблиц
create table customers
(
	customer_id varchar(100) primary key,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);

create table employees
(
	employee_id int primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title varchar(100) not null,
	birth_date varchar(100) not null,
	notes text
);

create table orders
(
	order_id int primary key,
	customer_id varchar(100) references customers(customer_id) not null,
	employee_id int references employees(employee_id) not null,
	order_date varchar(100) not null,
	ship_city varchar(100) not null
);

