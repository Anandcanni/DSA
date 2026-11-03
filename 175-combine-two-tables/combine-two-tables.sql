# Write your MySQL query statement below
select e.firstName , e.lastName , eu.city , eu.state
from Person e
left join Address eu
on e.personId = eu.personId 
