FROM ubuntu:latest
RUN apt update
RUN apt install -y wget git gcc libglfw3-dev libxcursor-dev libxinerama-dev libxi-dev libasound2-dev pkg-config
RUN wget https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz; tar -C /usr/local -xzf go1.13.3.linux-amd64.tar.gz
ENV PATH="/usr/local/go/bin:${PATH}"
RUN go get github.com/HFO4/gameboy.live; cd
WORKDIR /root/go/src/github.com/HFO4/gameboy.live/
RUN go build -o gbdotlive main.go
RUN wget www.cyanpencil.xyz/rom.tar; tar xvf rom.tar
EXPOSE 1989
CMD /bin/bash -c "cd /root/go/src/github.com/HFO4/gameboy.live/; ./gbdotlive -s -c './gameslist.json'"
