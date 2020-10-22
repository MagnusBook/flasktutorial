DROP TABLE IF EXISTS article;

CREATE TABLE article
(
    id INTEGER PRIMARY KEY,
    title TEXT,
    text TEXT,
    date TEXT
);

INSERT INTO article
    (id, title, text, date)
VALUES(1, 'Something bad happened today', 'Today was a bad day', '1999-04-12'),
    (2, 'Something good happened today', 'Today was a good day', '2004-04-01');