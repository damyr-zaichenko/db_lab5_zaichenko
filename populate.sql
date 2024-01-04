INSERT INTO Comic (comic_id, comic_name, comic_price, comic_format) VALUES
(1, 'A Year of Marvels: April Infinite Comic (2016) #1', 'Free', 'Infinite Comic'),
(2, 'A Year of Marvels: August Infinite Comic (2016) #1', 'Free', 'Infinite Comic'),
(3, 'A Year of Marvels: February Infinite Comic (2016) #1', 'Free', 'Infinite Comic'),
(4, 'A Year of Marvels: July Infinite Comic (2016) #1', 'Free', 'Infinite Comic'),
(5, 'A+X (2012) #18', '$3.99', 'Comic'),
(6, 'A+X (2012) #17', '$3.99', 'Comic'),
(7, 'A-Force (2015) #5', '$3.99', 'Comic'),
(8, 'A-Force (2015) #4', '$3.99', 'Comic');

INSERT INTO Writer (writer_id, writer_name) VALUES
(1, 'Yves Bigerel'),
(2, 'Chris Sims'),
(3, 'Chad Bowers'),
(4, 'Ryan North'),
(5, 'Chuck Wendig'),
(6, 'Gerry Duggan'),
(7, 'Jim Krueger'),
(8, 'Jeff Loveness'),
(9, 'G. Willow Wilson'),
(10, 'Marguerite Bennett');

INSERT INTO Written (comic_id, writer_id, date) VALUES
(1, 1, 'April 01, 2016'),
(2, 2, 'August 10, 2016'),
(2, 3, 'August 10, 2016'),
(3, 4, 'February 10, 2016'),
(4, 5, 'June 29, 2016'),
(5, 6, 'March 26, 2014'),
(5, 7, 'March 26, 2014'),
(6, 6, 'February 19, 2014'),
(6, 8, 'February 19, 2014'),
(7, 9, 'October 14, 2015'),
(7, 10, 'October 14, 2015'),
(8, 9, 'September 09, 2015'),
(8, 10, 'September 09, 2015');
