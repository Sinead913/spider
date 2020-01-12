DROP DATABASE IF EXISTS spiderIndexer;
CREATE DATABASE IF NOT EXISTS spiderIndexer;
USE spiderIndexer;

DROP TABLE IF EXISTS webpages;

CREATE TABLE webpages (
    URL  VARCHAR(14)     NOT NULL,
    webContent   VARCHAR(16)     NOT NULL
);
