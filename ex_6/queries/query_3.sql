SELECT g.code, ROUND(AVG(m.mark), 2) AS mark FROM groups AS g JOIN students AS s ON s.group_id = g.id JOIN marks as m ON m.student_id = s.id WHERE m.subject_id = 2 GROUP BY g.code 