SELECT s.name, g.code as group_code FROM students AS s JOIN groups AS g ON g.id = s.group_id WHERE s.group_id = 2 