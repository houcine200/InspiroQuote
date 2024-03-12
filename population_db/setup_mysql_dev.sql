-- Create or use an existing database
CREATE DATABASE IF NOT EXISTS iq_dev_db;

-- Create or use an existing user
CREATE USER IF NOT EXISTS 'iq_dev'@'localhost' IDENTIFIED BY 'iq_dev_pwd';

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON iq_dev_db.* TO 'iq_dev'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'iq_dev'@'localhost';
