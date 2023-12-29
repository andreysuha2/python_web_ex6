SELECT s.name, ROUND(AVG(m.mark), 2) as mark FROM students AS s JOIN marks as m ON s.id = m.student_id  GROUP BY s.name ORDER BY mark DESC LIMIT 5