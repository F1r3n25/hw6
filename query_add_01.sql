--Середній бал, який певний викладач ставить певному студентові

SELECT subjects.teacher_id, AVG(grades.grade) AS average_grade
FROM grades
INNER JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = 1 AND grades.student_id = 4;
