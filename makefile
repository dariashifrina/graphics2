run: app.py
	python app.py
	convert wow.ppm wow.png
	display wow.png
clean:
	rm *.pyc
	rm *~
