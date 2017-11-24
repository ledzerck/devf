## Bases de datos
* Es un conjunto de datos relacionados


#### Propiedades
* Independencia en sus datos
* Redundancia mínima
* Acceso por múltiples usuarios a la vez
* Integridad en los datos
* Consultas optimizadas
* Seguridad de acceso y auditoría
* Backups y restores


#### Gestores de bases de datos SGBD
* Te permiten tener acceso a la base de datos de una forma gráfica
* PGadmin, SQLserver, phpMyAdmin, etc.

----

## Tipos de bases de datos
* **SQL**
  * Todas se manejan muy parecido
  * Estas son relacionales
  * Pueden estar orientadas a diferentes cosas
  * SQLserver, PostgreSQL, MySQL
* **No SQL**
  * mongoDB, Redis, membase, CouchDB, MariaDB

### Ejemplo SQL

|USER|
|-|
|id (Primary key) ---------|
|Nombre|

|CLASE|
|-|
|id_clase|
|--------- id (Foreign key)|
|clase|

* La Primary key no se puede repetir
* La foreign Key debe ser la Primary Key en la otra tabla

#### Modelo entidad relación
* Esuna herramienta para modelar datos de un sistemade información

### ORM
* Object Relational Mapping
* Es un intermediario entre el lenguaje y las BD
* Se encarga de convertir los objetos en sentencias SQL

---

# Tarea

* Instalar PostgreSQL
* Instalar PGadmin

---


### PostgreSQL y PGadmin
* Configurar en ubuntu https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-16-04-es
* Dar de alta una base de datos
  * sudo -i -u postgres
  * psql postgres
  * CREATE ROLE prueba WITH LOGIN PASSWORD 'prueba';
  * CREATE DATABASE cintaroja;
  * GRANT ALL PRIVILEGES ON DATABASE cintaroja TO prueba;
  * Para salir \ quit
* PGadmin
  * Add a connection to server

* Click en botón SQL

CREATE TABLE User_cinta (
id_user int,
nombre char(50),
apellido char(50),
edad int,
PRIMARY KEY(id_user)
);

* execute query
* Click secundario en Databases: Refresh

* Nuevo SQL para agregar datos a esa tabla:

INSERT INTO user_cinta(id_user,nombre,apellido,edad) VALUES(1,'JUAN','Juarez',30)

* Para hacer una consulta:

SELECT * FROM user_cinta;

---

* Herramientas para trabajar con la BD Postgres y Flask
* Ir al entorno virtual e instalar:
  * pip install psycopg2
  * pip install SQLAlchemy
  * pip install Flask-SQLAlchemy

* Hay que crear un archivo config.py
