DROP DATABASE IF EXISTS employees;
CREATE DATABASE IF NOT EXISTS employees;
USE employees;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_no      INT             NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,    
    PRIMARY KEY (emp_no)
);

INSERT INTO `employees` VALUES (10001,'Georgi','Facello','M'),
(10002,'Bezalel','Simmel','F'),
(10050,'Yinghua','Dredge','M'),
(10113,'Jaewon','Syrzycki','M');
