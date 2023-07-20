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

--Create table for each job
CREATE TABLE job (
	id SERIAL PRIMARY KEY,
	title TEXT NOT NULL,
	company TEXT NOT NULL,
	job_location TEXT NOT NULL,
	salary INTEGER NOT NULL,
	description TEXT NOT NULL,
	requirements TEXT NOT NULL,
	slug TEXT NOT NULL UNIQUE
);

INSERT INTO job(title, company, job_location, salary,
			   description, requirements, slug)
VALUES ('Software engineer', 'Career Circuit', 'Eastern Cape',
	   '30000', 'Our client is currently looking for a qualified candidate to assist in our software development needs. The Developer will work alongside the rest of the team to develop, improve, and optimise our current software solutions and as well as new systems to follow.',
	   'Desired experience and qualifications: 3 year undergraduate degree or diploma in Computer Science or Information Systems, or a related field. Strong problem-solving skills.', 'software-engineer');