--Оцінки студентів у певній групі з певного предмета на останньому занятті

SELECT g.student_id, g.grade
FROM grades g
INNER JOIN students s ON g.student_id = s.id
WHERE s.group_id = 1 AND g.subject_id = 4
ORDER BY g.date DESC
LIMIT 1;