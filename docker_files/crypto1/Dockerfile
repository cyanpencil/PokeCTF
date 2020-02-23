FROM alpine
ENV FLAG="poke{CrYpTo_4nd_sn3ks?U_M4D_br0!}"
RUN apk add --no-cache python3 python3-dev gcc musl-dev gmp-dev socat
RUN pip3 install fastecdsa
RUN mkdir /app
WORKDIR /app
COPY pokectf/interactive_challs/crypto1/* /app/
EXPOSE 5007
CMD ["/bin/sh", "/app/run.sh"]
