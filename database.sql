-- Put here SQL statements that creates structure of database, e.g.
--   CREATE TABLE users (id INT PRIMARY KEY NOT NULL, full_name CHAR(50) NOT NULL);
--
-- Put statements below
CREATE TABLE IF NOT EXISTS events (
	id	SERIAL PRIMARY KEY,
	name	VARCHAR(25) NOT NULL,
	date	DATE NOT NULL,
	description	VARCHAR(255)
);
