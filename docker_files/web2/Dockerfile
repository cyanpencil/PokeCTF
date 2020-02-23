FROM ubuntu:latest
RUN apt update
RUN apt install -y python-pip
RUN pip2 install Flask Werkzeug flask-admin flask_security enum tornado psycopg2-binary 
RUN useradd -m poke
COPY pokectf/interactive_challs/web2 /home/poke/web2
RUN echo "poke{3V3n_pYth0n_c4n_b_vuLn}" > /home/poke/flag
RUN chown poke -R /home/poke
EXPOSE 5005
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/web2 && python2 run.py'"]
