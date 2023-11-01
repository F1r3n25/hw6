--Знайти оцінки студентів у окремій групі з певного предмета

SELECT s.name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 2 AND g.subject_id = 7