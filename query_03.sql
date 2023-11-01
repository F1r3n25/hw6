--Знайти середній бал у групах з певного предмета


SELECT s.group_id, AVG(grade) as average_grade
FROM students s
INNER JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 5
GROUP BY s.group_id