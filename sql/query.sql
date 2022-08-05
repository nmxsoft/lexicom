# Задача 4.1
SELECT * FROM customer a
JOIN city b
on a.cod = b.cod;
               
# Задача 4.2
SELECT a.name as person, b.name as city FROM customer a
LEFT JOIN city b
on a.cod = b.cod;
              
# Задача 4.3
SELECT a.name as person, b.name as city FROM city b
LEFT JOIN customer a
on a.cod = b.cod;
