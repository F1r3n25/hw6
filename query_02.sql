--Знайти студента із найвищим середнім балом з певного предмета


SELECT g.student_id, ROUND(AVG(g.grade),2) as avgMark FROM grades g
WHERE g.subject_id = 8
Group by g.student_id
ORDER by avgMark DESC
Limit 1
