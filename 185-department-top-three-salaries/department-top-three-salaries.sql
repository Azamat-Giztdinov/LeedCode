-- Write your PostgreSQL query statement below
select department, employee, salary
from
(select 
    d.name as department, 
    e.name as employee, 
    salary,
    dense_rank() over(partition by e.departmentId order by e.salary desc) as shorted
from employee as e 
join department as d on e.departmentId = d.id)
where shorted <= 3