FROM ubuntu:latest

WORKDIR /coypu_demo
ADD . /coypu_demo

RUN apt-get --assume-yes update
RUN apt-get --assume-yes upgrade
RUN apt-get --assume-yes install python3 python3-pip
RUN pip3 install -r requirements.txt
CMD tail -f /dev/null


# docker build -t coypu_demo:latest .
# docker tag coypu_demo:latest coypu_demo:1.0
# docker push coypu_demo:1.0