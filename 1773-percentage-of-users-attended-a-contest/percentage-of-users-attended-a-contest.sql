# Write your MySQL query statement below
select r.contest_id , ROUND(COUNT(DISTINCT r.user_id)/COUNT(DISTINCT u.user_id)*100,2) as percentage 
from Register r ,Users u
group by contest_id order by percentage DESC, contest_id ASC