FROM ubuntu:latest
RUN apt update
RUN apt install -y socat python3
COPY pokectf/interactive_challs/calculate_me.py /calculate_me.py
EXPOSE 5002
CMD /bin/bash -c "socat tcp-listen:5002,reuseaddr,fork exec:'python3 /calculate_me.py'"
