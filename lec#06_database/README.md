CRUD operations in FastAPI refer to the implementation of Create, Read, Update, and Delete functionalities for managing data, typically within a database or other persistent storage.

FastAPI doesn't require you to use a SQL (relational) database. But you can use any database that you want.
As SQLModel is based on SQLAlchemy, you can easily use any database supported by SQLAlchemy (which makes them also supported by SQLModel), like: PostgreSQL MySQL SQLite Oracle Microsoft SQL Server, etc.

Here is the database creation coomplete process.

1. create a **init**.py file in the root directory

2. main.py file it will contain the CRUD operations like we will create a table there using app.post()
   a) to create table run the --> models.base.metadata.create_all(engine)
   b) load the database my_db.db using the session created in the database.py file

   following are the functions for main.py file
   a) create a blogs
   b) get the blogs
   c) get the blog by id
   d) delete a blog
   e) update a blog

3. schema.py file will return the values in the database
   a) we have to create a base class there that will return the values defined inside that class

4. database.py fill contain the code to establish the database connections, the steps are
   a) first we need to create the engine for our database
   b) after creating engine we have to create a session
   c) finally create a ddecelartive base

5. create a models.py file to create the the tables and everything that we want in our table
   a) here we have to make use of the base class of database.py file's declerative base

6. create a database to store all values --> my_db.db
