--https://leetcode.com/problems/department-highest-salary

SELECT Department.name AS Department, A.name AS Employee, A.salary as Salary
FROM Employee A LEFT JOIN Department ON A.departmentId = Department.id
WHERE A.salary = (SELECT MAX(salary) FROM Employee AS B WHERE A.departmentId = B.departmentId)