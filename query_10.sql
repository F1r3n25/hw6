-- Список курсів, які певному студенту читає певний викладач

SELECT groups.name AS course_name, subjects.subject AS subject_name, teachers.name AS teacher_name
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 23;