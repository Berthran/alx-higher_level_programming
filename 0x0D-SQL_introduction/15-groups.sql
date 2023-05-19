-- Lists the number of records with the same score from the second_table
-- Displays the score
-- Displays the number of records for that score with a label number
-- Displays a sorted list in descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;

-- This works too
-- SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;
