--Знайти список курсів, які відвідує студент

SELECT groups.name
FROM students
INNER JOIN groups ON students.group_id = groups.id
WHERE students.id = 12;