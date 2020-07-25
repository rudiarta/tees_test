## How to use with docker

first you must change ip `.env` file from `127.0.0.1` to `7.7.7.3`
then you can type command below:
```sh
    $ docker-compose up --build
```

then after that you can use mysql client to input first admin user query in `admin_user.sql`

username = admin

password = admin

(to use on login)

#

the connection for the mysql:

host = 127.0.0.1

port = 3306

user = root

password = maulapor

database = maulapor

## How to use without docker

run the mysql in your client config `.env` to your mysql config
then run command below:
```sh
    $ python3 app.py
```
to run the migrate database
```sh
    $ python3 manage.py db init
    $ python3 manage.py db migrate
    $ python3 manage.py db upgrade
```

or simply you kan use Makefile command:
```sh
    $ make run
```
for the migrate
```sh
    $ make init
    $ make migrate 
```

then after that you can use mysql client to input first admin user query in `admin_user.sql`

username = admin

password = admin

(to use on login)

#

this is the API endpoint postman collection link: https://www.getpostman.com/collections/e748a5d853ef56752ff0