# Write your MySQL query statement below
select Project.project_id,round(sum(Employee.experience_years)/count(Employee.experience_years),2) as average_years
From Project
Join Employee On Employee.employee_id=Project.employee_id
group by project.project_id
Order by Project.project_id