In this directory we have following folders and their functions 

1. db_connection.py --> to establish the db connection using engine, session and declerative base

2. models.py --> has the daytabase with table name and columns

3. schemas.py --> has classes to define the user and also a ShowUser class to not display the id

4. main.py --> contains the following functions
a) create a user with name, email, password
b) show the user by id
c) Update the user by id