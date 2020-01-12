DROP DATABASE IF EXISTS spiderIndexer;
CREATE DATABASE IF NOT EXISTS spiderIndexer;
USE spiderIndexer;

DROP TABLE IF EXISTS webpages;

CREATE TABLE webpages (
    pageID      INT             NOT NULL,
    URL  VARCHAR(14)     NOT NULL,
    webContent   VARCHAR(16)     NOT NULL,
    PRIMARY KEY (pageID)
);

INSERT INTO `webpages` VALUES (1,'Georgi','Facello'),
(2,'Bezalel','Simmel'),
(3,'Yinghua','Dredge'),
(4,'Jaewon','Syrzycki');
