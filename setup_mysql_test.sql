-- script that prepares a MySQL server for testing
-- if base doesn't exists, create  hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- CRATE A NEW USER IF NOT EXISTS FOR TESTING
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give all previliges to the user hbnb_test for hbnb_test_db database 
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- give select previliges to the user  hbnb_test for performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- FLUSING process
FLUSH PRIVILEGES;
