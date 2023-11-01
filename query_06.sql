--Знайти список студентів у певній групі

SELECT g.name as groupname, COUNT(s.name) as quantity From students s
JOIN groups g ON s.group_id = g.id
GROUP BY group_id