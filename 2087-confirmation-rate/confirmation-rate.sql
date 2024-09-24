# Write your MySQL query statement below
select s.user_id, round(avg(if(c1.action="confirmed",1,0)),2)  as confirmation_rate
from Signups s
left join Confirmations c1 on c1.user_id= s.user_id
group by s.user_id;   