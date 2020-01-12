DROP DATABASE IF EXISTS spiderIndexer;
CREATE DATABASE IF NOT EXISTS spiderIndexer;
USE spiderIndexer;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS webpages;

CREATE TABLE webpages (
    pageID      INT             NOT NULL,
    URL  VARCHAR(14)     NOT NULL,
    webContent   VARCHAR(16)     NOT NULL,
    PRIMARY KEY (pageID)
);

SELECT 'LOADING employees' as 'INFO';
source load_employeeTest.dump ;

source show_elapsed.sql ;
