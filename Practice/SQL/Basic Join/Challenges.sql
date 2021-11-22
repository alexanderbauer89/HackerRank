SELECT hacker_id AS hid, (SELECT name FROM Hackers WHERE hacker_id=hid), COUNT(*) as cnt
FROM Challenges 
GROUP BY hacker_id
HAVING cnt = (
    /* SELECT MAX RANK */
    SELECT MAX(maxx.rank)
    FROM(
        SELECT COUNT(*) AS rank
        FROM Challenges
        GROUP BY hacker_id
    ) AS maxx
) 
OR cnt IN (
    /* SELECT ALL RANKS WITH ONE HACKER */
    SELECT single.rank
    FROM (
        SELECT COUNT(*) AS rank
        FROM Challenges
        GROUP BY hacker_id
    ) AS single
    GROUP BY single.rank
    HAVING COUNT(single.rank) = 1
)
ORDER BY cnt DESC, hacker_id ASC
