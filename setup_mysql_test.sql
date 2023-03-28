-- prepares a MySQL server for the project for testing

CREATE DATABASE IF NOT EXISTS sh_test_db;
CREATE USER IF NOT EXISTS 'sh_test_user'@'localhost' IDENTIFIED BY 'Sch_t3st_#3#_pwd';
GRANT ALL PRIVILEGES ON `sh_test_db`.* TO 'sh_test_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sh_test_user'@'localhost';
FLUSH PRIVILEGES;
