SET @row := 21;
SELECT REPEAT('* ', @row := @row - 1) 
FROM information_schema.tables 
WHERE @row > 0
