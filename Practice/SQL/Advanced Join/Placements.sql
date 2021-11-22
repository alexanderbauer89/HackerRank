SELECT Students.Name
FROM Students
INNER JOIN Friends ON Friends.ID   = Students.ID
INNER JOIN Packages ON Packages.ID = Students.ID
WHERE Packages.Salary < (SELECT Salary FROM Packages WHERE ID=Friends.Friend_id)
ORDER BY (SELECT Salary FROM Packages WHERE ID=Friends.Friend_id)
