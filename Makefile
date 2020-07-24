migrate:
	# python3 manage.py db init;
	python3 manage.py db migrate; 
	python3 manage.py db upgrade; 

run:
	python3 app.py;