# Write your MySQL query statement below

select e1.firstName,e1.lastName,e2.city,e2.state 
from person e1 
left join address e2
on e1.personId=e2.personId
