-- 1 --
CREATE TABLE peliculas(id int primary key, nombre varchar(255), anno int);

CREATE TABLE tags(id int primary key, tag varchar(32));

CREATE TABLE peliculastags(idpelicula int REFERENCES peliculas(id), idtag int REFERENCES tags(id));
-- 2 --
INSERT INTO peliculas VALUES(1, 'avatar', 2010);
INSERT INTO peliculas VALUES(2, 'pulp fiction', 1994);
INSERT INTO peliculas VALUES(3, 'la odisea', 2026);
INSERT INTO peliculas VALUES(4, 'matrix', 1999);
INSERT INTO peliculas VALUES(5, 'buscando a nemo', 2003);

INSERT INTO tags VALUES(1, 'ciencia ficcion');
INSERT INTO tags VALUES(2, 'espacial');
INSERT INTO tags VALUES(3, 'aventura');
INSERT INTO tags VALUES(4, 'comedia negra');
INSERT INTO tags VALUES(5, 'crimen');

INSERT INTO peliculastags VALUES(1, 1);
INSERT INTO peliculastags VALUES(1, 2);
INSERT INTO peliculastags VALUES(1, 3);
INSERT INTO peliculastags VALUES(2, 4);
INSERT INTO peliculastags VALUES(2, 5);
-- 3 --
SELECT p.nombre, COUNT(pt.idtag) FROM peliculas p LEFT JOIN peliculastags pt ON p.id = pt.idpelicula GROUP BY p.nombre;

-- parte II --
-- 4 --
CREATE TABLE preguntas(id int primary key, pregunta varchar(255), respuesta_correcta varchar);
CREATE TABLE usuarios(id int primary key, nombre varchar(255), edad int);

CREATE TABLE respuestas(id int primary key, respuesta varchar(255), usuario_id int REFERENCES usuarios(id), pregunta_id int REFERENCES preguntas(id));
-- 5 --
INSERT INTO usuarios VALUES(1, 'seba', 30);
INSERT INTO usuarios VALUES(2, 'valeska', 89);
INSERT INTO usuarios VALUES(3, 'maria', 27);
INSERT INTO usuarios VALUES(4, 'laura', 28);
INSERT INTO usuarios VALUES(5, 'mauricio', 29);

INSERT INTO preguntas VALUES(1, 'color del cielo?', 'celeste');
INSERT INTO preguntas VALUES(2, 'color del sol?', 'amarillo');
INSERT INTO preguntas VALUES(3, 'color del agua?', 'transparente');
INSERT INTO preguntas VALUES(4, 'color de la tierra?', 'cafe');
INSERT INTO preguntas VALUES(5, 'color del mar?', 'azul');

INSERT INTO respuestas VALUES(1, 'celeste', 1, 1);
INSERT INTO respuestas VALUES(2, 'celeste', 2, 1);
INSERT INTO respuestas VALUES(3, 'amarillo', 3, 2);
INSERT INTO respuestas VALUES(4, 'azul', 4, 3);
INSERT INTO respuestas VALUES(5, 'celeste', 5, 4);
-- hasta aqui fue lo que yo hice junto a la clase --
-- 6 --
SELECT
    u.nombre,
    SUM(
        CASE
            WHEN r.respuesta = p.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas
FROM usuarios u
LEFT JOIN respuestas r
    ON u.id = r.usuario_id
LEFT JOIN preguntas p
    ON r.pregunta_id = p.id
GROUP BY u.id, u.nombre
ORDER BY u.id;
-- 7 --
SELECT p.pregunta, 
SUM(
        CASE
            WHEN r.respuesta = p.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas
FROM preguntas p LEFT JOIN respuestas r ON p.id=r.pregunta_id LEFT JOIN usuarios u ON r.usuario_id=u.id 
GROUP BY p.pregunta;
-- 8 --
ALTER TABLE respuestas DROP CONSTRAINT respuestas_usuarios_id_fkey, ADD FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE;
DELETE FROM usuarios WHERE id=1;  --prueba del codigo anterior --
-- 9 --
ALTER TABLE usuarios ADD CONSTRAINT edad CHECK (edad>18);
INSERT INTO usuarios VALUES(6, 'constanza', 17); -- nuevo usuario menor --
-- 10 --
ALTER TABLE usuarios ADD COLUMN email varchar UNIQUE;

-- EXPLICAR TODA LA LOGICA EN UN VIDEO CORTO PARECE --

"""

CODIGO COMPLETO DIA 04/08/2026

#Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la pregunta).
SELECT
    u.nombre,
    SUM(
        CASE
            WHEN r.respuesta = p.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas
FROM usuarios u
LEFT JOIN respuestas r
    ON u.id = r.usuario_id
LEFT JOIN preguntas p
    ON r.pregunta_id = p.id
GROUP BY u.id, u.nombre
ORDER BY u.id;

#Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la respuesta correcta.
SELECT p.pregunta,    
SUM(
        CASE
            WHEN r.respuesta = p.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas 
FROM preguntas p 
LEFT JOIN respuestas r 
ON p.id=r.pregunta_id 
LEFT JOIN usuarios u 
ON r.usuario_id=u.id
GROUP BY p.pregunta;

#Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el primer usuario para probar la implementación.
ALTER TABLE respuestas DROP CONSTRAINT respuestas_usuario_id_fkey, ADD FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE;
DELETE FROM usuarios WHERE id=1;

#Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos.
ALTER TABLE usuarios ADD CONSTRAINT edad CHECK (edad>18);
INSERT INTO usuarios VALUES(6, 'camila', 17);

#Altera la tabla existente de usuarios agregando el campo email con la restricción de único.
ALTER TABLE usuarios ADD COLUMN email varchar UNIQUE;
"""
