migrate:
	# python3 manage.py db init;
	python3 manage.py db migrate; 
	python3 manage.py db upgrade; 

run:
	make install-dependency;
	python3 app.py;

install-dependency:
	pip3 install flask;
	pip3 install flask_sqlalchemy;
	pip3 install pinject;
	pip3 install bcrypt;