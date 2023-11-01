--


SELECT s.name, ROUND(AVG(grade),2) as avgGrade FROM grades g
LEFT JOIN students as s ON s.id = g.student_id
GROUP BY student_id
ORDER BY avgGrade DESC
LIMIT 5;
