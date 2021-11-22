/* GET MAX SCORE PER CHALLENGE */
SELECT Hackers.hacker_id, Hackers.name, SUM(maximum.score) AS total 
FROM Hackers 
INNER JOIN (
            SELECT hacker_id, MAX(score) AS score 
            FROM SUBMISSIONS 
            GROUP BY hacker_id, challenge_id) AS maximum 
            ON Hackers.hacker_id = maximum.hacker_id
            GROUP BY Hackers.hacker_id, Hackers.name 
            HAVING total > 0 ORDER BY total DESC, Hackers.hacker_id ASC
