/*¿Cuáles son los productos más vendidos?*/

SELECT p.id,p.title, sum(quantity) as total_ventas FROM Products p JOIN Carts c on p.id=c.productId GROUP by p.id, p.title ORDER by total_ventas DESC;

/*¿Cuál es el promedio, mínimo y máximo precio por categoría de producto?*/

SELECT category, round(avg(price),2) as precio_promedio FROM Products GROUP by category;

/*¿Qué productos tienen mejor rating y cuántas calificaciones tienen?*/

SELECT title, rating, rating_count FROM Products ORDER by rating DESC

/*¿Cuántos usuarios se registraron en marzo?*/

SELECT count(userId) as "registrados_marzo" from Carts WHERE "date" like "2020-03-%"

/*¿Cuantos usuarios hay por ciudad y región)?*/

SELECT count(username) as "users_per_city", city FROM Users GROUP by city ORDER by "users_per_city" DESC

/*¿Cuántos usuarios hicieron compras en enero?*/

SELECT count(DISTINCT userId) as "total_compras_usuarios_enero" FROM Carts where strftime('%m',cart_date= '01')

/*¿Cuáles son los usuarios con mayor gasto acumulado?*/

SELECT u.username, sum(p.price *c.quantity) as gasto_acumulado FROM Carts c JOIN Users u on c.userId=u.id
JOIN Products p on c.productId=p.id GROUP BY u.username ORDER BY gasto_acumulado DESC;

/*¿Cuál es el total de ventas (cantidad y monto) por mes?*/

SELECT strftime('%m',c.cart_date) as mes,sum(c.quantity) as cantidad, sum(p.price*c.quantity) as Monto FROM Carts c JOIN Products p on p.id = c.productId GROUP by mes ORDER by c.quantity DESC

