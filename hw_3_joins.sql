select * from employees as e;
select * from roles_employee as re ;
select * from roles as r ;
select * from salary as s ;
select * from employee_salary as es ;


-- 1. ������� ���� ���������� ��� �������� ���� � ����, ������ � ����������.
select employee_name, s.monthly_salary 
	from employees as e 
join employee_salary as es 
	on e.id = es.employee_id 
join salary as s 
	on es.salary_id = s.id ;


--  2. ������� ���� ���������� � ������� �� ������ 2000.
select employee_name, s.monthly_salary 
	from employees as e 
join employee_salary as es 
	on e.id = es.employee_id 
join salary as s 
	on es.salary_id = s.id 
where s.monthly_salary < 2000;


-- 3. ������� ��� ���������� �������, �� �������� �� ��� �� ��������. 
-- (�� ����, �� �� ������� ��� � ��������.)
select employee_name, s.monthly_salary 
from employee_salary as es 
left join employees as e 
	on es.employee_id = e.id 
join salary as s 
	on es.salary_id = s.id 
where employee_name isnull; 


-- 4. ������� ��� ���������� �������  ������ 2000 �� �������� �� ��� �� ��������. 
-- (�� ����, �� �� ������� ��� � ��������.)
select employee_name, s.monthly_salary 
from employee_salary as es 
left join employees as e 
	on es.employee_id = e.id 
join salary as s 
	on es.salary_id = s.id 
where employee_name isnull and s.monthly_salary < 2000; 


-- 5. ����� ���� ���������� ���� �� ��������� ��.
select  employee_name, es.salary_id 
	from employees as e 
left join employee_salary as es 
	on e.id = es.employee_id 
where salary_id isnull ;

--  6. ������� ���� ���������� � ���������� �� ���������.
select employee_name, r.role_name  
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id;
	
-- 7. ������� ����� � ��������� ������ Java �������������.
select employee_name, role_name 
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%Java %';


-- 8. ������� ����� � ��������� ������ Python �������������.
select employee_name , role_name  
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%Python%';

--  9. ������� ����� � ��������� ���� QA ���������.

select employee_name , role_name 
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%QA%';

--  10. ������� ����� � ��������� ������ QA ���������.
select employee_name , role_name  
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%Manual QA%';

--  11. ������� ����� � ��������� ��������������� QA
select employee_name, role_name 
	from employees as e 
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%Automation QA%';

-- 12. ������� ����� � �������� Junior ������������
select employee_name , role_name, monthly_salary  
	from employee_salary as es
right join employees as e 
	on es.employee_id = e.id 
left join salary as s 
	on es.salary_id = s.id
join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like 'Junior%'

--13. ������� ����� � �������� Middle ������������
select employee_name , role_name , monthly_salary
	from employees as e 
	join roles_employee as re 
		on e.id = re.employee_id 
	left join roles as r 
		on re.role_id = r.id 
	left join employee_salary as es 
		on re.employee_id = es.employee_id 
	left join salary as s 
		on s.id = es.salary_id
	where role_name like '%Middle%';

--  14. ������� ����� � �������� Senior ������������
select employee_name , role_name , monthly_salary 
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like '%Senior%'

--  15. ������� �������� Java �������������
select employee_name , role_name , monthly_salary 
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like '%Java %';

-- 16. ������� �������� Python �������������
select employee_name , role_name , monthly_salary  
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like '%Python %';

--  17. ������� ����� � �������� Junior Python �������������
select employee_name , role_name , monthly_salary  
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like 'Junior Python %';

-- 18. ������� ����� � �������� Middle JS �������������
select employee_name , role_name , monthly_salary  
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like 'Middle JavaScript %';

-- 19. ������� ����� � �������� Senior Java �������������
select employee_name , role_name , monthly_salary  
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like 'Senior Java %';

--  20. ������� �������� Junior QA ���������
select employee_name , role_name , monthly_salary  
	from employees as e 
left join roles_employee as re 
	on e.id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
