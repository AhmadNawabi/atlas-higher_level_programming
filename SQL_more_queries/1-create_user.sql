-- creates the MySQL server user user_0d_1.

-- Create user only if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
