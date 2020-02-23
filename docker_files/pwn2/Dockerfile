FROM ubuntu:latest
RUN dpkg --add-architecture i386
RUN apt update
RUN apt install -y socat libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m poke
COPY pokectf/static/pwn2 /home/poke/pwn2
RUN echo "poke{I_h0p3_u_l1k3_str1ngs_:)}" > /home/poke/flag
RUN chown poke -R /home/poke
RUN chmod -w -R /home/poke
EXPOSE 5001
CMD su poke /bin/bash -c "cd;socat tcp-listen:5001,reuseaddr,fork exec:'/home/poke/pwn2'"
