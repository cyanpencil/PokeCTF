FROM ubuntu:latest
RUN apt update
RUN apt install -y python-pip
RUN pip2 install Flask Flask-Login Flask-SQLAlchemy Flask-WTF SQLAlchemy WTForms Werkzeug flask-admin flask_security enum tornado psycopg2-binary 
RUN useradd -m poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/pokectf && python2 chals.py && python2 run.py'"]
