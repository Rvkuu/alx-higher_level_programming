-- Scripts that will list the number of records with the same score in the table.
-- The records will be ordered by descending count.
SELECT 'score', COUNT (*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;
