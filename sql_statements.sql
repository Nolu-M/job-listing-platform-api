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

ALTER TABLE job
ADD job_location TEXT;


INSERT INTO job( job_name, job_type, job_posted, job_location)
VALUES ('Backend engineer', 'Contract', '2023-07-14', 'Gauteng');