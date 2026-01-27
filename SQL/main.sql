Create TABLE supplier(
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT
);


INSERT INTO supplier (SNO,SNAME,STATUS,CITY) VALUES
("s1","Smith",20,"London"),
("s2","Jones",10,"Paris"),
("s3","Blake",30,"London"),
("s4","Clark",30,"London"),
("s5","Adams",10,"Athens");


SELECT * FROM supplier;



