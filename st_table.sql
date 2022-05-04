DROP TABLE IF EXISTS students;

CREATE TABLE students (
  sno VARCHAR(20) not null,
  sname VARCHAR(20) not null,
  ssex VARCHAR(20) not null DEFAULT 'female',
  sbirthday DATE,
  sclass VARCHAR(20)
  );