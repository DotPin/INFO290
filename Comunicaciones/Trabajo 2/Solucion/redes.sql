PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE redes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	channel INTEGER,
	power INTEGER,
	ESSID TEXT,
	FILE TEXT);
COMMIT;
