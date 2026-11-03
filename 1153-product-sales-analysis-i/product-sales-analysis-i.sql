# Write your MySQL query statement below
select eu.product_name , e.year ,e.price
from Sales e
left join Product eu
on e.product_id = eu.product_id

