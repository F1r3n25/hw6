--Знайти які курси читає певний викладач

SELECT t.name, s.subject FROM teachers t
JOIN subjects s ON t.id = s.teacher_id