-- Lists all records of the second_table
-- Rows without a name value are not listed
-- Displays the score and the name in descending order of the score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
