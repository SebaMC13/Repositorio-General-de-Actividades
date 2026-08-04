-- prg 1 --
CREATE DATABASE PELICULAS
-- prg 2 --
CREATE TABLE peliculas(id int primary key, titulo varchar unique, añoestreno int, director varchar);
CREATE TABLE reparto(idpelicula int REFERENCES peliculas(id), actor varchar);
\copy peliculas FROM 'C:\Users\El Admin\peliculas.csv' csv header;
\copy reparto FROM 'C:\Users\El Admin\reparto.csv' csv header;
-- preg 3 --
SELECT id FROM peliculas WHERE LOWER(titulo) = 'titanic';
-- preg 4 --
SELECT actor FROM reparto WHERE idpelicula = 2;
-- preg 5 --
SELECT count(idpelicula) FROM reparto WHERE LOWER(actor) = 'harrison ford';
-- preg 6 --
SELECT * FROM peliculas WHERE añoestreno BETWEEN 1990 and 1999 ORDER BY titulo ASC;
-- preg 7 --
SELECT titulo, LENGTH(titulo) AS longitud_titulo FROM peliculas; 
-- preg 8 --
SELECT MAX(LENGTH(titulo)) AS longitud_titulo FROM peliculas;
-- mostrando titulo --
SELECT titulo, LENGTH(titulo) AS longitud_titulo FROM peliculas ORDER BY longitud_titulo DESC LIMIT 1;
