-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sh_db;
CREATE USER IF NOT EXISTS 'sh_user'@'localhost' IDENTIFIED BY 'sch_#3#_pwd';
GRANT ALL PRIVILEGES ON `sh_db`.* TO 'sh_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sh_user'@'localhost';
FLUSH PRIVILEGES;
