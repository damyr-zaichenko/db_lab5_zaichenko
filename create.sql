CREATE TABLE Comic
(
  comic_id INT NOT NULL,
  comic_name VARCHAR(200) NOT NULL,
  comic_price VARCHAR(20) NOT NULL,
  comic_format VARCHAR(200) NOT NULL,
  PRIMARY KEY (comic_id)
);

CREATE TABLE Writer
(
  writer_id INT NOT NULL,
  writer_name VARCHAR(200) NOT NULL,
  PRIMARY KEY (writer_id)
);

CREATE TABLE Written
(
  date DATE NOT NULL,
  writer_id INT NOT NULL,
  comic_id INT NOT NULL,
  FOREIGN KEY (writer_id) REFERENCES Writer(writer_id),
  FOREIGN KEY (comic_id) REFERENCES Comic(comic_id)
);