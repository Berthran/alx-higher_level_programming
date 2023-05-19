-- Lists all records of the second_table of the hbtn_0c_0 database
-- where the score is greater than or equal to 10
--  Only the score and name columns are displayed
-- The scores are displayed in an descending order
SELECT score, name FROM second_table WHERE score>=10 ORDER BY score DESC;
