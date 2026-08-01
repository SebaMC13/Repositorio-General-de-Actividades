CREATE TABLE clientes (
   email varchar(50),
   nombre varchar,
   telefono varchar(16),
   empresa varchar(50),
   prioridad smallint
);

INSERT INTO 
clientes 
VALUES 
('abc@gmail.com', 'abc', '987654321', 'qwerty', 10), 
('zxc@gmail.com', 'zxc', '982323321', 'qwerta', 7),
('asd@gmail.com', 'asd', '987656321', 'qwerts', 3),
('tyu@gmail.com', 'tyu', '987123221', 'qwertd', 2),
('mnb@gmail.com', 'mnb', '984574321', 'qwertf', 4)
('sustituto@gmail.com', 'sqwerty', '884574321', 'qwerty', 4)
;

SELECT * FROM clientes;

SELECT * FROM clientes ORDER BY prioridad DESC LIMIT 3;

SELECT * FROM clientes WHERE empresa = 'qwerty';

SELECT * FROM clientes WHERE prioridad = 4;