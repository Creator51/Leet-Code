# Write your MySQL query statement below
select email from person GROUP BY email having count(email)>1