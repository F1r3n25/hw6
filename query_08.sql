-- Знайти середній бал, який ставить певний викладач зі своїх предметів

SELECT s.subject, AVG(g.grade) as avrGrade
FROM subjects s
LEFT JOIN grades g ON s.id = g.subject_id
WHERE s.teacher_id = 1
GROUP BY s.subject