full join employee_salary as es 
	on e.id = es.employee_id 
full join salary as s 
	on es.salary_id  = s.id 
where role_name like 'Junior% %QA% %';

-- 21. ������� ������� �������� ���� Junior ������������
select avg(monthly_salary)
	from salary as s 
join employee_salary as es 
	on s.id = es.salary_id 
join roles_employee as re 
	on es.employee_id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like 'Junior%';

--  22. ������� ����� ������� JS �������������
select sum(monthly_salary)
	from salary as s 
join employee_salary as es 
	on s.id = es.salary_id 
join roles_employee as re 
	on es.employee_id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%JavaScript%';

--  23. ������� ����������� �� QA ���������
select min(monthly_salary)
	from salary as s 
join employee_salary as es 
	on s.id = es.salary_id 
join roles_employee as re 
	on es.employee_id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%QA%';

--  24. ������� ������������ �� QA ���������
select max(monthly_salary)
	from salary as s 
join employee_salary as es 
	on s.id = es.salary_id 
join roles_employee as re 
	on es.employee_id = re.employee_id 
join roles as r 
	on re.role_id = r.id 
where role_name like '%QA%';

-- 25. ������� ���������� QA ���������
select count(role_name) as qty_QA from roles_employee as re 
join roles as r 
	on re.role_id = r.id 
where role_name like '%QA%';

-- 26. ������� ���������� Middle ������������.
select count(role_name) as qty_QA from roles_employee as re 
right join roles as r 
	on re.role_id = r.id 
where role_name like 'Middle%';

--27. ������� ���������� �������������
select count(role_name) as qty_dev from roles_employee as re 
right join roles as r 
	on re.role_id = r.id 
where role_name like '%developer%';

--28. ������� ���� (�����) �������� �������������.
select sum(monthly_salary) as fund_dev
	from salary as s 
	join employee_salary as es 
		on s.id = es.salary_id 
	left join roles_employee as re
		on es.employee_id = re.employee_id 
	join roles as r 
		on re.role_id = r.id 
	where role_name like '%developer';

--  29. ������� �����, ��������� � �� ���� ������������ �� �����������
select employee_name , role_name , monthly_salary
	from employees as e 
	join roles_employee as re 
		on e.id = re.employee_id 
	join roles as r 
		on re.role_id = r.id 
	join employee_salary as es 
		on re.employee_id = es.employee_id 
	join salary as s 
		on s.id = es.salary_id
	order by monthly_salary;
	
-- 30. ������� �����, ��������� � �� ���� ������������ �� ����������� 
-- � ������������ � ������� �� �� 1700 �� 2300
select employee_name , role_name , monthly_salary
	from employees as e 
	join roles_employee as re 
		on e.id = re.employee_id 
	join roles as r 
		on re.role_id = r.id 
	join employee_salary as es 
		on re.employee_id = es.employee_id 
	join salary as s 
		on s.id = es.salary_id
	where monthly_salary between 1700 and 2300
	order by monthly_salary ;

--  31. ������� �����, ��������� � �� ���� ������������ �� 
--  ����������� � ������������ � ������� �� ������ 2300
select employee_name , role_name , monthly_salary
	from employees as e 
	join roles_employee as re 
		on e.id = re.employee_id 
	join roles as r 
		on re.role_id = r.id 
	join employee_salary as es 
		on re.employee_id = es.employee_id 
	join salary as s 
		on s.id = es.salary_id
	where monthly_salary < 2300
	order by monthly_salary ;

--  32. ������� �����, ��������� � �� ���� ������������ �� ����������� 
--  � ������������ � ������� �� ����� 1100, 1500, 2000
select employee_name , role_name , monthly_salary
	from employees as e 
	join roles_employee as re 
		on e.id = re.employee_id 
	join roles as r 
		on re.role_id = r.id 
	join employee_salary as es 
		on re.employee_id = es.employee_id 
	join salary as s 
		on s.id = es.salary_id
	where monthly_salary in (1100, 1500, 2000)
	order by monthly_salary ;

