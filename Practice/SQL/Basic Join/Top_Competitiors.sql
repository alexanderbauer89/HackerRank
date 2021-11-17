SELECT Submissions.hacker_id, Hackers.name
FROM Submissions
INNER JOIN Challenges ON Challenges.challenge_id = Submissions.challenge_id
INNER JOIN Difficulty ON Difficulty.difficulty_level = Challenges.difficulty_level
INNER JOIN Hackers ON Hackers.hacker_id = Submissions.hacker_id
WHERE Submissions.score = Difficulty.score
GROUP BY Submissions.hacker_id, Hackers.name
HAVING COUNT(Submissions.hacker_id) > 1
ORDER BY COUNT(Submissions.hacker_id) DESC, Submissions.hacker_id ASC
