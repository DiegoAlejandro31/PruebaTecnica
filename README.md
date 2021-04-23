# PruebaTecnica

Se analizo la informacion brindada de SEPOMEX, y se identificaron los atributos para poder generar la base de datos que son d_estado, D_nmpio, d_asenta, d_CP 
(Estado,municipio,colonia y codigo postal), para la base de datos se opto por utlizar phpMyadmin Mysql, los datos de SEPOMEX se extrajeron del documento excel proporcionado
y para cargarlos en la base de datos se opto Mysql for excel, para la base de datos se opto elejir una que estuviera en un servidor en la nube.
Por lo que uso la siguiente direccion https://www.freemysqlhosting.net/.

La base de datos se puede probar de la sig. manera:

Ingresando a https://www.phpmyadmin.co/ 
Server: sql10.freemysqlhosting.net
Name: sql10407298
Username: sql10407298
Password: bMthrJ6lsK
Port number: 3306

Para generar las conexiones api se uso el framework flask la cual permite manejar la base de datos.

el archivo db.py realiza la conexion con la base datos.

el archivo app.py sirver para manejarla en este caso solo se agrego busqueda, insertar, actualizar y borrar.

Considerasiones:
- se tiene que ejecutar en un entorno virtual.
- se debera importar las librerias flask, request, jsonify y pymysql.

Los puntos restantes no se agregaron por cuestiones de tiempo.
