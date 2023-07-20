-- Create email alert table
CREATE TABLE email_alert (
	id SERIAL PRIMARY KEY,
	job TEXT NOT NULL,
	province TEXT NOT NULL,
	city TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE
);

-- Create jobs table for the job card
CREATE TABLE jobs (
	id SERIAL PRIMARY KEY,
	job_title TEXT NOT NULL,
	job_type TEXT NOT NULL,
	job_posted TEXT NOT NULL,
	job_location TEXT NOT NULL,
	job_slug TEXT NOT NULL UNIQUE
);

-- Insert initial jobs
INSERT INTO jobs (job_title, job_type, job_posted, job_location,
				 job_slug)
VALUES ('Software engineer', 'Permanent', '27 June 2023', 'Eastern Cape', 'software-engineer'),
('Backend engineer', 'Contract', '29 June 2023', 'Eastern Cape', 'backend-engineer'),
('Software engineer', 'Permanent', '22 June 2023', 'Western Cape', 'frontend-engineer');


