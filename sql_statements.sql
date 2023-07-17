CREATE TABLE email_alert (
	id SERIAL PRIMARY KEY,
	job TEXT NOT NULL,
	province TEXT NOT NULL,
	city TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE
);

CREATE TABLE jobs (
	id SERIAL PRIMARY KEY,
	job_title TEXT NOT NULL UNIQUE,
	company TEXT NOT NULL UNIQUE,
	job_location TEXT NOT NULL,
	job_desc TEXT NOT NULL,
	job_req_ TEXT NOT NULL
);

CREATE TABLE job (
	id SERIAL PRIMARY KEY,
	job_name TEXT NOT NULL UNIQUE,
	job_type TEXT NOT NULL UNIQUE,
	job_posted DATE NOT NULL
);

INSERT INTO job( job_name, job_type, job_posted)
VALUES ('Software engineer', 'Permanent', '2023-07-13');