migrate:
	python3 manage.py db migrate; 
	python3 manage.py db upgrade; 

init:
	python3 manage.py db init; 

run:
	make install-dependency;
	python3 app.py;

install-dependency:
	pip3 install flask;
	pip3 install flask_sqlalchemy;
	pip3 install pinject;
	pip3 install bcrypt;
	pip3 install pyjwt;
	pip3 install flask_script;
	pip3 install flask_migrate;
	pip3 install pymysql;
	pip3 install python-dotenv;
	pip3 install coverage;

run-test:
	python3 -m unittest test.py;
	# python3 -m coverage run test.py;
	# python3 -m coverage report;