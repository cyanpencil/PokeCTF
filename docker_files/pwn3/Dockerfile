FROM ubuntu:latest
#RUN dpkg --add-architecture i386
RUN apt update
RUN apt install -y socat 
RUN useradd -m poke
COPY pokectf/static/league /home/poke/league
RUN echo "poke{UR_p0k3mOn_cH4mp_c0ngRaT5!!1}" > /home/poke/flag
RUN chown poke -R /home/poke
RUN chmod -w -R /home/poke
EXPOSE 5009
CMD su poke /bin/bash -c "cd;socat tcp-listen:5009,reuseaddr,fork exec:'/home/poke/league',pty,ctty"
