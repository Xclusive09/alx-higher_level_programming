-- Lists all records of the table second_table having a name value.
-- Records are ordered by descending score.
- list all coincidences--
SELECT
    score,
    name
FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
