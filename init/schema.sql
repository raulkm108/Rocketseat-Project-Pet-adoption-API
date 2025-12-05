CREATE TABLE IF NOT EXISTS 'pets' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES people(id)
);

CREATE TABLE IF NOT EXISTS 'people' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
);

INSERT INTO pets (name, type)
VALUES
    ("cobra", "snake"),
    ("cao", "dog"),
    ("gato", "cat"),
    ("jorgin", "hamster"),
    ("burro", "donkey"),
    ("shrek", "ogro"),
    ("belinha", "dog");