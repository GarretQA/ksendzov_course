-- Создать таблицу employees
-- - id. serial,  primary key,
-- - employee_name. Varchar(50), not null
create table employees (
	id serial primary key,
	employee_name varchar(50) not null
);


-- Наполнить таблицу employee 70 строками.
insert into employees (employee_name)
values  ('Arthur Sabin'), ('Marilou Sims'), ('Steven Pauley'), ('Nicholas Rollman'), ('Lamont Finley'),
	    ('Miranda Rusert'), ('Katrina Richardson'), ('Elwood Adams'), ('Orville Weaver'), ('James Otero'),
	    ('Keith Miner'), ('Valerie Peterson'), ('Jim Moore'), ('Josephine Schilling'), ('Benjamin Baskin'),
	    ('Anna Bernard'), ('Michael Holden'), ('Esther Wyse'), ('Martha Brown'), ('Lowell Alvey'),
	    ('Kira Thomas'), ('Miranda Casper'), ('Freeman Ryan'), ('Stacy Colon'), ('Frances Hansen'),
	    ('Thomas Voller'), ('Betty Simmons'), ('Robert Monson'), ('Tonya Vinson'), ('Mary Morales'),
	    ('Rodney Kelter'), ('Patricia Duncan'), ('Ruth Hunnell'), ('Richard Triana'), ('Olga Brown'),
	    ('Louise Smith'), ('Devin Bridges'), ('Albert Fantasia'), ('Crystal Morales'), ('Louis Klein'),
	    ('Joshua Owen'), ('Jennie Roane'), ('Benjamin Nishitani'), ('Melisa Biggs'), ('Elena Sager'),
	    ('Harriett Thomas'), ('John Ellington'), ('Tom Clark'), ('Mary Booth'), ('Kaitlin Kennedy'),
	    ('Sebastian Drake'), ('Teresa Surface'), ('Randall Rivera'), ('Kelly Sawer'), ('Adrian Johnson'),
	    ('Dominique Valdivia'), ('Eileen Darrigo'), ('Russell Pratt'), ('Christopher Turner'), ('Ellen Gonzales'),
	    ('Doris Pea'), ('Sally Whitely'), ('Hassan Shafer'), ('Tamela Hamilton'), ('Terry Simons'), ('Esteban Towns'),
	    ('John Silva'), ('Sarah Craig'), ('Matthew Larrieu'), ('Jennifer Walker');
	   
-- Создать таблицу salary
--   - id. Serial  primary key,
--   - monthly_salary. Int, not null
create	table salary (
	id serial primary key,
	monthly_salary int not null 
);


-- Наполнить таблицу salary 15 строками
insert into salary (monthly_salary)
values (1000), (1100), (1200), (1300), (1400), (1500), (1600), (1700),
	   (1800), (1900), (2000), (2100), (2200), (2300), (2400), (2500);

	  
-- Создать таблицу employee_salary
--  - id. Serial  primary key,
--  - employee_id. Int, not null, unique
--  - salary_id. Int, not null
create	table employee_salary (
	id serial primary key ,
	employee_id int not null unique ,
	salary_id int not null 
);


-- Наполнить таблицу employee_salary 40 строками:
-- - в 10 строк из 40 вставить несуществующие employee_id
insert into employee_salary (employee_id, salary_id)
values  (1, 1), (9, 9), (16, 14), (99, 11), (89, 3),
		(2, 2), (10, 10), (127, 13), (65, 2), (100, 4),
		(3, 3), (11, 11), (17, 12), (33, 1), (94, 5),
		(4, 4), (12, 12), (18, 11), (44, 2), (93, 6),
		(5, 5), (113, 13), (219, 10), (55, 3), (47, 7),
		(6, 6), (13, 14), (34, 9), (66, 4), (59, 8),
		(7, 7), (14, 15), (22, 8), (88, 5), (29, 9),
		(8, 8), (15, 15), (25, 7), (77, 6), (39, 10);

	
-- Создать таблицу roles
-- - id. Serial  primary key,
-- - role_name. int, not null, unique	
create table roles (
	id serial primary key ,
	role_name int not null unique 
);

-- Поменять тип столба role_name с int на varchar(3
alter table roles 
alter column role_name type varchar(30) using role_name::varchar(30);

-- Наполнить таблицу roles 20 строками:
insert into roles (role_name)
values ('Junior Python developer'), ('Middle Python developer'), ('Senior Python developer'), 
		('Junior Java developer'), ('Middle Java developer'), ('Senior Java developer'),
		('Junior JavaScript developer'), ('Middle JavaScript developer'), ('Senior JavaScript developer'),
		('Junior Manual QA engineer'), ('Middle Manual QA engineer'), ('Senior Manual QA engineer'),
		('Project Manager'), ('Designer'), ('HR'), ('CEO'), ('Sales manager'), ('Junior Automation QA engineer'),
		('Middle Automation QA engineer'), ('Senior Automation QA engineer');


-- Создать таблицу roles_employee
-- - id. Serial  primary key,
-- - employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
-- - role_id. Int, not null (внешний ключ для таблицы roles, поле id)
create table roles_employee (
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key (employee_id)
		references employees (id),
	foreign key (role_id)
		references roles (id)
);


-- Наполнить таблицу roles_employee 40 строками:
insert into roles_employee (employee_id, role_id)
values (5, 20), (63, 11), (68, 20), (23, 15), (17, 3), (34, 13), (60, 13), (31, 17), (22, 3), 
	   (46, 12), (33, 3), (24, 20), (7, 15), (69, 10), (12, 10), (39, 12), (47, 11), (48, 10),
	   (37, 13), (14, 19), (67, 10), (6, 10), (45, 15), (15, 18), (21, 12), (50, 18), (49, 11),
	   (61, 20), (25, 20), (38, 3), (70, 1), (11, 6), (43, 8), (8, 1), (51, 15), (59, 15),
	   (57, 3), (66, 14), (44, 7), (9, 19);



	    
	    