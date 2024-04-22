create table practicas.app_ahorro(numero int);
select * from practicas.app_ahorro;
use practicas;
insert into app_ahorro (numero, fecha) values (214, curdate());
delete from app_ahorro;
SET SQL_SAFE_UPDATES = 0;
delete from app_ahorro where fecha = 2024-01-03;
select numero, fecha, sum(numero) as ahorro_total from app_ahorro;
select count(numero) from app_ahorro;
SELECT numero, COUNT(*) as cantidad_repeticiones
FROM app_ahorro
GROUP BY numero
HAVING cantidad_repeticiones > 1;
select sum(numero) from app_ahorro;