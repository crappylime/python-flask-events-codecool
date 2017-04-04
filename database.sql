-- Put here SQL statements that creates structure of database, e.g.
--   CREATE TABLE users (id INT PRIMARY KEY NOT NULL, full_name CHAR(50) NOT NULL);
--
-- Put statments below
CREATE TABLE IF NOT EXISTS `events`(
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`date`	DATE,
	`description`	TEXT
);
