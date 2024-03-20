-- script that prepares a MySQL server for this project
-- if base doesn't exists, create  hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- CRATE A NEW USER IF NOT EXISTS
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- give all previliges to the user hbnb_dev for hbnb_dev_db database 
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- give select previliges to the user  hbnb_dev for erformance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- FLUSING process
FLUSH PRIVILEGES;
