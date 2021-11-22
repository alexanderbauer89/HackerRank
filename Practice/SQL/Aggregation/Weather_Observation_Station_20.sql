-- use of prepared statement due to limit restrictions neccessary --
SET @median = (SELECT FLOOR(COUNT(*)/2) FROM STATION);
PREPARE STMT FROM 'SELECT ROUND(LAT_N, 4)
FROM STATION
GROUP BY LAT_N
ORDER BY LAT_N ASC
LIMIT ?,1;';
EXECUTE STMT USING @median;
