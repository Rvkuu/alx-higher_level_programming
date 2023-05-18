-- Script that will list all records of the table second_table having a name value.
-- The records will be ordered in a descending score.
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' != ""
ORDER BY 'score' DESC
