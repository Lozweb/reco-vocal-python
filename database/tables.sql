CREATE TABLE IF NOT EXISTS "Question" (
	"guess"	TEXT UNIQUE,
	"responseUUID"	TEXT
);

CREATE TABLE IF NOT EXISTS "Response" (
	"UUID"	TEXT UNIQUE,
	"response"	TEXT,
	"type"	TEXT,
	"command"	TEXT
);