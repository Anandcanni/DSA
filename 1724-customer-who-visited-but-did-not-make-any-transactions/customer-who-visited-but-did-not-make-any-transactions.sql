# Write your MySQL query statement below
select e.customer_id,count(e.visit_id) as count_no_trans
from Visits e
left join Transactions eu
on e.visit_id = eu.visit_id
where eu.transaction_id is null
group by e.customer_id
