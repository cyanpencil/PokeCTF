FROM ubuntu:latest
RUN apt update
RUN apt install -y socat frotz npm 
RUN useradd -m poke
COPY pokectf/interactive_challs/web1 /home/poke/web1
RUN chown poke -R /home/poke/web1
EXPOSE 5004
CMD su poke /bin/bash -c "cd /home/poke/web1 && mkdir uploaded_files && npm install express http formidable path crypto querystring zombie && npm start"
