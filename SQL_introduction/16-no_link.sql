-- lists all records oof the table second_table of the database in MySQL.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
