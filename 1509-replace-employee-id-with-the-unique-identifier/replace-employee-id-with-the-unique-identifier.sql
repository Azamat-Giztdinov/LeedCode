# Write your MySQL query statement below
SELECT unique_id, name FROM Employees AS e LEFT JOIN EmployeeUNI AS ei ON e.id = ei.id